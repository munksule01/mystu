# S3 BUCKET NAMING

company = "cloudco"
env = "staging"
random_suffix = "x7k"

bucket_name = f"{company}-{env}-bucket-{random_suffix}"

print(f"Generated S3 bucket name: {bucket_name}")