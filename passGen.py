import random
import string

def generate_password(min_length, max_length, use_special_chars, use_numbers, allow_capital_letters, no_consecutive_repeats):
    # Start with lowercase letters
    characters = string.ascii_lowercase
    
    if allow_capital_letters:
        characters += string.ascii_uppercase  # Add uppercase letters if allowed
    
    if use_numbers:
        characters += string.digits  # Add digits to the character set
    
    if use_special_chars:
        characters += string.punctuation  # Add special characters to the character set

    length = random.randint(min_length, max_length)  # Randomly choose a length within the specified range
    password = []
    
    while len(password) < length:
        char = random.choice(characters)
        
        # Check for consecutive repeats if not allowed
        if no_consecutive_repeats and password and char == password[-1]:
            continue
        
        password.append(char)

    return ''.join(password)

def main():
    try:
        # Prompt user for input
        min_length = int(input("Enter the minimum desired password length: "))
        max_length = int(input("Enter the maximum desired password length: "))
        
        include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
        include_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        allow_capital_letters = input("Enable capital letters? (yes/no): ").strip().lower() == 'yes'
        no_consecutive_repeats = input("Avoid consecutive repeating characters? (yes/no): ").strip().lower() == 'yes'
        
        num_passwords = int(input("How many passwords would you like to generate? "))

        print("\nGenerated Passwords:")
        
        # Generate and display the requested number of passwords with numbering
        for i in range(1, num_passwords + 1):
            password = generate_password(min_length, max_length, include_special_chars, include_numbers,
                                         allow_capital_letters, no_consecutive_repeats)
            print(f"{i}. {password}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values where required.")

if __name__ == "__main__":
    main()
