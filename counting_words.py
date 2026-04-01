import string
from collections import Counter

def count_words(filename):
    
    # Read a .txt file and count how many times each word appears.
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return {}

    # Convert all words to lowercase, to treat "This" and "this" as the same
    text = text.lower()

    # Remove punctuation and newlines,  replace with spaces
    for punctuation in string.punctuation + '\n' + '\r':
        text = text.replace(punctuation, ' ')

    # Split the text into a list of words
    words = text.split()

    # Counter returns a dictionary-like object
    word_counts = dict(Counter(words))

    return word_counts

# Call the file name function
file_name = 'sample.txt'
frequency_dict = count_words(file_name)

# Print the results
if frequency_dict:
    print(f"Word frequencies in '{file_name}':")
    print(frequency_dict)
  