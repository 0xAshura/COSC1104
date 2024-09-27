# Cloud Resource Provisioning Simulation

## Authors
- Mihir Limbad
- Sahil Koundal

## Description
This project simulates a cloud resource provisioning system. It includes two Python scripts:

1. **provisioning.py**: A simple script that allows a user to request cloud resources (CPU cores and memory). The program checks if the requested resources are available based on predefined limits.

2. **provisioning_loops.py**: An extended version of the first script, which allows users to make multiple requests. It tracks allocated resources and pending requests, ensuring efficient management of cloud resources.

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Running the Scripts

1. **provisioning.py**:
   - Run the script using the command:
     ```bash
     python provisioning.py
     ```
   - Follow the prompts to enter the required CPU cores and memory. The script will inform you whether the resources were provisioned successfully or if the request exceeded capacity.

2. **provisioning_loops.py**:
   - Run the script using the command:
     ```bash
     python provisioning_loops.py
     ```
   - You will be prompted to enter a username along with the number of CPU cores and memory required. The program will continue to accept requests until you choose to stop. At the end, it will display a summary of allocated resources and any pending requests.

## Features
- Input validation to ensure non-negative values are entered for CPU cores and memory.
- The second script incorporates loops to handle multiple user requests.
- Keeps track of allocated resources and pending requests in a user-friendly manner.

## Example Usage
### provisioning.py
