
# 📚 BookBot - Character & Word Analyzer

BookBot is a simple Python script that analyzes a given text file (like a book) to count the total number of words and the frequency of each alphabetical character (case-insensitive).

---

## 🚀 Features

- Counts the total number of words in the text.
- Tallies how often each alphabetical character (a–z) appears, ignoring punctuation, numbers, and case.
- Displays characters in order of most to least frequent.

---

## 🛠️ How It Works

1. The script reads in the text file you specify.
2. It splits the text into words and counts them.
3. It loops through every character in the text, counts only alphabetical characters (ignoring case), and tallies how often each appears.
4. The results are printed to the console in descending order by frequency.

---

## 🧪 Example Output

```bash
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt
----------- Word Count ----------
Found 74312 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
...
```

---

## 📦 How to Use

### 1. Clone the Repository or Download the Files

```bash
git clone https://github.com/DarkSideDani/bookbot.git
cd bookbot
```

### 2. Add a Text File

Place your `.txt` file inside the project folder (e.g. `books/frankenstein.txt`).

### 3. Run the Script

```bash
python3 main.py books/frankenstein.txt
```

If you don't provide a file path, you'll see a usage message:

```bash
Usage: python3 main.py <path_to_book>
```

---

## 📁 Project Structure

```bash
bookbot/
│
├── main.py             # Main program logic and CLI handling
├── stats.py            # Word and character counting functions
├── books/              # (optional) Folder to store your .txt files
│   └── frankenstein.txt
└── README.md           # This file
```

---

## 📌 Requirements

- Python 3.x
- A plain `.txt` file to analyze

---



BookBot is my first [Boot.dev](https://www.boot.dev) project!
