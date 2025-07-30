from stats import count_number_of_words, character_count, report_func
import sys

def main():
    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        
        book_path = sys.argv[1]
        #book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        num_words = count_number_of_words(text)
        character_total = character_count(text)
        report = report_func(character_total)
        print (f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...")
        print (f"----------- Word Count ----------\nFound {num_words} total words")
        print ("--------- Character Count -------")
        for item in (report):
            print(f"{item["char"]}: {item["num"]}")
        print("============= END ===============")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()