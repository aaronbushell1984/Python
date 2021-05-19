def case_count(string:str):
    uppercase = 0
    lowercase = 0
    for character in string:
        if character.isupper():
            uppercase += 1
        if character.islower():
            lowercase += 1
    return "No. of Upper case characters : " + str(uppercase) + "\nNo. of Lower case Characters : " + str(lowercase)

string = "The quick Brow Fox"
print(case_count(string))