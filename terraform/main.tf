resource "aws_instance" "ec2_instance" {
    ami = "${var.ami_id}"
    count = "${var.number_of_instances}"
    instance_type = "${var.instance_type}"
}

######### To do ###########
#add name
#add security group with ingress rules 
#Add tags