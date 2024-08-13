def main():
    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_num_chars(text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    
    for char in sorted(char_count.keys()): # Sort the characters alphabetically and print their counts
        print(f"The '{char}' character was found: {char_count[char]} times")
        
    print("--- End Report ---")
        
def get_num_words(text):
    words = text.split()
    return len(words)        
        
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_chars(text):
    char_count = {}
    
    for char in text:
        char = char.lower()
        if char.isalpha(): # making sure that it's checking with characters from the alphabet
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

main()