#This function will open the book and count how many words there found within the book.
def get_book_text():
    with open("./books/frankenstein.txt", 'r', encoding='utf-8') as f:
        content = f.read()
        wordSplitted = content.split()
        wordCount = 0
        for word in wordSplitted:
            wordCount +=1
        f.closed
        print(f"Found {wordCount} total words")
def main():
    get_book_text()

main()