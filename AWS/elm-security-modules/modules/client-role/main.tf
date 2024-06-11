variable "primary_account_id" {
  description = "The ID of the primary account that will assume the role."
  type        = string
}

variable "role_name" {
  description = "The name of the IAM role to create."
  type        = string
  default     = "WAFManagementRole"
}



variable "aws_region" {
  description = "The AWS region where resources are deployed."
  type        = string
}

# Create the IAM role with the assume role policy
resource "aws_iam_role" "cross_account_role" {
  name = var.role_name

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          AWS = "arn:aws:iam::${var.primary_account_id}:root"
        },
        Action = "sts:AssumeRole"
      }
    ]
  })
}

# Attach the policy to the created IAM role
resource "aws_iam_role_policy" "waf_policy" {
  name   = "${var.role_name}_policy"
  role   = aws_iam_role.cross_account_role.id
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Action = [
          "wafv2:GetIPSet",
          "wafv2:UpdateIPSet"
        ],
        Resource = "arn:aws:wafv2:${var.aws_region}:${data.aws_caller_identity.current.account_id}:regional/ipset/managed_ipset*"
      }
    ]
  })
}

output "role_arn" {
  description = "The ARN of the created IAM role."
  value       = aws_iam_role.cross_account_role.arn
}

# Data source to get the current AWS account ID
data "aws_caller_identity" "current" {}
