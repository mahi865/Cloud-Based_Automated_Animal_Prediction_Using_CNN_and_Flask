resource "aws_security_group" "web_sg" {
  name        = "web-sg"
  description = "Allow access to Flask app"

  # Inbound rules (allow traffic to port 5000)
  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Allow traffic from anywhere
  }

  # Outbound rules (allow all outbound traffic)
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1" # Allow all protocols
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "FlaskAppSecurityGroup"
  }
}