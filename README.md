# BookBot: Character Frequency Analysis

BookBot is a Python program that analyzes an entire book and generates a detailed statistical report on the frequency of each character found in the text. It's designed to help you gain insights into the text by examining character usage.

## Project Overview

This project reads the content of a book, counts the number of words, and calculates the frequency of each alphabetic character (case-insensitive). The characters are then sorted alphabetically, and the report is printed in a clean, readable format.

### Features

- **Word Count**: Calculates the total number of words in the book.
- **Character Frequency Analysis**: Counts how many times each alphabetic character appears in the text, regardless of case.
- **Alphabetical Sorting**: The characters are listed in alphabetical order in the report.
- **Simple and Clean Output**: The report is presented in a structured and easy-to-read format.

## How to Use

### Prerequisites

- Python 3.x installed on your system.
- A text file of the book you want to analyze. The example included is **Frankenstein**.

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/DarkSideDani/bookbot
    cd bookbot
    ```

2. **Place your text file**:
   - Ensure the text file of the book is placed in the `books` directory within the project folder.
   - The default example uses `frankenstein.txt`. To analyze a different book, replace this file or update the file path in the code.

3. **Run the program**:
    ```bash
    python main.py
    ```

### Example Output

When you run the program, it generates a report similar to this:

```
--- Begin report of books/frankenstein.txt ---
74347 words found in the document

The 'a' character was found: 4456 times
The 'b' character was found: 1398 times
The 'c' character was found: 2521 times
...
The 'y' character was found: 2437 times
The 'z' character was found: 249 times
--- End Report ---
```

### Customization

- **Analyzing a Different Book**: To analyze a different book, change the `book_path` variable in the `main()` function to point to the desired text file.
- **Output Formatting**: Modify the output format in the `main()` function to suit your preferences.


## Acknowledgments

This project was inspired by the [Boot.dev](https://www.boot.dev/tracks/backend) course project, to perform simple text analysis and generate meaningful insights from written content/books.
