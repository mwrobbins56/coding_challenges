# Check input string to see if it is a palindrome
in_str = input("What word do you want to be checked for being a paindrome? ")

# Initialize variables.
f, b = 0, len(in_str) - 1  
is_palindrome = True  

# Compares both ends going toward middle of the input string
while f < b:
    if in_str[f] != in_str[b]:  
        is_palindrome = False
        break
    f += 1
    b -= 1

# Display result of check
if is_palindrome:
    print(f"Yes {in_str} is a palindrome.") 
else:
    print(f"No, {in_str} is not a palindrome.")