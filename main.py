from stats import get_book_text
from stats import get_num_words
from stats import get_num_chars
from stats import sort_dictionary
import sys


    
def main():
    if len(sys.argv) != 2:
        print("To use this program you must provide the command:")
        print("Usage: python3 main.py <path_to_book>")
        print("Please try again")
        sys.exit(1)
    book_location = f"{sys.argv[1]}"
    book_text = get_book_text(book_location)
    unordered_numbers = get_num_chars(book_text)
    sorted_results = sort_dictionary(unordered_numbers)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    for i in sorted_results:
        print(f"{i["letter"]}: {i["count"]}")
    
main()