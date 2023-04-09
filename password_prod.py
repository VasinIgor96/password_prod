
characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special:
        characters += "._%$/?!"
    
    if not characters:
        print("Error: Unable to create password while all categories = 'No'.")
        continue
    password = ''
    for i in range(length):
        password += random.choice(characters)

    print("Your password: ", password)
    break