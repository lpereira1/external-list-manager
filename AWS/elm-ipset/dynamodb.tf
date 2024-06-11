# Create DynamoDB table for tracking IP actions
resource "aws_dynamodb_table" "IPSetActions" {
  name         = "IPSetActions"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "CustomerID"
  range_key    = "IPAddressTimestamp"

  attribute {
    name = "CustomerID"
    type = "S"
  }

  attribute {
    name = "IPAddressTimestamp"
    type = "S"
  }

  attribute {
    name = "TicketID"
    type = "S"
  }

  attribute {
    name = "ProductID"
    type = "S"
  }

  attribute {
    name = "Timestamp"
    type = "S"
  }

  attribute {
    name = "IPAddress"
    type = "S"
  }

  global_secondary_index {
    name            = "ProductIDIndex"
    hash_key        = "ProductID"
    range_key       = "Timestamp"
    projection_type = "ALL"
  }

  global_secondary_index {
    name            = "TicketIDIndex"
    hash_key        = "TicketID"
    range_key       = "Timestamp"
    projection_type = "ALL"
  }

  global_secondary_index {
    name            = "IPAddressIndex"
    hash_key        = "IPAddress"
    range_key       = "Timestamp"
    projection_type = "ALL"
  }
}
