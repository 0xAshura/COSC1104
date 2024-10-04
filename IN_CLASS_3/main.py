# main.py
# Author: Mihir Limbad and Sahil Koundal 
# Date: 2024-10-04
# Description: This script imports and tests the functions strip_vowels, is_positive, 
# and is_power_of_two with various test cases.

# Importing the functions from their respective files
from strip_vowels import strip_vowels
from is_power_of_two import is_power_of_two
from is_positive import is_positive

if __name__ == "__main__":
    print(strip_vowels("Hello World"))  
    print(strip_vowels("Drham College!"))  
    print(strip_vowels("CANADA is AWSOME BRO "))  
    print(is_power_of_two(265))    
    print(is_power_of_two(2048))  
    print(is_power_of_two(4096)) 
    print(is_positive(-1))     
    print(is_positive(0))      
    print(is_positive(3.5))

