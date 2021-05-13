def countWords(stringOfWords):
    stringOfWords = stringOfWords.lower()
    words = stringOfWords.split()
    wordsEndROrS = 0
    for word in words:
        if word.endswith("r") or word.endswith("s"):
            wordsEndROrS = wordsEndROrS + 1
    return wordsEndROrS              