import argparse
import os

def get_book_text(path):
    if not os.path.isfile(path):
        raise FileNotFoundError(f"The file '{path}' does not exist.")
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
            if not text.strip():
                raise ValueError("The file is empty or only contains whitespace.")
            return text
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{path}' was not found.")
    except IOError as e:
        raise IOError(f"An IO error occurred while trying to read the file '{path}': {e}")
    except ValueError as ve:
        raise ValueError(f"Error reading file: {ve}")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char.isalpha():  # Only count alphabetic characters
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

def generate_report(book_path):
    try:
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        char_count = get_num_chars(text)
        
        print(f"--- Begin report of {book_path} ---")
        print(f"{num_words} words found in the document\n")
        
        for char in sorted(char_count.keys()):  # Sort characters alphabetically
            print(f"The '{char}' character was found: {char_count[char]} times")
            
        print("--- End Report ---")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main function to handle command-line interface."""
    parser = argparse.ArgumentParser(description="Analyze a book and print a statistical report.")
    parser.add_argument('book_path', type=str, help='Path to the book file')
    
    args = parser.parse_args()
    generate_report(args.book_path)

if __name__ == "__main__":
    main()
