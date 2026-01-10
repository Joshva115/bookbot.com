#This function will open a book and
def get_book_text(wordSplit):
    with open("./books/frankenstein.txt", 'r', encoding='utf-8') as f:
        content = f.read()
        wordSplit = content.split()
        return wordSplit

#This function returns the wordCount in the entire book that was parsed in.
def get_word_count(wordSplit,wordCount):
    for word in wordSplit:
        wordCount +=1
    return wordCount

#Function iterates through the entire list and returns each value lower cased
def word_to_lower_case(wordSplit):
    lowered_list = [word.lower() for word in wordSplit]
    return lowered_list

#Function iterates through list and will add to the dictionary the count of each character.
def adding_words_to_dict(wordSplit,wordDict):
    for word in wordSplit:
        for j in word:
            if j not in wordDict:
                wordDict[j] = 1
            else:
                wordDict[j] +=1
    return wordDict