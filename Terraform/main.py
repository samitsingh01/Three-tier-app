resource "aws_instance" "web" {
  ami           = "ami-04f59c565deeb2199"
  instance_type = "t2.large"
  key_name      = "samitnv"
  # No security group specified = uses default
  user_data = file("${path.module}/setup_k8s.sh")
  tags = {
    Name = "Samit_Instance"
  }
}

provider "aws" {
  region = "us-east-1"
  shared_credentials_files = ["~/.aws/credentials"]
  # private_key_path = "~/vilas.pem"
}
