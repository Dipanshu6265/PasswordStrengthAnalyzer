import os

file_path = r"C:\Project\PasswordAnalyzer\common_passwords.txt"
try:
    with open(file_path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file]
    print(f"Read {len(lines)} passwords successfully.")
except Exception as e:
    print(f"Error reading file: {e}")