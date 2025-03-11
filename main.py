#!/usr/bin/python3.10
import sys
from stats import get_num_words
from stats import char_count
from stats import sorted


def get_book_text(filepath):
    with open(filepath,'r') as file:
        content = file.read()

    return content


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]


    content = get_book_text(filepath)
    
    num_words = get_num_words(content)

    print(f"Found {num_words} total words")


    penis = char_count(content)

    print(f"There is this many characters {penis}")


    sorted_counts = sorted(penis)

    # Print the sorted character frequency count
    print("\nSorted Character Frequency Count (from greatest to least):")
    for item in sorted_counts:
        print(f"{item['character']}: {item['count']}")


main()
