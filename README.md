# BookBot: Text Analysis Tool

## Overview

**BookBot** is a Python tool designed to analyze the content of a book or any text file. It provides a detailed statistical report on the number of words and the frequency of each character (case-insensitive) in the text. This project is suitable for anyone needing to quickly gain insights into the textual content of their documents.

## Features

- Counts the total number of words in the text.
- Calculates the frequency of each alphabetic character, ignoring case.
- Generates a clear and sorted report of character frequencies.
- Can be used as a standalone script or imported as a module for integration into other Python projects.
- Includes error handling for common issues like missing or empty files.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/DarkSideDani/bookbot
   cd bookbot
   ```

2. **Ensure Python is Installed**:
   Make sure you have Python 3.x installed on your machine.

## Usage

### As a Standalone Script

1. Save your text file (e.g., `frankenstein.txt`) in the `books` directory, or specify a path to your file.

2. Run the script from the command line:

   ```bash
   python book_analyzer.py books/frankenstein.txt
   ```

   Replace `books/frankenstein.txt` with the path to your text file.

3. **Command-line Options**:
   You can get help on how to use the script by running:

   ```bash
   python book_analyzer.py -h
   ```

   This will display the help message:

   ```
   usage: book_analyzer.py [-h] book_path
   
   Analyze a book and print a statistical report.
   
   positional arguments:
     book_path  Path to the book file
   
   optional arguments:
     -h, --help  show this help message and exit
   ```

### As a Module

You can import the functions into your own Python scripts for further use:

```python
from book_analyzer import get_num_words, get_num_chars

text = "Your text here"
print(get_num_words(text))
print(get_num_chars(text))
```

## Functions

### `get_book_text(path)`

- **Description**: Reads the content of a book from the specified file path.
- **Parameters**: `path` (str) - Path to the text file.
- **Returns**: String containing the text from the file.
- **Error Handling**: Raises `FileNotFoundError` if the file does not exist or `ValueError` if the file is empty.

### `get_num_words(text)`

- **Description**: Counts the number of words in the given text.
- **Parameters**: `text` (str) - Text to analyze.
- **Returns**: Integer representing the number of words.

### `get_num_chars(text)`

- **Description**: Counts the occurrences of each alphabetic character in the given text (case-insensitive).
- **Parameters**: `text` (str) - Text to analyze.
- **Returns**: Dictionary with characters as keys and their frequencies as values.

### `generate_report(book_path)`

- **Description**: Generates and prints a statistical report of the text file located at `book_path`.
- **Parameters**: `book_path` (str) - Path to the text file.
- **Error Handling**: Ensures the file is read correctly and outputs a report of the analysis.

### `main()`

- **Description**: Handles command-line interface for the script. Parses arguments and generates the report.

## Example Output

When running the script with a sample text file, you might see:

```
--- Begin report of books/frankenstein.txt ---
1234 words found in the document

The 'a' character was found: 5423 times
The 'b' character was found: 2341 times
The 'c' character was found: 1234 times
...
--- End Report ---
```

## Acknowledgments

This project was inspired by the [Boot.dev](https://www.boot.dev/tracks/backend) course project, to perform simple text analysis and generate meaningful insights from written content/books.