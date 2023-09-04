from tkinter import *
from tkinter import messagebox
import pyshorteners as ps
from PIL import Image, ImageTk
import tkinter

root = Tk()
root.title("URL Shortener")
root.geometry("541x337")
canvas = Canvas(root, width=541, height=337)
photo = ImageTk.PhotoImage(Image.open("bg_image.jpg"))
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()


def shortenurl():
    # creating the object of pyshorteners
    s = ps.Shortener()
    short = s.tinyurl.short(longurl_entry.get())  # creating a short url from the long one
    shorturl_entry.insert(0, short)  # entering into output box
    root.clipboard_clear()
    root.clipboard_append(short)  # copying the short url to clipboard
    messagebox.showinfo("Message", " Shortened URL is Copied to your Clipboard!!")


# longurl_label = tkinter.Label(root, text="Enter the URL", font=('Arial', 15))
canvas.create_text(270, 125, text="Enter the URL", fill="black", font='Helvetica 15 bold')
longurl_entry = tkinter.Entry(root, font=('Arial', 15))
# shorturl_label = tkinter.Label(root, text="Shortened URL", font=('Arial', 15))
canvas.create_text(270, 185, text="Shortened URL", fill="black", font='Helvetica 15 bold')
shorturl_entry = tkinter.Entry(root, font=('Arial', 15))
shorten_button = tkinter.Button(root, text="Shorten URL", command=shortenurl)


longurl_entry.place(x=160, y=135)
shorturl_entry.place(x=160, y=195)
shorten_button.place(x=220, y=225)

root.mainloop()
