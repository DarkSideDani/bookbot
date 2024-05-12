# BookBot
---

### Character Frequency Analyzer

This Python script analyzes the frequency of characters in a given text file and generates a report showing the number of words in the document and the count of each alphabetic character in descending order of frequency.

#### Features:
- **Word Count:** Counts the total number of words in the document.
- **Character Frequency:** Analyzes the frequency of each alphabetic character (case-insensitive) and prints the count of each character in descending order.

#### How it Works:
1. **Reading Text:** The script reads the content of a text file specified by the `book_path` variable.
2. **Word Count:** It calculates the number of words in the text using whitespace as the delimiter.
3. **Character Frequency Analysis:** It counts the occurrences of each alphabetic character (case-insensitive) in the text and creates a dictionary mapping each character to its count.
4. **Sorting Characters:** Characters are sorted by frequency in descending order.
5. **Printing Report:** Finally, it prints a report showing the number of words in the document and the count of each alphabetic character.

#### Dependencies:
- This script requires Python 3.x to run.
- It uses only built-in Python modules and does not require any external dependencies.

#### Usage:
1. Set the `book_path` variable to the path of the text file you want to analyze.
2. Run the script.

---
