# is_power_of_two.py
# Author: Mihir Limbad and Sahil Koundal 
# Date: 2024-10-04
# Description: This function checks if a given integer is a power of 2. It uses bitwise operations 
# to efficiently determine whether the number is a power of 2. This can be useful in scenarios like 
# optimizing resources in systems or verifying conditions in algorithms where powers of 2 are important.


def is_power_of_two(number):
    """Return True if the number is a power of 2, False otherwise."""
    if number < 1:
        return False
    return (number & (number - 1)) == 0

if __name__ == "__main__":
   
    print(is_power_of_two(32))    
    print(is_power_of_two(64))    
    print(is_power_of_two(128))   
    print(is_power_of_two(265))    
    print(is_power_of_two(2048))    
