# Checks if string is a palindrome using re module.
import re

in_str = input("What word do you want to be checked for being a paindrome? ")

def is_palindrome(in_str: str) -> bool:
 
    # Uses re to only check letters and numbers, plus convert to lowercase
    re_in_str = re.sub(r'[^A-Za-z0-9]', '', in_str).lower()
       
    # Compare re string to its input string
    return re_in_str == re_in_str[::-1]
    
# Display result of check
if is_palindrome:
    print(f"Yes, {in_str} is a palindrome.") 
else:
    print(f"No, {in_str} is not a palindrome.")