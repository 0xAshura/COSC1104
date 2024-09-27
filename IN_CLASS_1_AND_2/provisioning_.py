# provisioning.py

# Cloud resource provisioning simulation
# Authors: Mihir Limbad and Sahil Koundal
# Date: 2024-09-27
# Description: Simulates a cloud resource provisioning system based on available CPU cores and memory.

# Constants (total available resources)
TOTAL_CPU_CORES = 32
TOTAL_MEMORY_GB = 480

def get_valid_cpu_cores():
    while True:
        try:
            cpu_cores = int(input("Enter the number of required CPU cores: "))
            if cpu_cores < 0:
                raise ValueError("CPU cores cannot be negative.")
            return cpu_cores
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a non-negative integer.")

def get_valid_memory_gb():
    while True:
        try:
            memory_gb = float(input("Enter the amount of required memory (in GB): "))
            if memory_gb < 0:
                raise ValueError("Memory cannot be negative.")
            return memory_gb
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a non-negative float.")

# Input from user with validation
required_cpu_cores = get_valid_cpu_cores()
required_memory_gb = get_valid_memory_gb()

# Check if resources are available
if required_cpu_cores <= TOTAL_CPU_CORES and required_memory_gb <= TOTAL_MEMORY_GB:
    print("Resources provisioned successfully.")
    # Update available resources
    TOTAL_CPU_CORES -= required_cpu_cores
    TOTAL_MEMORY_GB -= required_memory_gb
else:
    print("Resource request exceeds capacity. Provisioning failed.")

# Display remaining available resources
print(f"Remaining CPU cores: {TOTAL_CPU_CORES}")
print(f"Remaining memory (GB): {TOTAL_MEMORY_GB:.2f}")
