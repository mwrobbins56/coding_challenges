# Generate Fizz /3 Buzz/5 Bang/7 and FizzBuzz if / by multiple
# Initialize fizzbuzzbang output variable, scan thru 1 - 100
fizz_buzz_bang = ""
for nums in range(1, 101):
    if nums % 3 == 0 and nums % 5 == 0:
        fizz_buzz_bang = "FizzBuzz35"
    elif nums % 3 == 0 and nums % 7 == 0:
        fizz_buzz_bang = "FizzBuzz37"
    elif nums % 5 == 0 and nums % 7 == 0:
        fizz_buzz_bang = "FizzBuzz57"
    elif nums % 3 == 0:
        fizz_buzz_bang = "Fizz"
    elif nums % 5 == 0:
        fizz_buzz_bang = "Buzz"
    elif nums % 7 == 0:
        fizz_buzz_bang = "Bang"
    else:
        fizz_buzz_bang = "None"
    # Print out FizzBuzzBang and current number 1-101
    fbb_entry = (f"{fizz_buzz_bang}, {nums}\n")
    print(fbb_entry)
    try:
        with open("fizz.txt", "a") as fizz_file:
            fizz_file.write(fbb_entry)
        print(f"Logged: {fbb_entry}")
    except IOError as e:
            print(f"Error writing to file: {e}")
