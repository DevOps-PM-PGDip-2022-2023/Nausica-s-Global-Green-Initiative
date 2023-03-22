# ################################################################################
# # S3 Setup for terraform state
# ################################################################################

resource "aws_s3_bucket" "state_bucket" {
  bucket = var.bucket_name
  acl    = "private"

  tags = {
    Name = "GreenGiants"
  }
}