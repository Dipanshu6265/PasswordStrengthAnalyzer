import tkinter as tk
from tkinter import messagebox
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

# Function to analyze password
def analyze_password():
    password = entry.get()
    text.delete(1.0, tk.END)
    
    if not password:
        messagebox.showerror("Error", "Password cannot be empty.")
        return
    
    common_passwords_file = r"C:\Project\PasswordAnalyzer\common_passwords.txt"
    if not os.path.exists(common_passwords_file):
        messagebox.showerror("Error", f"Common passwords file not found at {common_passwords_file}. Please ensure it exists.")
        text.insert(tk.END, f"Common passwords file not found at {common_passwords_file}. Skipping check.\n\n")
        common_passwords = []
    else:
        try:
            with open(common_passwords_file, "r", encoding="utf-8") as file:
                common_passwords = [line.strip() for line in file]
            if password in common_passwords:
                messagebox.showwarning("Warning", "Password is too common. Choose a different password.")
                return
        except Exception as e:
            messagebox.showerror("Error", f"Error reading common passwords file: {e}.")
            text.insert(tk.END, f"Error reading common passwords file: {e}. Skipping check.\n\n")
            common_passwords = []
    
    score, has_upper, has_lower, has_digit, has_special, entropy = calculate_strength(password)
    
    text.insert(tk.END, "Results:\n")
    text.insert(tk.END, "Length is good!\n" if len(password) >= 8 else "Password is too short.\n")
    text.insert(tk.END, "Contains uppercase letter: Good\n" if has_upper else "Missing uppercase letter\n")
    text.insert(tk.END, "Contains lowercase letter: Good\n" if has_lower else "Missing lowercase letter\n")
    text.insert(tk.END, "Contains digit: Good\n" if has_digit else "Missing digit\n")
    text.insert(tk.END, "Contains special character: Good\n" if has_special else "Missing special character\n")
    text.insert(tk.END, f"\nPassword Strength Score: {score}/100\n")
    text.insert(tk.END, f"Password Entropy: {entropy:.2f} bits\n")
    text.insert(tk.END, "Password Strength: Strong\n" if score >= 80 else "Password Strength: Moderate\n" if score >= 60 else "Password Strength: Weak\n")
    
    if score < 80:
        text.insert(tk.END, "\nSuggestions to improve your password:\n")
        if len(password) < 8:
            text.insert(tk.END, "- Make your password at least 8 characters long\n")
        if not has_upper:
            text.insert(tk.END, "- Add at least one uppercase letter\n")
        if not has_lower:
            text.insert(tk.END, "- Add at least one lowercase letter\n")
        if not has_digit:
            text.insert(tk.END, "- Add at least one digit\n")
        if not has_special:
            text.insert(tk.END, "- Add at least one special character (e.g., !@#$%^&*)\n")

# Function to generate and analyze password
def generate_and_analyze():
    generated = generate_password()
    entry.delete(0, tk.END)
    entry.insert(0, generated)
    analyze_password()

# Function to toggle password visibility
def toggle_password():
    global show_password
    show_password = not show_password
    entry.configure(show="" if show_password else "*")
    toggle_button.config(text="Hide Password" if show_password else "Show Password")

# Create GUI
window = tk.Tk()
window.title("Password Strength Analyzer")
window.geometry("500x400")
window.configure(bg="#F0F0F0")  # Soft gray background
window.iconbitmap(default="")  # Placeholder for icon (no file needed)

# State variable for password visibility
show_password = False

# Input label and entry
label = tk.Label(window, text="Enter Password:", font=("Arial", 14), fg="darkblue", bg="#F0F0F0")
label.pack(pady=20)

entry = tk.Entry(window, width=30, show="*")
entry.pack()

# Buttons
analyze_button = tk.Button(window, text="Analyze", command=analyze_password, bg="#4CAF50", fg="white", font=("Arial", 12), padx=10, pady=5)
analyze_button.pack(pady=10)

generate_button = tk.Button(window, text="Generate Password", command=generate_and_analyze, bg="#2196F3", fg="white", font=("Arial", 12), padx=10, pady=5)
generate_button.pack(pady=10)

toggle_button = tk.Button(window, text="Show Password", command=toggle_password, bg="#9E9E9E", fg="black", font=("Arial", 12), padx=10, pady=5)
toggle_button.pack(pady=10)

quit_button = tk.Button(window, text="Quit", command=window.quit, bg="#F44336", fg="white", font=("Arial", 12), padx=10, pady=5)
quit_button.pack(pady=10)

# Output text area
text = tk.Text(window, height=15, width=50, bg="white", font=("Arial", 10))
text.pack(pady=20)

# Run the GUI
window.mainloop()