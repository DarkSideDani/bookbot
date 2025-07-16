import sys

from stats import count_words, char_counter, sorted_counts

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    word_count = count_words(text)
    char_counts = char_counter(text)
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    sorted_counts(char_counts)


if __name__ == "__main__":
    main()