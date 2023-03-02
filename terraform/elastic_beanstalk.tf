### Elastic bean stalk does not make it easy to deploy to already created enviroment 
##  you have to deplot from the enviroment you created from

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
