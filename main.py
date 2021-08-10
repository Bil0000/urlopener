import tkinter as tk
from tkinter.constants import BOTTOM
import webbrowser

url = 'https://www.facebook.com/'
url1 = 'https://mail.google.com/mail/u/0/#inbox'
url2 = 'https://www.google.com/'
url3 = 'https://stackoverflow.com/'
url4 = 'https://github.com/'
url5 = 'https://youtube.com/'

root = tk.Tk()

def openfacebook():
    webbrowser.open_new(url)

openfacebookbtn = tk.Button(root, text="Open Facebook", fg="blue", command=openfacebook)
openfacebookbtn.pack(side="bottom")

def opengmail():
    webbrowser.open_new(url1)

opengmailbtn = tk.Button(root, text="Open Gmail", fg="red", command=opengmail)
opengmailbtn.pack(side="bottom")

def opengoogle():
    webbrowser.open_new(url2)

opengooglebtn = tk.Button(root, text="Open Google", fg="purple", command=opengoogle)
opengooglebtn.pack(side="bottom")

def openstackoverflow():
    webbrowser.open_new(url3)

openstackoverflowbtn = tk.Button(root, text="Open Stackoverflow", fg="orange", command=openstackoverflow)
openstackoverflowbtn.pack(side="bottom")

def opengithub():
    webbrowser.open_new(url4)

opengithubbtn = tk.Button(root, text="Open Github", fg="black", command=opengithub)
opengithubbtn.pack(side="bottom")

def openyoutube():
    webbrowser.open_new(url5)

openyoutubebtn = tk.Button(root, text="Open Youtube", fg="pink", command=openyoutube)
openyoutubebtn.pack(side="bottom")

canvas = tk.Canvas(root, height=550, width=600, bg="gold")
canvas.pack()

tk.mainloop()
