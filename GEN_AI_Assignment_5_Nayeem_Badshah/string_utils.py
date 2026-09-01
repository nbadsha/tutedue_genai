def capitalize_words(input_string):
    return ' '.join(word.capitalize() for word in input_string.split())

def reverse_string(input_string):
    return input_string[::-1]

def word_count(input_string):
    return len(input_string.split())