import tkinter as tk

# Create window
root = tk.Tk()
root.title("My First Window App")
root.geometry("400x250")

# Add text
label = tk.Label(root, text="Hello Gayana 😄", font=("Arial", 18))
label.pack(pady=20)

# Button action
def show_message():
    label.config(text="You clicked the button! 🎉")

# Button
button = tk.Button(root, text="Click Me", font=("Arial", 14), command=show_message)
button.pack(pady=10)

# Run the window
root.mainloop()