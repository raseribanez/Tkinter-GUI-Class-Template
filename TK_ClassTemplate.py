# Tkinter class template
# Ben Woodfield.
# I have another class tmeplate for tkinter apps, but it had a LOT of
# additional arguments, a bit overkill for the level of stuff I write,
# This one was very much more suited to my programs. And easy to understand!

from Tkinter import *

# Main class
class Application:
    def __init__(self, master):  # Constructor
        def program_functions(): # Program functions
            print("Awesomeness")
        frame = Frame(master)
        frame.pack()
        btn_one = Button(master, text='Exit', command=quit)
        btn_one.pack(side=BOTTOM)

root = Tk()
app = Application(root)
root.title('Title Here')
root.minsize(300,300)

root.mainloop()



'''
AND HERES THE DETAILS ABOUT WHAT IS GOING ON HERE

This sample application is written as a class.

The constructor (the __init__ method) is called with a
Parent widget (known as master)

A number of child widgets are added to the master widget.

The constructor starts by creating a Frame widget. A frame is
a simple container, and in this case is only used to hold the
other widgets (which are to be added)

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()


The frame instance is stored inside a local variable called 'frame'.
After creating the widget we use the pack() method to display it.

We then create the children widgets to add to it (buttons etc)

Finally, we provide some script level code that creates a Tk root
widget, and one instance of the App class using the root widget as
its parent:


root = Tk()
app = App(root)
root.mainloop()
        
'''
