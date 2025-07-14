import tkinter as tk

window = tk.Tk()
window.title("UI Test")
window.geometry("400x300")

# Background color
window.configure(bg="lightblue")

# Label with custom font and color
label = tk.Label(window, text="Test Label", font=("Arial", 14), fg="darkblue", bg="lightblue")
label.pack(pady=20)

# Button with color
button = tk.Button(window, text="Click Me", bg="lightgreen", fg="black", font=("Arial", 12))
button.pack(pady=10)

window.mainloop()