def findDuplicates(string):
    duplicates = []
    for character in string:
        if string.count(character) > 1:
            if character not in duplicates:
                duplicates.append(character)
    return len(duplicates)

