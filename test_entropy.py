import math

password = "P@ssw0rd"
length = len(password)
charset_size = 62  # Assume alphanumeric (26 lowercase + 26 uppercase + 10 digits)
entropy = math.log2(charset_size ** length)
print(f"Password: {password}")
print(f"Entropy: {entropy:.2f} bits")