def extract_username(email):
    # Split the email address at '@'
    parts = email.split('@')

    # Check if the email address has the expected format
    if len(parts) == 2:
        return parts[0]  # The username is the first part
    else:
        return "Invalid email format"


email = input("Enter an email address: ")
username = extract_username(email)
print(username)
