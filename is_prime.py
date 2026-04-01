# Check whether a number is prime
import math

# What number?
in_nbr = int(input("What number do you want to check if it is prime: "))

def is_prime(number):
    
    if number <= 1:
        return False  # 0, 1, and negative numbers are not prime.
    if number == 2:
        return True   # 2 is the only even prime number.
    if number % 2 == 0:
        return False  # even numbers - not prime.

    # Check for odd divisors starting at 3
    # Skip even numbers because handled the case for 2.
    limit = int(math.sqrt(number)) + 1
    for i in range(3, limit, 2):
        if number % i == 0:
            return False  # Found a divisor - not prime.

    return True # No divisors found - prime.

# Display if number is prime or no ->
print(f"Is {in_nbr} prime? {is_prime(in_nbr)}")

# print(f"Is 10 prime? {is_prime(10)}")
# print(f"Is 29 prime? {is_prime(29)}")
# print(f"Is 1 prime? {is_prime(1)}")