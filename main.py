from stats import get_book_text, get_word_count, word_to_lower_case, adding_words_to_dict, reporting

def main():
    wordSplit = ""
    wordCount = 0
    wordDict = {}
    wordSplit = get_book_text(wordSplit)
    wordCount = get_word_count(wordSplit,wordCount)
    wordSplit = word_to_lower_case(wordSplit)
    wordDict = adding_words_to_dict(wordSplit,wordDict)
    reporting(wordDict,wordCount)




main()