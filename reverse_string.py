def reverse_string(in_str):
  # Accept a string and return it reversed.
  in_str = input("What would you like to reverse? ")
  return in_str[::-1]

in_str = " "
reversed_str = reverse_string(in_str)
# Output: revered input
print(reversed_str)
