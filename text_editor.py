import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete('1.0', tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get('1.0', tk.END))

def about():
    messagebox.showinfo("About", "Simple Text Editor\nCreated with tkinter")

# Create the main window
root = tk.Tk()
root.title("Text Editor")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save As", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

# Create text area
text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, font=("Arial", 12))
text.pack(expand=True, fill='both')

# Run the application
root.mainloop()
