locals {
  region = "us-east-1"

  tags = {
    Name        = "GreenGiants"
    Environment = "Production"
    Contact     = "GreenGiants"
  }
}


# ################################################################################
# # RDS Setup
# ################################################################################


resource "aws_rds_cluster" "aurora_cluster" {

  cluster_identifier           = "green-giants"
  database_name                = "GreenGiants"
  master_username              = "dbadmin"
  master_password              = "12345678ab" #this will be change after the resource is created"
  backup_retention_period      = 0
  preferred_backup_window      = "02:00-03:00"
  preferred_maintenance_window = "wed:03:00-wed:04:00"
  # availability_zones           = ["eu-west-1"] #error when applying in eurorpe
  skip_final_snapshot = true
  deletion_protection = false
  #db_subnet_group_name          = "${aws_db_subnet_group.aurora_subnet_group.name}"
  final_snapshot_identifier = "${var.environment_name}auroraCluster"

  tags = local.tags
}

resource "aws_rds_cluster_instance" "aurora_cluster_instance" {
  identifier         = "green-giants"
  cluster_identifier = aws_rds_cluster.aurora_cluster.id
  instance_class     = "db.t3.small"
  publicly_accessible = true

  tags = local.tags

}


#resource "aws_db_security_group" "aurora_sg" {
#  name        = "GreenGiants_sg"
#  description = "Security group used for aurora database"

#  ingress {
#    from_port = 0
#    to_port   = 3306
#    protocol  = "TCP"
#    #security_group_id = data.aws_security_group.ec2_sg.id #need to resolve
#  }

#}


######### To do ###########
#add security group with ingress rules 
