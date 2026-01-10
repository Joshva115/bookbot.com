#Need to define the path to the book to open it
def get_book_text():
    with open("./books/frankenstein.txt", 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
        f.closed
def main():
    get_book_text()

main()