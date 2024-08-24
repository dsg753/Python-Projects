'''Python Program - QR Code generating by DJ Harshit'''

from tkinter import *
from tkinter import messagebox
import time
import pyqrcode
from PIL import Image, ImageTk
import os

def generate_qr_code(content):
    """
    Generates a QR code image from the provided content.

    Args:
        content (str): The content to encode in the QR code.

    Returns:
        BitmapImage: A Tkinter BitmapImage to display the QR code.
    """
    qr = pyqrcode.create(content)
    qr_xbm = qr.xbm(scale=5)
    img = BitmapImage(data=qr_xbm, foreground='black', background='white')
    return img, qr

def display_qr_code(img):
    """
    Displays the generated QR code on the UI.

    Args:
        img (BitmapImage): The generated QR code image.
    """
    l4.config(image=img)
    l4.image = img  # Keep reference to avoid garbage collection

def save_qr_code(qr):
    """
    Saves the generated QR code as a PNG file.

    Args:
        qr (pyqrcode.QRCode): The QR code object.
    """
    tme = int(time.time())
    filename = f'{tme}.png'
    qr.png(filename, scale=8)
    messagebox.showinfo("QR Code Saved", f"QR code saved as {filename}")
    con.set('')  # Clear the input field after saving

def on_generate_click():
    """
    Handles the QR code generation button click.
    """
    content = con.get()
    if not content:
        messagebox.showwarning("Input Error", "Please enter content for the QR code.")
        return

    img, qr = generate_qr_code(content)
    display_qr_code(img)
    b2.config(state=NORMAL)  # Enable save button

def on_save_click():
    """
    Handles the save button click.
    """
    if l4.image:
        save_qr_code(qr)
        l4.config(image='')  # Clear the displayed QR code
        b2.config(state=DISABLED)  # Disable save button after saving
    else:
        messagebox.showwarning("No QR Code", "Generate a QR code before saving.")

# Main program
wind = Tk()
wind.title('QR Code Generator')
wind.geometry('500x400')
wind.resizable(0, 0)

# Variable
con = StringVar()

# Layout
f1 = Frame(wind, width=500, height=100)
f1.pack()
f2 = Frame(wind, width=500, height=50)
f2.pack()
f3 = Frame(wind, width=500, height=250)
f3.pack()

l1 = Label(f1, text='QR Code Generator', font=('Arial Bold', 30))
l1.grid(row=0, column=0, columnspan=3, padx=5, pady=10)
l2 = Label(f1, text='By Harshit', font=('Arial', 15))
l2.grid(row=0, column=4, sticky='w', pady=10)

l3 = Label(f2, text='Enter the content')
l3.grid(row=0, column=0, padx=5)

e1 = Entry(f2, textvariable=con, width=40)
e1.grid(row=0, column=1, padx=5)

b1 = Button(f2, text='Generate', command=on_generate_click)
b1.grid(row=1, column=0, pady=10)

b2 = Button(f2, text='Save', command=on_save_click, state=DISABLED)
b2.grid(row=1, column=1, pady=10)

l4 = Label(f3, pady=5)
l4.pack()

wind.mainloop()
