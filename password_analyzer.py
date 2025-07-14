import random
import string
import math
import os

# Define special characters
special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

# Function to calculate password strength score and entropy
def calculate_strength(password):
    score = 0
    if len(password) >= 8:
        score += 20
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in special_chars for c in password)
    if has_upper:
        score += 20
    if has_lower:
        score += 20
    if has_digit:
        score += 20
    if has_special:
        score += 20
    
    charset_size = 0
    if has_upper:
        charset_size += 26
    if has_lower:
        charset_size += 26
    if has_digit:
        charset_size += 10
    if has_special:
        charset_size += len(special_chars)
    entropy = math.log2(charset_size ** len(password)) if charset_size > 0 else 0
    
    return score, has_upper, has_lower, has_digit, has_special, entropy

# Function to generate a secure password
def generate_password(length=12):
    if length < 8:
        length = 8
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + special_chars
    password = (
        random.choice(string.ascii_uppercase) +
        random.choice(string.ascii_lowercase) +
        random.choice(string.digits) +
        random.choice(special_chars) +
        ''.join(random.choice(chars) for _ in range(length - 4))
    )
    return ''.join(random.sample(password, len(password)))

# Main program loop
while True:
    print("\n=== Password Strength Analyzer ===")
    print("1. Analyze a password")
    print("2. Generate a secure password")
    print("3. Quit")
    try:
        choice = input("Enter your choice (1-3): ")
        if choice == '3':
            print("Exiting program.")
            break
        elif choice == '2':
            generated = generate_password()
            print(f"\nGenerated Secure Password: {generated}")
            print("\nAnalysis of generated password:")
            strength_score, has_upper, has_lower, has_digit, has_special, entropy = calculate_strength(generated)
            print(f"Results:")
            print(f"Length is good!" if len(generated) >= 8 else "Password is too short.")
            print(f"Contains uppercase letter: Good" if has_upper else "Missing uppercase letter")
            print(f"Contains lowercase letter: Good" if has_lower else "Missing lowercase letter")
            print(f"Contains digit: Good" if has_digit else "Missing digit")
            print(f"Contains special character: Good" if has_special else "Missing special character")
            print(f"\nPassword Strength Score: {strength_score}/100")
            print(f"Password Entropy: {entropy:.2f} bits")
            print("Password Strength: Strong" if strength_score >= 80 else "Password Strength: Moderate" if strength_score >= 60 else "Password Strength: Weak")
            continue
        elif choice != '1':
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        password = input("Enter your password: ")
        if not password:
            print("Error: Password cannot be empty.")
            continue

        # Check against common passwords
        common_passwords_file = r"C:\Project\PasswordAnalyzer\common_passwords.txt"
        if not os.path.exists(common_passwords_file):
            print(f"Error: Common passwords file not found at {common_passwords_file}. Please ensure it exists.")
            common_passwords = []
        else:
            try:
                with open(common_passwords_file, "r", encoding="utf-8") as file:
                    common_passwords = [line.strip() for line in file]
                if password in common_passwords:
                    print("Password is too common. Choose a different password.")
                    continue
            except Exception as e:
                print(f"Error reading common passwords file: {e}. Skipping check.")
                common_passwords = []

        # Calculate strength and get flags
        strength_score, has_upper, has_lower, has_digit, has_special, entropy = calculate_strength(password)

        # Check password length
        print("\nResults:")
        if len(password) < 8:
            print("Password is too short. It should be at least 8 characters.")
        else:
            print("Length is good!")

        # Provide character type feedback
        if has_upper:
            print("Contains uppercase letter: Good")
        else:
            print("Missing uppercase letter")
        if has_lower:
            print("Contains lowercase letter: Good")
        else:
            print("Missing lowercase letter")
        if has_digit:
            print("Contains digit: Good")
        else:
            print("Missing digit")
        if has_special:
            print("Contains special character: Good")
        else:
            print("Missing special character")

        # Display strength score and entropy
        print(f"\nPassword Strength Score: {strength_score}/100")
        print(f"Password Entropy: {entropy:.2f} bits")
        print("Password Strength: Strong" if strength_score >= 80 else "Password Strength: Moderate" if strength_score >= 60 else "Password Strength: Weak")

        # Provide improvement suggestions
        if strength_score < 80:
            print("\nSuggestions to improve your password:")
            if len(password) < 8:
                print("- Make your password at least 8 characters long")
            if not has_upper:
                print("- Add at least one uppercase letter")
            if not has_lower:
                print("- Add at least one lowercase letter")
            if not has_digit:
                print("- Add at least one digit")
            if not has_special:
                print("- Add at least one special character (e.g., !@#$%^&*)")

    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting.")
        break