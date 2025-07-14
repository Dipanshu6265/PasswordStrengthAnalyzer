# File: clean_passwords.py
with open("common_passwords.txt", "r", encoding="utf-8") as file:
    passwords = [line.strip() for line in file if line.strip().isascii()]

with open("common_passwords_cleaned.txt", "w", encoding="utf-8") as file:
    for password in passwords[:1000]:  # Limit to 1,000+ passwords
        file.write(password + "\n")