import tkinter as tk

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry field
entry = tk.Entry(root, width=25, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the button labels
button_labels = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+')
]

# Create buttons
for i, row in enumerate(button_labels):
    for j, label in enumerate(row):
        if label == '=':
            btn = tk.Button(root, text=label, width=5, command=calculate)
        elif label == 'C':
            btn = tk.Button(root, text=label, width=5, command=clear)
        else:
            btn = tk.Button(root, text=label, width=5, command=lambda key=label: press(key))
        btn.grid(row=i+1, column=j, padx=5, pady=5)

# Run the application
root.mainloop()
