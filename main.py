import argparse

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    char_count = {}
    
    for char in text:
        char = char.lower()
        if char.isalpha():  # only count alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def generate_report(book_path):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_num_chars(text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    
    for char in sorted(char_count.keys()):  # Sort characters alphabetically
        print(f"The '{char}' character was found: {char_count[char]} times")
        
    print("--- End Report ---")

def main():
    """Main function to handle command-line interface."""
    parser = argparse.ArgumentParser(description="Analyze a book and print a statistical report.")
    parser.add_argument('book_path', type=str, help='Path to the book file')
    
    args = parser.parse_args()
    generate_report(args.book_path)

if __name__ == "__main__":
    main()
