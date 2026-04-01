import re

def pswd_checker():
    password = input("Enter a password: ")

    if len(password) < 8:
        print("Too weak: password must be at least 8 characterss long.")
        return
    elif not re.search("[a-z]", password):
        print("Too weak: password must contain at least one lowercase letter.")
        return
    elif not re.search("[A-Z]", password):
        print("Too weak: password must contain at least one uppercase letter.")
        return
    elif not re.search("[0-9]", password):
        print("Too weak: password must contain at least one number.")
        return
    elif not re.search("[!@#$%^&*?|<>]"):
        print("Too weak: password must contain at least one special character.")
        return
    else:
        print("Your password is strong!")

pswd_checker()
