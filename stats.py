#This function will open a book and count the amount of words that appear in the book
def get_book_text(wordCount):
    with open("./books/frankenstein.txt", 'r', encoding='utf-8') as f:
        content = f.read()
        wordSplitted = content.split()
    for word in wordSplitted:
        wordCount +=1
    return wordCount