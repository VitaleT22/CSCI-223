# Monterey Pheonix Code Completer

**CSCI 223 Semester Project**

An inline code completer for the Monetery Pheonix (MP) behavior modeling language using a **Trie** data structure.

## Project Description

This provides autocomplete suggestions for Monterey Pheonix schemas.
It helps users write MP code faster, and helps in case you get stuck. 

**Time Complexity**
- O(N)

## How It Works

The program uses a **Trie** data structure:
- Each node represents a character
- Words are stored along paths from the root
- Prefix search is fast

You type your word/prefix and hit **enter** when you are ready. It would then output the next **5 suggestions** that are similar to your word/prefix. If the word doesnt already exist in the dictionary then it saves it as a new word. After the **5 suggestions** apear then you **input** the corresponding number **1-5** of the word you wanted or click **enter** if it is not present. Once you are finished typing you can input **exit** and it will end the code there and show you what code you used.

## Setup and Installation

1. Make sure you have Python 3 installed.
2. Place both files ('code_completer.py' and 'MP_wordbank.txt') in the same folder.
3. Run the program