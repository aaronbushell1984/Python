def is_palindrome(string:str):
    string = string.lower()
    string = string.replace(" ", "")
    string = string.replace("'", "")
    reverse_string = string[::-1]
    if string == reverse_string:
        return True
    else:
        return False


string = "'Madam I'm Adam"
print(is_palindrome(string))