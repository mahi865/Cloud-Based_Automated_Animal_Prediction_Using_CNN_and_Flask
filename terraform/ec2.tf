# Allocate an Elastic IP
resource "aws_eip" "web_eip" {
  vpc = true
}

# EC2 Instance
resource "aws_instance" "web" {
  ami           = "ami-0e449927258d45bc4" # Amazon Linux 2 AMI
  instance_type = "t2.micro"

  # User data script to install Docker and run the container
  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y docker
              service docker start
              usermod -a -G docker ec2-user
              docker run -d -p 80:5000 your-dockerhub-username/flask-app:latest
              EOF

  tags = {
    Name = "FlaskAppInstance"
  }
}

# Associate Elastic IP with the Instance
resource "aws_eip_association" "web_eip_assoc" {
  instance_id   = aws_instance.web.id
  allocation_id = aws_eip.web_eip.id
}