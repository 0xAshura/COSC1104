# Author: Mihir Limbad and Sahil Koundal 
# Date: 2024-11-01
# Description: The code implements a console-based application in Python that allows users to filter AWS EC2 instances based on their CPU and memory requirements. 
# The program prompts users for their minimum and optional maximum CPU cores and memory, loads instance data from a JSON file, filters the instances based on the provided criteria, and displays the results in a user-friendly format.

import json
import re

def get_input(prompt, min_value=None):
    """Get validated integer input from the user."""
    while True:
        try:
            user_input = input(prompt).strip()
            value = int(user_input)
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
            else:
                return value
        except ValueError:
            print("Please enter a valid integer.")

def load_instances(filename):
    """Load instance data from a large JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)

def parse_cpu(cpu_str):
    """Extract the number of CPUs from a string like '16 vCPUs' or '2 vCPUs for a burst'."""
    match = re.search(r'(\d+)', cpu_str)
    return int(match.group(1)) if match else 0

def parse_memory(memory_str):
    """Extract the amount of memory in GiB from a string like '64.0 GiB'."""
    match = re.search(r'(\d+(\.\d+)?)', memory_str)
    return float(match.group(1)) if match else 0

def filter_instances(instances, min_cpu, min_memory):
    """Filter instances based on minimum CPU and memory requirements."""
    filtered = []
    for instance in instances:
        cpu = parse_cpu(instance.get("vcpu", "0 vCPUs"))
        memory = parse_memory(instance.get("memory", "0 GiB"))

        # Only apply minimum filters for CPU and memory
        if cpu >= min_cpu and memory >= min_memory:
            filtered.append(instance)

    return filtered

def main():
    # Get user input for CPU and memory requirements
    min_cpu = get_input("Enter minimum CPU cores: ", min_value=1)
    min_memory = get_input("Enter minimum memory (GiB): ", min_value=1)

    # Load instances from JSON file
    instances = load_instances("instances.json")  # Ensure the filename is correct

    # Filter instances based on user input
    filtered_instances = filter_instances(instances, min_cpu, min_memory)

    # Display filtered results in a readable format
    print("\nFiltered EC2 Instances:")
    for instance in filtered_instances:
        print(f"Type: {instance['name']}, vCPU: {instance['vcpu']}, Memory: {instance['memory']}, "
              f"Storage: {instance['storage']}, Bandwidth: {instance['bandwidth']}, Availability: {instance['availability']}")

if __name__ == "__main__":
    main()
