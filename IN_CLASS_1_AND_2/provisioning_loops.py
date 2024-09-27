#provisioning_loops.py
#Cloud resource provisioning simulation
#Author:Mihir Limbad and Shil Koundal
#Date: 2024-09-27
#Description: This Python script simulates a cloud resource provisioning system with multiple requests.It checks whether the requested CPU cores and memory can be provisioned based on the available resources,stores allocated resources, and logs pending requests when resources are unavailable.

# Constants for total available resources
TOTAL_CPU_CORES = 32  # Total number of CPU cores available
TOTAL_MEMORY_GB = 480  # Total amount of memory in gigabytes (GB) available

# Lists for allocated resources and pending requests
allocated_resources = []
pending_requests = []

# Track remaining resources
remaining_cpu_cores = TOTAL_CPU_CORES
remaining_memory_gb = TOTAL_MEMORY_GB

# Start the loop to process multiple requests
while True:
    # Request user input
    username = input("Enter your username: ")
    try:
        required_cpu_cores = int(input("Enter the number of required CPU cores (whole number): "))
        required_memory_gb = float(input("Enter the amount of required memory in GB (float): "))

        # Input validation for negative values
        if required_cpu_cores < 0 or required_memory_gb < 0:
            print("Invalid input: Values cannot be negative.")
            continue

        # Check if requested resources are available
        if required_cpu_cores <= remaining_cpu_cores and required_memory_gb <= remaining_memory_gb:
            # Resources available, allocate them
            allocated_resources.append([username, required_cpu_cores, required_memory_gb])
            remaining_cpu_cores -= required_cpu_cores
            remaining_memory_gb -= required_memory_gb
            print("Resources provisioned successfully.")
        else:
            # Resources not available, add to pending requests
            pending_requests.append([username, required_cpu_cores, required_memory_gb])
            print("Resource request exceeds capacity. Added to pending requests.")

        # Ask if the user wants to make another request
        another_request = input("Do you want to make another request? (yes/no): ").strip().lower()
        if another_request != 'yes':
            break

    except ValueError:
        print("Invalid input: Please enter a whole number for CPU cores and a float for memory.")

# Display the final lists in table-like format
print("\n--- Allocated Resources ---")
print(f"{'Username':<15}{'CPU Cores':<10}{'Memory (GB)':<10}")
for resource in allocated_resources:
    print(f"{resource[0]:<15}{resource[1]:<10}{resource[2]:<10}")

print("\n--- Pending Requests ---")
if pending_requests:
    print(f"{'Username':<15}{'CPU Cores':<10}{'Memory (GB)':<10}")
    for request in pending_requests:
        print(f"{request[0]:<15}{request[1]:<10}{request[2]:<10}")
else:
    print("No pending requests.")
