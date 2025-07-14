import tkinter as tk

window = tk.Tk()
window.title("Test GUI")
window.geometry("400x300")

label = tk.Label(window, text="Enter something:")
label.pack()

entry = tk.Entry(window)
entry.pack()

def show_input():
    text.delete(1.0, tk.END)
    text.insert(tk.END, f"You entered: {entry.get()}")

button = tk.Button(window, text="Show Input", command=show_input)
button.pack()

text = tk.Text(window, height=5, width=30)
text.pack()

window.mainloop()