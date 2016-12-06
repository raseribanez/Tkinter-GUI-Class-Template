# Ben Woodfield
# 06/12/2016
# An example program using my Tkinter GUI Class Template
# This is an Antenna wavelength program from another repository I have
# I have wrapped the whole thing into an Aplication class
# The program then uses a main Frame as a container for all the other child widgets

from tkinter import *

# Main class
class Application:
    # Constructor
    def __init__(self, master):
        cvt_from = StringVar()
        cvt_to = StringVar()
		
        def calculate_full_meter():
            freq_val = int(cvt_from.get())
            full_wave = 306.342/freq_val  # Full wave loop meters calculation
            cvt_to.set('%s Meters' % full_wave)
   
        frame = Frame(master)
        frame.pack()
		
	# Label to display instructions
        lbl_one = Label(master, text='Enter your Frequency \n in MHz', font='freesansbold')
        lbl_one.pack(fill=X)

        # Take the frequency from the user
        freq_input = Entry(master, textvariable=cvt_from, relief='sunken', justify='center', width=30, font=14)
        freq_input.pack()

        # Label to display instructions
        lbl_two = Label(master, text='Click the Button \nTo Calculate Full wavelength \nIn meters', font='freesansbold')
        lbl_two.pack(fill=X)
		
	# Button to Calculate Full Wave Length in Meters
        btn_one = Button(master, bg='DarkGrey', text='CALCULATE', font='freesansbold', fg='Blue', command=calculate_full_meter)
        btn_one.pack(fill=X)

	# Label to display the results of the calculation	
        lbl_result = Label(master, textvariable=cvt_to, relief='flat', bg='Grey', font='freesansbold', fg='Blue')
        lbl_result.pack(fill=BOTH, expand=1)

        # The exit Button
        btn_exit = Button(master, text='Exit')
        btn_exit.pack(side=BOTTOM, fill=X)
		

root = Tk()
app = Application(root)
root.title('Antenna Wavelength Calculator')
root.minsize(350,350)

root.mainloop()
