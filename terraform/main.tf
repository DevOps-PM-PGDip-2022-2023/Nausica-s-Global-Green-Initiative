################################################################################
# Create an EC2 instance for the Service
################################################################################

resource "aws_instance" "ec2_instance" {
  ami           = "${var.ami_id}"
  count         = "${var.number_of_instances}"
  key_name      = aws_key_pair.key_pair.id
  instance_type = "${var.instance_type}"
  monitoring    = true
}

resource "aws_security_group" "ec2_sg" {
  name        = "GreenGiants_ec2_sg"
  description = "Security group created for EC2 security group - managed by terraform"

  egress {
    from_port = 0
    to_port   = 0
    protocol  = "-1"
  }
}

resource "tls_private_key" "key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

# Generate a Private Key and encode it as PEM.
resource "aws_key_pair" "key_pair" {
  key_name   = "key"
  public_key = tls_private_key.key.public_key_openssh

  provisioner "local-exec" {
    command = "echo '${tls_private_key.key.private_key_pem}' > ./key.pem"
  }
}

######### To do ###########
#add name
#add security group with ingress rules 
#Add tags