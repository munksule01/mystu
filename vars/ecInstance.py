# EC 2 INSTANCE LAUNCHER

instance_type = "t3.micro"

ami_id = "ami-0c94855ba95c71c99"
instance_count = 3

print(f"Launching {instance_count} {instance_type} instances using AMI ID {ami_id}.")

