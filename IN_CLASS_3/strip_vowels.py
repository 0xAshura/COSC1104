# strip_vowels.py
# Author: Mihir Limbad and Sahil Koundal 
# Date: 2024-10-04
# Description: This function takes a string as input and removes all vowels (a, e, i, o, u) from it, 
# returning the modified string without vowels. It processes both uppercase and lowercase vowels. 
# The function is useful for processing strings where vowels need to be excluded, 
# such as creating consonant-only versions of text for specific applications.


def strip_vowels(text):
    """Remove all vowels from the given string."""
    vowels = "aeiouAEIOU"
    return ''.join([char for char in text if char not in vowels])


