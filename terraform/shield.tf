# ################################################################################
# # AWS Sheild protection for infrastructure
# ################################################################################

# Enable shield on RDS
resource "aws_shield_protection" "greengiants_rds" {
  name         = "greengiants_rds"
  resource_arn = aws_rds_cluster.aurora_cluster.arn
}