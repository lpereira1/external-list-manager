# API Gateway for the whitelist manager
resource "aws_api_gateway_rest_api" "whitelist_manager" {
  name        = "whitelist-manager-API"
  description = "API for managing WAF IP sets which are used to whitelist IP addresses"
}

# Resource for the /updateipset endpoint
resource "aws_api_gateway_resource" "whitelist_manager" {
  rest_api_id = aws_api_gateway_rest_api.whitelist_manager.id
  parent_id   = aws_api_gateway_rest_api.whitelist_manager.root_resource_id
  path_part   = "updateipset"
}

# Method for the /updateipset endpoint
resource "aws_api_gateway_method" "whitelist_manager_method" {
  rest_api_id   = aws_api_gateway_rest_api.whitelist_manager.id
  resource_id   = aws_api_gateway_resource.whitelist_manager.id
  http_method   = "POST"
  authorization = "NONE"
  api_key_required = true
}

# Integration of the /updateipset endpoint with the Lambda function
resource "aws_api_gateway_integration" "lambda_integration" {
  rest_api_id = aws_api_gateway_rest_api.whitelist_manager.id
  resource_id = aws_api_gateway_resource.whitelist_manager.id
  http_method = aws_api_gateway_method.whitelist_manager_method.http_method

  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.ip_manager.invoke_arn
}

# Grant API Gateway permission to invoke the Lambda function
resource "aws_lambda_permission" "allow_api_gateway" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.ip_manager.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.whitelist_manager.execution_arn}/*/*"
}