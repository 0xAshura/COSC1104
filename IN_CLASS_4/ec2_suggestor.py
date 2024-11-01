# Author: Mihir Limbad and Sahil Koundal 
# Date: 2024-11-01
# Description: The code implements a console-based application in Python that allows users to filter AWS EC2 instances based on their CPU and memory requirements. 
# The program prompts users for their minimum and optional maximum CPU cores and memory, loads instance data from a JSON file, filters the instances based on the provided criteria, and displays the results in a user-friendly format.

import json

def get_integer_input(prompt, optional=False, min_value=None):
    """Prompt for integer input with validation and optional field support."""
    while True:
        user_input = input(prompt).strip()
        if optional and not user_input:
            return None
        try:
            value = int(user_input)
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def load_instance_data(filename):
    """Load and return JSON data from a file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error loading instance data. Check the file and its content.")
        return []

def filter_instances(instances, min_cpu, max_cpu, min_memory, max_memory):
    """Filter instances based on CPU and memory criteria."""
    return [
        instance for instance in instances
        if min_cpu <= instance.get("vCPU", 0) <= (max_cpu or instance["vCPU"])
        and min_memory <= instance.get("MemoryGiB", 0) <= (max_memory or instance["MemoryGiB"])
    ]

def display_instances(instances):
    """Display filtered instances in a readable format."""
    if instances:
        print("\nFiltered EC2 Instances:")
        for instance in instances:
            print(f"Type: {instance['InstanceType']}, vCPU: {instance['vCPU']}, Memory: {instance['MemoryGiB']} GiB")
    else:
        print("No instances match the specified requirements.")

def main():
    # Input requirements
    min_cpu = get_integer_input("Enter minimum CPU cores: ", min_value=1)
    max_cpu = get_integer_input("Enter maximum CPU cores (optional): ", optional=True)
    min_memory = get_integer_input("Enter minimum memory (GiB): ", min_value=1)
    max_memory = get_integer_input("Enter maximum memory (GiB, optional): ", optional=True)

    # Load, filter, and display
    instances = load_instance_data("instances.json")
    filtered_instances = filter_instances(instances, min_cpu, max_cpu, min_memory, max_memory)
    display_instances(filtered_instances)

if __name__ == "__main__":
    main()
