import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():

            if char.islower():
                alphabet = 'abcdefghijklmnopqrstuvwxyz'
            else:
                alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

            shifted_idx = (alphabet.index(char) + shift) % 26

            if mode == 'decrypt':
                shifted_idx = (alphabet.index(char) - shift) % 26
            result += alphabet[shifted_idx]

        else:
            result += char
    return result

def encrypt_decrypt():
    mode = mode_var.get()
    text = text_entry.get()
    shift = int(shift_entry.get())

    if mode == 'Encrypt':
        result = caesar_cipher(text, shift, 'encrypt')
        result_label.config(text=f"Encrypted message: {result}")

    else:
        result = caesar_cipher(text, shift, 'decrypt')
        result_label.config(text=f"Decrypted message: {result}")

# creating tkinter window
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("400x300")

# Label and Entry for text input
tk.Label(root, text="Enter the message:").pack()
text_entry = tk.Entry(root)
text_entry.pack()

# Label and Entry for shift value input
tk.Label(root, text="Enter the shift value:").pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

# Dropdown for mode selection
mode_var = tk.StringVar()
mode_var.set("Encrypt")
mode_dropdown = tk.OptionMenu(root, mode_var, "Encrypt", "Decrypt")
mode_dropdown.pack()

# Button to trigger encryption/decryption
tk.Button(root, text="Encrypt/Decrypt", command=encrypt_decrypt).pack()

# Label to display result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
