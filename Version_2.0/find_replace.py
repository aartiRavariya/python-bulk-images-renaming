from tkinter import messagebox
import os
from tkinter import filedialog
from tkinter import *
import re


# Function to rename multiple files
def submit():
    find = find_path.get()
    replace = replace_path.get()
    input_folder = filedialog.askdirectory()

    cntr = 0
    for root, dirs, files in os.walk(input_folder):
        for img_file in files:
            src = os.path.join(root, img_file)
            newname = src.replace(find, replace)
            dst = os.path.join(root, newname)
            os.rename(src, dst)
            cntr += 1

    find_path.set("")
    replace_path.set("")
    if cntr > 0:
        messagebox.showinfo("Done", "Files Renamed Successfully...!!")
    else:
        messagebox.showerror("Error", "No files renamed...!!")


# Driver Code
if __name__ == '__main__':
    top = Tk()
    top.geometry("450x300")
    top.title("Image Files Renamer")
    top.configure(background="Dark grey")

    label_find_path = Label(top, text="Enter the text to find:", bg="Dark grey").place(x=40, y=40)

    find_path = StringVar()
    entry_find_path = Entry(top, textvariable=find_path, width=50).place(x=40, y=70)

    label_replace_path = Label(top, text="Enter the text to replace:", bg="Dark grey").place(x=40, y=120)

    replace_path = StringVar()
    entry_replace_path = Entry(top, textvariable=replace_path, width=50).place(x=40, y=150)

    submit_button = Button(top, text="Submit", command=submit).place(x=200, y=200)
    top.mainloop()
