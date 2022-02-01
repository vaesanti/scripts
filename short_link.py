#!/bin/py
'''
import pyshorteners as ps

link = input("link: ")
short = ps.Shortener()
x = short.tinyurl.short(link)
print(x)


import pyshorteners as ps

url = "http://1b0b-2804-1b3-1080-7d46-d087-295b-7297-18ca.ngrok.io/1.jpg"
short = ps.Shortener().tinyurl.short(url)
print(short)


####################YOUTUBE_SHORT_LINK
x = True
while x == True:
	big_link = input("link: ")
	if big_link == "":
		break
	string_1 = big_link
	p1 = string_1.partition("https://www.youtube.com/watch?v=")
	string_2 = p1[2]
	p2 = string_2.partition("&feature=youtu.be")
	string_3 = p2[0]
	short_link = "https:youtu.be/"+string_3
	print()
	print(short_link)
	print()
#########################################
'''
import pyshorteners
import pyperclip
from tkinter import *

root = Tk()
root.geometry("400x200")
root.title("URL SHORTENER")
root.configure(bg='#49A')
url = StringVar()
url_address = StringVar()

def urlshortener():
    urladdress = url.get()
    url_add = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_add)

def copyurl():
    url_add = url_address.get()
    pyperclip.copy(url_add)

Label(root, text="URL SHORTENER", font="calibri 20 bold").pack(pady=10)
Entry(root,textvariable=url).pack(pady=5)
Button(root, text="Generate Short Url", command=urlshortener).pack(pady=7)
Entry(root, textvariable = url_address).pack(pady=5)
Button(root, text="Copy",command=copyurl).pack()

root.mainloop()

