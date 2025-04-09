# main.tf

# Define the provider
provider "aws" {
  region = var.aws_region
}

# Define the variables
variable "aws_region" {
  description = "The AWS region to deploy in"
  default     = "us-west-2"
}

variable "instance_type" {
  description = "The type of instance to create"
  default     = "t2.micro"
}

variable "ami_id" {
  description = "The AMI ID to use for the instance"
  default     = "ami-0c55b159cbfafe1f0" # This is an example AMI ID, replace with a valid one
}

variable "key_name" {
  description = "The name of the SSH key pair"
  default     = "my-key-pair"
}

# Create the EC2 instance
resource "aws_instance" "example" {
  ami           = var.ami_id
  instance_type = var.instance_type
  key_name      = var.key_name

  tags = {
    Name = "ExampleInstance"
  }
}

# Output the instance's public IP
output "instance_public_ip" {
  description = "The public IP address of the instance"
  value       = aws_instance.example.public_ip
}