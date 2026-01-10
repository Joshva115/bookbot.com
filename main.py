from stats import get_book_text 

def main():
    wordCount = 0
    wordCount = get_book_text(wordCount)
    print(f"Found {wordCount} total words")
main()