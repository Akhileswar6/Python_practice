# Python Tkinter -> Tkinter is Python’s built-in library for creating graphical user interfaces (GUIs). It acts as a lightweight wrapper around Tcl/Tk GUI toolkit, offering Python developers a simple and intuitive way to build desktop applications.

# Create First Tkinter GUI Application

# 1. Tk()
# To create a main window in Tkinter, we use the Tk() class.

# import tkinter as tk
# root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
# root.title("My First Tkinter App")
# root.geometry("400x300")
# root.mainloop()


# 2. mainloop()
# The mainloop() method is used to run application once it is ready

# import tkinter
# m = tkinter.Tk()
# '''
# widgets are added here
# '''
# m.mainloop()


# Tkinter Widget
# 1. Label

from tkinter import *
root = Tk()
w = Label(root, text='GeeksForGeeks.org!')
w.pack()
root.geometry("400x300")
root.mainloop()





















# 2. Widgets
# Widgets are the building blocks of a Tkinter application. They are the elements that make up the user interface, such as buttons, labels, text boxes, etc.

# import tkinter as tk
# root = tk.Tk()
# root.title("Tkinter Widgets Example")
# root.geometry("400x300")
# label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
# label.pack(pady=20)
# button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
# button.pack(pady=10)
# root.mainloop()


