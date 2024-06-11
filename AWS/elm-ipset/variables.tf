variable "products" {
  description = "Map of products with their account details and IP set IDs."
  type = map(object({
    account_id = string
    role_name  = string
  }))
  default = {
    acldev1 = {
      account_id = "292372131272",
      role_name  = "WAFIPSETManagementRole"
    },
    acldev2 = {
      account_id = "292372131272",
      role_name  = "WAFIPSETManagementRole",
    }
    // Add more products/accounts as needed
  }
}