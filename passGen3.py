import random
import string

def generate_password(min_length, max_length, use_special_chars, special_chars_list, use_numbers,
                      allow_capital_letters, no_consecutive_repeats, ensure_one_of_each):
    # Start with lowercase letters
    characters = string.ascii_lowercase
    
    if allow_capital_letters:
        characters += string.ascii_uppercase  # Add uppercase letters if allowed
    
    if use_numbers:
        characters += string.digits  # Add digits to the character set
    
    if use_special_chars:
        characters += special_chars_list  # Use only specified special characters

    length = random.randint(min_length, max_length)  # Randomly choose a length within the specified range
    password = []

    # Ensure at least one of each selected type is included
    if ensure_one_of_each:
        if allow_capital_letters:
            password.append(random.choice(string.ascii_uppercase))
        if use_numbers:
            password.append(random.choice(string.digits))
        if use_special_chars:
            password.append(random.choice(special_chars_list))

    while len(password) < length:
        char = random.choice(characters)
        
        # Check for consecutive repeats if not allowed
        if no_consecutive_repeats and password and char == password[-1]:
            continue
        
        password.append(char)

    random.shuffle(password)  # Shuffle to mix ensured elements with others
    return ''.join(password[:length])

def main():
    try:
        # Prompt user for input
        min_length = int(input("Enter the minimum desired password length: "))
        max_length = int(input("Enter the maximum desired password length: "))
        
        include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
        
        special_chars_list = ''
        if include_special_chars:
            special_chars_list = input("Enter the list of allowed special characters: ")
        
        include_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        allow_capital_letters = input("Enable capital letters? (yes/no): ").strip().lower() == 'yes'
        
        ensure_one_of_each = input("Make at least one of each additional selection? (yes/no): ").strip().lower() == 'yes'
        
        no_consecutive_repeats = input("Avoid consecutive repeating characters? (yes/no): ").strip().lower() == 'yes'
        
        num_passwords = int(input("How many passwords would you like to generate? "))

        print("\nGenerated Passwords:")
        
        # Generate and display the requested number of passwords with numbering
        for i in range(1, num_passwords + 1):
            password = generate_password(min_length, max_length, include_special_chars,
                                         special_chars_list, include_numbers,
                                         allow_capital_letters, no_consecutive_repeats,
                                         ensure_one_of_each)
            print(f"{i}. {password}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values where required.")

if __name__ == "__main__":
    main()