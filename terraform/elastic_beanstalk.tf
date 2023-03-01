resource "aws_elastic_beanstalk_application" "application" {
  name = "GreenGiants"
}

resource "aws_elastic_beanstalk_environment" "environment" {
  name                = "GreenGiants"
  application         = aws_elastic_beanstalk_application.application.name
  solution_stack_name = "64bit Amazon Linux 2 v3.4.4 running Python 3.8"
  setting {
    namespace = "aws:autoscaling:launchconfiguration"
    name      = "IamInstanceProfile"
    value     = "aws-elasticbeanstalk-ec2-role"
  }
}
