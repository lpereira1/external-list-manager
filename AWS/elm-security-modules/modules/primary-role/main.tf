variable "db_ipset_table_name" {
  description = "Name of the ipset dynamodb table"
  default = "IPSetActions"
}


data "aws_caller_identity" "current" {

}

data "aws_region" "current" {

}

# Creates the cross account role to assume other roles and deploy changes
resource "aws_iam_role" "whitelist-manager-role" {
  name = "whitelist-manager-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

# Attach combined policy to Lambda role for basic execution and WAF/DynamoDB access
resource "aws_iam_role_policy" "primary_ipset_policy" {
  name   = "sandbox-lambda-waf-policy"
  role   = aws_iam_role.whitelist-manager-role.id
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      # Basic Lambda execution permissions
      {
        Effect = "Allow",
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ],
        Resource = "arn:aws:logs:*:*:*"
      },
      # Custom WAF and DynamoDB permissions
      {
        Effect = "Allow",
        Action = [
          "dynamodb:PutItem",
          "sts:AssumeRole"
        ],
        Resource = [
          "arn:aws:dynamodb:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:table/${var.db_ipset_table_name}",
          "arn:aws:iam::*:role/WAFIPSETManagementRole"
        ]
      }
    ]
  })
}



