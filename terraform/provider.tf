provider "aws" {
  access_key = ""
  secret_key = ""
  region     = "eu-west-1"
  profile    = "default"
}

terraform {
  backend "s3" {
    bucket     = "green-giants"
    key        = "greengiants/terraform.tfstate"
    region     = "eu-west-1"
    encrypt    = true
  }
}