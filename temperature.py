import tkinter as tk

def convert_to_fahrenheit():
    celsius = float(entry.get())
    fahrenheit = (celsius * 9/5) + 32
    result_label.config(text=f"{celsius} Celsius = {fahrenheit:.2f} Fahrenheit")

def convert_to_celsius():
    fahrenheit = float(entry.get())
    celsius = (fahrenheit - 32) * 5/9
    result_label.config(text=f"{fahrenheit} Fahrenheit = {celsius:.2f} Celsius")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create input entry
entry = tk.Entry(root)
entry.pack()

# Create buttons for conversion
to_fahrenheit_button = tk.Button(root, text="Convert to Fahrenheit", command=convert_to_fahrenheit)
to_fahrenheit_button.pack()

to_celsius_button = tk.Button(root, text="Convert to Celsius", command=convert_to_celsius)
to_celsius_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
