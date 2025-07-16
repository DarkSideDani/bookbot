def count_words(text):
    words = text.split()
    return len(words)

def char_counter(text):
    char_counts = {}
    for char in text.lower():
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def sorted_counts(char_counts):
    sorted_chars = sorted(
        char_counts.items(), # returns list of (char, count) tuples.
        key=lambda pair: pair[1], # sorts those tuples by the count (the value at index 1), so it tells sorted() to sort by the count and not by the letter
        reverse=True) # start with the biggest count first
    for char, count in sorted_chars:
        print(f"{char}: {count}")
