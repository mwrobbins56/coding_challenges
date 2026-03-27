def reverse_string(in_str):
  # Accept a string and return it reversed.
  in_str = input("What would you like to reverse? ")
  print(in_str)
  for_str = " "
  for i in in_str:
    for_str = i + for_str
  return for_str

in_str = " "
reversed_str = reverse_string(in_str)
# Output: revered input
print(reversed_str)
