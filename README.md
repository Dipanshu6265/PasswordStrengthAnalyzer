Password Strength Analyzer
Overview
This is a Python-based password strength analyzer to evaluate password security. It offers both a command-line interface (password_analyzer.py) and a graphical interface (password_analyzer_gui.py). It checks for:

Minimum length of 8 characters
Presence of uppercase letters, lowercase letters, digits, and special characters
Absence of over 1,000 common passwords from a curated list
Provides a strength score (0–100), entropy (in bits), and improvement suggestions
Generates secure random passwords with a "Show/Hide Password" toggle in the GUI

Features

Command-line and enhanced Tkinter GUI interfaces with modern styling
Calculates password entropy to measure randomness
Robust error handling for file access, empty inputs, and non-ASCII characters
Feedback on password strength and specific areas for improvement
Checks against a list of 1,000+ common passwords
Generates random, secure passwords (12 characters, mixed types) with manual visibility control

How to Run

Ensure Python 3.12 or later is installed.
Place password_analyzer.py, password_analyzer_gui.py, and common_passwords.txt in C:\Project\PasswordAnalyzer.
For command-line:
Run: python password_analyzer.py
Choose to analyze a password (1), generate a password (2), or quit (3).


For GUI:
Run: python password_analyzer_gui.py
Enter a password, click "Analyze," "Generate Password," or use "Show/Hide Password" to toggle visibility, then "Quit."



Installation

Install Python from python.org.
Tkinter is included with Python; no additional libraries required.

Usage

Command-line Example:=== Password Strength Analyzer ===
1. Analyze a password
2. Generate a secure password
3. Quit
Enter your choice (1-3): 1
Enter your password: P@ssw0rd!
Results:
Length is good!
Contains uppercase letter: Good
Contains lowercase letter: Good
Contains digit: Good
Contains special character: Good

Password Strength Score: 80/100
Password Entropy: 53.46 bits
Password Strength: Strong


GUI Example:
Run password_analyzer_gui.py, click "Generate Password" to create a random password, use "Show/Hide Password" to toggle visibility, and click "Analyze" to see results in a styled interface.



Future Improvements

Allow customizable password generation (e.g., length, specific characters)
Enhance entropy calculation with more precise charset analysis
Add password history logging or advanced UI themes

Author
[Dipanshu Sonare] – Aspiring cybersecurity student.