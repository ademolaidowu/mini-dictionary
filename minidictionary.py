"""This is a program to create a very user friendly interactive dictionary"""
from tkinter import *
import json
import difflib
from difflib import get_close_matches


data = json.load(open("data.json"))

def definition(term):
    "A function to return the definition of a word"
    term = term.lower()
    matches = get_close_matches(term, data.keys(), 3, 0.8)
    
    if term in data:
        return data[term] 
        
    elif  len(matches) > 0:
        return "The word doesn't exist. \nPossible suggestions: {} ".format(str(matches[0:3]).upper())

    else:
        return "The word {} doesn't exist,please double check it".format(term)


def display():
    listbox.delete(0, END)
    output = definition(value.get())
    if type(output) == list:
        for item in output:
            listbox.insert(END, item)
    else:
       listbox.insert(END, output) 


"""GUI"""
window = Tk()
window.title("Dictionary")
window.iconbitmap("Book.ico")
    
b1 = Button(window, text = "DEFINE", command = display)
b1.grid(row = 4, column = 1)

value = StringVar()
l1 = Label(window, text = "Word:")
l1.grid(row = 3, column = 0)

e1 = Entry(window, textvariable = value)
e1.grid(row = 3, column = 1)

listbox = Listbox(window, height=10, width=70)
listbox.grid(row=1, column=2, rowspan=8, columnspan=7)
    
sb = Scrollbar(window, orient='horizontal')
sb.grid(row=10, column=2, columnspan=7)

listbox.configure(xscrollcommand=sb.set)
sb.configure(command=listbox.xview)

window.mainloop()