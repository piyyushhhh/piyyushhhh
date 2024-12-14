import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize the main window
root = tk.Tk()
root.title("Simple Notepad")
root.geometry("600x400")

# Create the Text widget (for writing the text)
text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
text_area.pack(expand="true", fill="both")

# Track the file name
filename = None

# Create the Menu Bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# New file operation
file_menu.add_command(label="New", command=lambda: text_area.delete(1.0, tk.END))

# Open file operation
file_menu.add_command(label="Open", command=lambda: open_file(filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])))
 
# Save file operation
file_menu.add_command(label="Save", command=lambda: save_file() if filename else save_as_file())

# Save As file operation
file_menu.add_command(label="Save As", command=lambda: save_as_file())

# Exit application operation
file_menu.add_separator()
file_menu.add_command(label="Exit", command=lambda: root.quit())

# Add Edit Menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Undo operation
edit_menu.add_command(label="Undo", command=lambda: text_area.edit_undo())

# Redo operation
edit_menu.add_command(label="Redo", command=lambda: text_area.edit_redo())

# Open File Logic
def open_file(file_path):
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)
        global filename
        filename = file_path
        root.title(f"Simple Notepad - {file_path}")

# Save File Logic
def save_file():
    if filename:
        with open(filename, "w") as file:
            content = text_area.get(1.0, tk.END)
            file.write(content)

# Save As File Logic
def save_as_file():
    global filename
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        filename = file_path
        with open(filename, "w") as file:
            content = text_area.get(1.0, tk.END)
            file.write(content)
        root.title(f"Simple Notepad - {file_path}")

# Run the Tkinter main loop
root.mainloop()
