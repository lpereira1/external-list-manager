provider "aws" {
  region = "us-east-1"
  profile = "home-lab"
}

module "account_sandbox1_role" {
  source    = "./modules/client-role"
  role_name  = "IPSETMgr"
  primary_account_id = "98230125324"
  aws_region = "us-west-1"
}

module "primary_account_role" {
source = "./modules/primary-role"
}


