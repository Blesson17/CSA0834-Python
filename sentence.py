import re

# Function to find sentences that start with 'B'
def find_sentences_starting_with_b(text):
    # Split the text into sentences using a regular expression
    sentences = re.split(r'(?<=[.!?]) +', text)
    # Filter and return sentences that start with 'B' or 'b'
    return [sentence for sentence in sentences if sentence.strip().startswith(('B', 'b'))]

# Example usage
text = "Better late than never. Apple is a fruit. Be brave. Many people are kind."
sentences_starting_with_b = find_sentences_starting_with_b(text)
print("Sentences starting with 'B' or 'b':")
for sentence in sentences_starting_with_b:
    print(sentence)
