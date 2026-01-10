from stats import get_book_text, get_word_count, word_to_lower_case, adding_words_to_dict

def main():
    wordSplit = ""
    wordCount = 0
    wordDict = {}
    wordSplit = get_book_text(wordSplit)
    wordCount = get_word_count(wordSplit,wordCount)
    print(f"Found {wordCount} total words")
    wordSplit = word_to_lower_case(wordSplit)
    wordDict = adding_words_to_dict(wordSplit,wordDict)
    print(wordDict)





main()