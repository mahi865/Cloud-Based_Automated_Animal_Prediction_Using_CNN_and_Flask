# Security Group
resource "aws_security_group" "web_sg" {
  name        = "web-sg"
  description = "Allow access to Flask app"

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Allow traffic from anywhere
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1" # Allow all outbound traffic
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "FlaskAppSecurityGroup"
  }
}

# EC2 Instance
resource "aws_instance" "web" {
  ami           = "ami-0e449927258d45bc4" # Amazon Linux 2 AMI ID (replace with your desired AMI)
  instance_type = "t2.micro"
  security_groups = [
    aws_security_group.web_sg.name
  ]

  tags = {
    Name = "FlaskAppInstance"
  }

  # User data for initialization (e.g., to install Docker and start the app)
  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo amazon-linux-extras enable docker
              sudo yum install -y docker
              sudo service docker start
              sudo usermod -a -G docker ec2-user
              docker pull your-dockerhub-username/flask-app:latest
              docker run -d -p 5000:5000 your-dockerhub-username/flask-app:latest
              EOF
}

# Elastic IP
resource "aws_eip" "web_eip" {
  domain = "vpc"

  tags = {
    Name = "FlaskAppEIP"
  }
}

# Associate Elastic IP with the EC2 instance
resource "aws_eip_association" "web_eip_assoc" {
  instance_id   = aws_instance.web.id
  allocation_id = aws_eip.web_eip.id
}