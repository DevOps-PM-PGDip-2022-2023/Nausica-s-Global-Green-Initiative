#not available in eu west
# locals {
#   region = "eu-west-1"

#   tags = {
#     Name        = "GreenGiants"
#     Environment = "Production"
#     Contact     = "GreenGiants"
#   }
# }

# ################################################################################
# # RDS Setup
# ################################################################################


# resource "aws_rds_cluster" "aurora_cluster" {

#   cluster_identifier           = "green-giants"
#   database_name                = "GreenGiants"
#   master_username              = "dbadmin"
#   master_password              = "12345678ab" #this will be change after the resource is created"
#   backup_retention_period      = 5
#   preferred_backup_window      = "02:00-03:00"
#   preferred_maintenance_window = "wed:03:00-wed:04:00"
#   availability_zones           = ["eu-west-1"]
#   #db_subnet_group_name          = "${aws_db_subnet_group.aurora_subnet_group.name}"
#   final_snapshot_identifier = "${var.environment_name}auroraCluster"

#   tags = local.tags

#   lifecycle {
#     create_before_destroy = true
#   }

# }

# resource "aws_rds_cluster_instance" "aurora_cluster_instance" {

#   count = length(split(",", var.vpc_rds_subnet_ids))

#   identifier         = "green-giants"
#   cluster_identifier = aws_rds_cluster.aurora_cluster.id
#   instance_class     = "db.t3.small"
#   #db_subnet_group_name  = "${aws_db_subnet_group.aurora_subnet_group.name}"
#   publicly_accessible = true

#   tags = local.tags

#   lifecycle {
#     create_before_destroy = true
#   }

# }

# #resource "aws_db_subnet_group" "aurora_subnet_group" {

# #    name          = "${var.environment_name}_aurora_db_subnet_group"
# #    description   = "Allowed subnets for Aurora DB cluster instances"
# #    subnet_ids = [aws_subnet.frontend.id, aws_subnet.backend.id]

# #    tags = local.tags

# #}


# ######### To do ###########
# #add security group with ingress rules 
# #Add tags
# #Resolve subnet names
# #config password to be not static but dynamic
