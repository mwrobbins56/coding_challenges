def caesar_cipher(text_and_shift):

   # Use a Caesar cipher on a string, to shift only alphabetical characters.

    text, shift = text_and_shift
    result = ""

    # Ensure shift is within the range of the alphabet (26 letters)
    shift = shift % 26

    for char in text:
        if 'a' <= char <= 'z':
            # Handle lowercase letters
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            result += shifted_char
        elif 'A' <= char <= 'Z':
            # Handle uppercase letters
            shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            result += shifted_char
        else:
            # Handle non-alphabetical characters (punctuation, spaces, numbers)
            result += char
            
    return result

# The Caessar Cipher inputs

caesar_tuple = ("Hello World!", 4)
encrypted_text = caesar_cipher(caesar_tuple)
print(f"Original: {caesar_tuple[0]}")
print(f"Shift: {caesar_tuple[1]}")
print(f"Encrypted: {encrypted_text}")

# Example with a large shift value and numbers/punctuation:
caesar_tuple_2 = ("West 22nd Street!", 29)
encrypted_text_2 = caesar_cipher(caesar_tuple_2)
print(f"\nOriginal: {caesar_tuple_2[0]}")
print(f"Shift: {caesar_tuple_2[1]}")
print(f"Encrypted: {encrypted_text_2}")
