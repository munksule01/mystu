# Cost Estimator

hourly_rate = float(input("Enter the hourly rate for the VM (USD): "))
uptime_hours = int(input("Enter uptime hours for the VM: ")) # 1 Month

monthly_cost = (hourly_rate * uptime_hours)

print(f"Monthly cost for 1 VM: ${monthly_cost:.2f}")