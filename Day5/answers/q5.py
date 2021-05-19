def name_from_email(email):
    if '@' not in email or '.' not in email:
        return "Invalid email"
    # Remove digits
    email = ''.join([i for i in email if not i.isdigit()])
    # Strip everything from the @ onwards
    email = email[:email.find("@")]
    # Replace '.' with a space and convert to title case
    name = email.replace("."," ").title()
    
    return name
