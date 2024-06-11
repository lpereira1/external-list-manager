import json
import boto3
import os
import ipaddress
from datetime import datetime

dynamodb = boto3.client('dynamodb')
sts_client = boto3.client('sts')

TABLE_NAME = "IPSetActions"
WAF_SCOPE = "REGIONAL" # or "CLOUDFRONT"

# Read and parse TARGET_ACCOUNTS from environment variable
TARGET_ACCOUNTS = json.loads(os.getenv('TARGET_ACCOUNTS', '{}'))
IP_SET_IDS = json.loads(os.getenv('IP_SET_IDS', {}))

def lambda_handler(event, context):
    ticket_id = event['ticketID']
    customer_id = event['customerID']
    ip_list = event['IPaddressCIDR']
    product_name = event['ProductName']
    ip_set_name = f"managed_ipset_{event['ProductName']}_customer_list"
    
    
    # Validate IP addresses
    valid_ips = []
    invalid_ips = []
    
    for ip in ip_list:
        if is_valid_ip(ip):
            valid_ips.append(ip)
        else:
            invalid_ips.append(ip)
    
    # Get target account details based on ProductName
    target_account = TARGET_ACCOUNTS.get(product_name)
    ip_set_id = IP_SET_IDS.get(product_name).split('/')[-1]
    if not target_account:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'Invalid ProductName'
            })
        }
    
    credentials = assume_role(target_account['account_id'], target_account['role_name'])
    
    waf_client = boto3.client(
        'wafv2',
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken']
    )
    
    # Check existing IPs in the IP set
    ip_set = waf_client.get_ip_set(Name=ip_set_name, Scope=WAF_SCOPE, Id=ip_set_id)
    existing_ips = ip_set['IPSet']['Addresses']
    lock_token = ip_set['LockToken']
    
    new_ips = [ip for ip in valid_ips if ip not in existing_ips]
    already_exists = [ip for ip in valid_ips if ip in existing_ips]
    
    # Update IP set
    if new_ips:
        waf_client.update_ip_set(
            Name=ip_set_name,
            Scope=WAF_SCOPE,
            Id=ip_set_id,
            Addresses=existing_ips + new_ips,
            LockToken=lock_token
        )
    
    # Update DynamoDB
    for ip in new_ips:
        timestamp = datetime.utcnow().isoformat()
        ip_address_timestamp = f"{ip}-{timestamp}"
        dynamodb.put_item(
            TableName=TABLE_NAME,
            Item={
                'CustomerID': {'S': customer_id},
                'IPAddressTimestamp': {'S': ip_address_timestamp},
                'TicketID': {'S': ticket_id},
                'ProductID': {'S': product_name},
                'Timestamp': {'S': timestamp},
                'IPAddress': {'S': ip}
            }
        )
    
    # Send comments to Samanage
    # Assuming samanage client and function is configured properly
    # samanage.send_comment(ticket_id=ticket_id, comment=f"Processed IPs: {json.dumps({'added': new_ips, 'existing': already_exists, 'invalid': invalid_ips})}")
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'IP addresses processed',
            'added': new_ips,
            'existing': already_exists,
            'invalid': invalid_ips
        })
    }

def is_valid_ip(ip):
    try:
        ip_addr = ipaddress.ip_network(ip, strict=False)
        # Check for private IP ranges
        if ip_addr.is_private or ip_addr.is_multicast or ip_addr.is_reserved:
            return False
        # Exclude 0.0.0.0/0
        if ip_addr == ipaddress.ip_network("0.0.0.0/0"):
            return False
        return True
    except ValueError:
        return False

def assume_role(account_id, role_name):
    response = sts_client.assume_role(
        RoleArn=f"arn:aws:iam::{account_id}:role/{role_name}",
        RoleSessionName="AssumeRoleSession"
    )
    return response['Credentials']
