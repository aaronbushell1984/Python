def name_from_email(email):
    name = ""
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if "@" not in email or "." not in email:
        return "Invalid email"
    else:
        namewithdot = email.split("@")[0]
        name = namewithdot.replace(".", " ")
        for letter in name:
            if letter != name.isdigit():
                name.remove(letter)
        # namenosymbols = ''.join(filter(whitelist.__contains__, name))
        # namenosymbols = ''.join(filter(str.isalpha, name))
        nameupper = name.title()
    return nameupper

email = "john.smith@fdmgroup.com"
print(name_from_email(email))


    
