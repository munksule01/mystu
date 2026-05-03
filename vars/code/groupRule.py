from_port = 443
to_port = 443
protocol = "tcp"
cidr_block = "10.0.0.0/16"

print(f"Allow {protocol} from {cidr_block} on ports {from_port}-{to_port}")