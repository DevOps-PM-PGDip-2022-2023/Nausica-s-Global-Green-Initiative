################################################################################
# Create an IAM role to allow enhanced monitoring
################################################################################

data "aws_iam_policy_document" "monitoring_rds_assume_role" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["monitoring.rds.amazonaws.com"]
    }
  }
}

###########
# IAM
###########
#IAM role that permits RDS to send enhanced monitoring metrics to CloudWatch Logs

resource "aws_iam_role" "rds_enhanced_monitoring" {
  description        = "IAM Role for RDS Enhanced monitoring"
  path               = "/"
  assume_role_policy = data.aws_iam_policy_document.monitoring_rds_assume_role.json
  #managed_policy_arns = ["arn:${data.aws_partition.current.partition}:iam::aws:policy/service-role/AmazonRDSEnhancedMonitoringRole"]
}