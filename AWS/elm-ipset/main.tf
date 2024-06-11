# Provider configuration for AWS
provider "aws" {
  region = "us-east-1" # Adjust the region as needed
  profile = "home-lab"
}

# Data source to get the current AWS account ID
data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

data "aws_iam_role" "whitelist-role" {
  name = "prod-csvc-whitelist-mgr-role"
}


data "archive_file" "lambda_zip" {                                                                                                                                                                                   
  type        = "zip"                                                                                                                                                                                                
  source_dir  = "${path.module}/files/"                                                                                                                                                                                         
  output_path = "${path.module}/package/lambda_package.zip"                                                                                                                                                                         
}                                                


locals {
  product_ip_sets = { for product, details in var.products :
    product => {
      account_id = details.account_id
      role_name  = details.role_name
      ip_set_id  = "managed_ipset_${product}_customer_list"
    }
  }
}

# Lambda function to manage IP sets
resource "aws_lambda_function" "ip_manager" {
  filename         = data.archive_file.lambda_zip.output_path
  function_name    = "sandbox-whitelist-manager"
  role             = data.aws_iam_role.whitelist-role.arn
  handler          = "lambda_function.lambda_handler"
  runtime          = "python3.8"
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
  environment {
    variables = {
      TABLE_NAME = aws_dynamodb_table.IPSetActions.name
      WAF_SCOPE  = "REGIONAL"
      TARGET_ACCOUNTS = jsonencode(local.product_ip_sets)
      IP_SET_IDS = jsonencode({for k, v in aws_wafv2_ip_set.ip_set : k => v.arn})
    }
  }
}
