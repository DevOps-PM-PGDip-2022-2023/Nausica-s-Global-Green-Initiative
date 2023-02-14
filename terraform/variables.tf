###### Access Key Setup #########
variable "access_key" {
        description = "Access key to AWS console"
}
variable "secret_key" {
        description = "Secret key to AWS console"
}

###### EC2 Instance Setup ########
variable "instance_name" {
        description = "Name of the instance to be created"
        default = "GreenGiants"
}

variable "instance_type" {
        default = "t2.micro"
}

variable "subnet_id" {
        description = "The VPC subnet the instance(s) will be created in"
        default = "subnet-07ebbe60"
}

variable "ami_id" {
        description = "The AMI to use"
        default = "ami-09d56f8956ab235b3"
}

variable "number_of_instances" {
        description = "number of instances to be created"
        default = 1
}


###### Aurora Setup ########
variable "environment_name" {
    description = "The name of the environment"
    default = "production"
}

variable "vpc_id" {
  description = "The ID of the VPC that the RDS cluster will be created in"
  default = ""

}

variable "vpc_name" {
  description = "The name of the VPC that the RDS cluster will be created in"
  default = ""

}

variable "vpc_rds_subnet_ids" {
  description = "The ID's of the VPC subnets that the RDS cluster instances will be created in"
  default = ""
}

variable "vpc_rds_security_group_id" {
    description = "The ID of the security group that should be used for the RDS cluster instances"
    default = ""

}

variable "rds_master_username" {
  description = "The ID's of the VPC subnets that the RDS cluster instances will be created in"
  default = "admin"
}

variable "rds_master_password" {
  description = "The ID's of the VPC subnets that the RDS cluster instances will be created in"
  default = "12345"
}

########################