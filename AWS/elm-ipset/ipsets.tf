# Create IP sets for each product ID
resource "aws_wafv2_ip_set" "ip_set" {
  for_each            = var.products
  name                = "managed_ipset_${each.key}_customer_list"
  scope               = "REGIONAL"
  ip_address_version  = "IPV4"
  addresses           = [] # Initially empty
  description         = "IP-set-for-${each.key}"

  tags = {
    Product = each.key
    ManagedBy = "Terraform"
  }

  lifecycle {
    ignore_changes = [ addresses ]
  }
}

output "ip_set_arns" {
  description = "The ARNs of the created IP sets."
  value       = { for k, v in aws_wafv2_ip_set.ip_set : k => v.arn }
}