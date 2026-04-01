# Find the largest number in a list.
# I tried to set this up to input the lists, but it was too complicated.
# It would have required a block of code just to build the list by typing it in. 

def find_max(numbers):
    # Return None for an empty list
    if not numbers:
        return None  
    
    # Initialize working variable to the first number in the list
    found_max = numbers[0]

    # Process through the remaining numbers of the list
    for number in numbers[1:]:
        # If next number is larger than the found_max, update found_max
        if number > found_max:
            found_max = number

    return found_max

# integers 
integer_list = [10, 4, 78, 22, 5, 90, 1]
largest_int = find_max(integer_list)
print(f"The largest integer in {integer_list} is: {largest_int}")

# floats
float_list = [3.14, 1.0, 5.5, 0.99, 2.71]
largest_float = find_max(float_list)
print(f"The largest float in {float_list} is: {largest_float}")

# integers and floats
mixed_list = [5, 10.5, 2, 20.1, 8]
largest_mixed = find_max(mixed_list)
print(f"The largest number in {mixed_list} is: {largest_mixed}")

# empty list
empty_list = []
largest_empty = find_max(empty_list)
print(f"The largest number in {empty_list} is: {largest_empty}")
