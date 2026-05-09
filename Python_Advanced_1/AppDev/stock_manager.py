import tkinter as tk

# Backend
def insert_item():
    pass

def delete_item():
    pass

def clear():
    pass

# UI

# Create a new main window
root = tk.Tk()

# Set the title for the page
root.title("Shopping Manager")

# Input fields
item_name_label = tk.Label(root, text="Item name:")
item_name_label.grid(row=0, column=0, padx=20, pady=20)
item_name_entry = tk.Entry(root)
item_name_entry.grid(row=0, column=1, padx=20, pady=20)

item_quantity_label = tk.Label(root, text="Quantity:")
item_quantity_label.grid(row=1, column=0, padx=20, pady=20)
item_quantity_entry = tk.Entry(root)
item_quantity_entry.grid(row=1, column=1, padx=20, pady=20)

item_price_label = tk.Label(root, text="Price:")
item_price_label.grid(row=2, column=0, padx=20, pady=20)
item_price_entry = tk.Entry(root)
item_price_entry.grid(row=2, column=1, padx=20, pady=20)

# Buttons
insert_button = tk.Button(root, text="Insert", command=insert_item)
insert_button.grid(row=3, column=0, padx=20, pady=20)

delete_button = tk.Button(root, text="Delete", command=delete_item)
delete_button.grid(row=3, column=1, padx=20, pady=20)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=4, column=0, padx=20, pady=20)

# Event Loop
root.mainloop()