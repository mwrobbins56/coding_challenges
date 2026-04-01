# Is your password is strong or not. 
def print_strong_pswd(input_string):
    
    n = len(input_string) 

    # Checking for lowercase, uppercase, numbers, special characters 
    lower_case = False
    upper_case = False
    nums_09 = False
    spec_chars = False
    norm_chars = "abcdefghijklmnopqrstu"
    "vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
    
    for i in range(n):
        if input_string[i].islower():
            lower_case = True
        if input_string[i].isupper():
            upper_case = True
        if input_string[i].isdigit():
            nums_09 = True
        if input_string[i] not in norm_chars:
            spec_chars = True

    # Is the password strong, moderate, or weak
    print("Strength of password: ", end = "")
    if (lower_case and upper_case and 
        nums_09 and spec_chars and n >= 8):
        print("Strong")    
    elif ((lower_case or upper_case) and 
          spec_chars and n >= 6):
        print("Moderate")
    else:
        print("Weak")

# Driver code 
if __name__=="__main__": 
    # Input the password to be checked
    input_string = input("Enter your password: ")
   
    print_strong_pswd(input_string)
