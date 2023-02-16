resource "aws_instance" "ec2_instance" {
    ami = "${var.ami_id}"
    count = "${var.number_of_instances}"
    instance_type = "${var.instance_type}"
}

<<<<<<< HEAD
resource "aws_security_group" "ec2_sg" {
  name        = "GreenGiants_ec2_sg"
  description = "Security group created for EC2 security group - managed by terraform"


  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
  }
}

=======
>>>>>>> main
######### To do ###########
#add name
#add security group with ingress rules 
#Add tags