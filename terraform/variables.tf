# variables.tf

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
  default     = "ami-0c55b159cbfafe1f0" # Replace with a valid AMI ID
}

variable "key_name" {
  description = "The name of the SSH key pair"
  default     = "my-key-pair"
}