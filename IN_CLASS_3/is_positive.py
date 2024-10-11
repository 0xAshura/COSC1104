# is_positive.py
# Author: Mihir Limbad and Sahil Koundal 
# Date: 2024-10-04
# Description: This function checks if a given number is positive. It returns True if the number is 
# greater than zero, and False otherwise. The function can handle both integer and floating-point numbers.
# It can be used in applications where a decision needs to be made based on whether a number is positive.

def is_positive(number):
    return isinstance(number, (int, float)) and number > 0

if __name__ == "__main__":
    
    print(is_positive(100))      
    print(is_positive(-1))     
    print(is_positive(0))      
    print(is_positive(3.5))    
    print(is_positive(-2.5))   
