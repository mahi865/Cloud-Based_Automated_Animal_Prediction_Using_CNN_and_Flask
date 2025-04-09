# outputs.tf

output "instance_public_ip" {
  description = "The public IP address of the instance"
  value       = aws_instance.example.public_ip
}