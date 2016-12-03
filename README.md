# Tkinter-GUI-Class-Template
Wraps a Tk project in an Application class - Use this to start a GUI project in Tkinter easily 

I just wanted a quick and easy template to start off my Tkinter / GUI projects in Python, as I seem to use the tkinter module quite often for little things I write. So the first version of this I went looking around and there is still a copy of it in another repository - called something like 'Tkinter examples'. It had a lot of additional arguments that I honestly had no idea about, and no use for so although it worked, I wanted a lightweight version suitable for my level of writing - and understanding.

You may see some of my other Tk projects with this other template/class, and it is a bit overkill. I will try to re-do those using the old version over time.

Anyway here's the new version

Nice and lightweight, nice and simple, wraps a Tk project into a class, or starts a project off as a class, however you want to use it, the code looks something like this:


    from Tkinter import *
    class Application:
        def __init__(self, master): 
            
            #def your_program_functions():
                #print("Awesomeness")
                            
            frame = Frame(master)
            frame.pack()
            # OtherWidgetsHere
            
            btn_one = Button(master, text='Exit', command=quit)
            btn_one.pack(side=BOTTOM)

    root = Tk()
    app = Application(root)
    root.title('Title Here')
    root.minsize(300,300)
    root.mainloop()


This creates an application class (called Application). The constructor is the __init__ method. It is called with a Parent widget, which we have named 'master'. Then from there we add our program. The frame is known as a container, everything that gets added to this template will be diaplayed within this frame. This container will hold ALL of the child widgets. Child widgets are things like buttons and labels within the tkinter GUI. The content you would write as normal.

So after the frame/container, you then add your program widgets. Note where I added 
    
    def your_program_function():

before the frame. This worked for me, I added my functions up here and it seemed to work fine.

Then at the end you see the usual Tkinter configuration stuff - creating a root = Tk() widget, and the title and window size etc. This is at the top level / script level because everything else needs to be created according to these settings (so not inside the class)

And finally the good old mainloop to kick start it all

I hope this template is of use to somebody. If it isn't I am not too bothered as I know I will get some use from it, that is why I made this repo, I make so many little Tkinter apps just playing around, and I get lazy...I find myself opening other projects as a starting point for a new one, so that was the reason I wanted a template to start me off.
