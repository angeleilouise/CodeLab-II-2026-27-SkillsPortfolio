from tkinter import * # Imports the TKINTER module

root = Tk() # Creates the window application 
root.title ('Maths Quiz') # Title for the window application 
root.geometry ('400x500') # Sets the size of the window application
root.configure (bg="#ffdaa1") 
root.resizable (0,0) # Sets the window size to fixed 

# Making of Label 1 for the Window Application's Heading: includes text, text colors & style, and positioning 
label1 = Label(root, text="Please select your preffered mode of difficulty!",
          fg = "#ff6d6d", bg= "#ffdaa1", font=("Papyrus", 18, "bold"), wraplength=350, justify="center") # Wraplength and Justify values were driven from ChatGPT 
label1.pack() # Calls the Label 1 so it will display on the GUI 

# Making of Buttons 
def onClick(): # Defines the onClick function, so that each button's command will call this function 
    pass
b1 = Button(root, text = "1. Easy", fg="#ff6d6d", bg="#ffdaa1", font=("Papyrus", 15, "bold"), command = onClick)
b1.place(relx=0.5, y=150, anchor="center") 

b2 = Button(root, text = "2. Moderate", fg="#ff6d6d", bg="#ffdaa1", font=("Papyrus", 15, "bold"), command=onClick)
b2.place(relx=0.5, y=220, anchor="center")

b3 = Button(root, text = "3. Difficult", fg="#ff6d6d", bg="#ffdaa1", font=("Papyrus", 15, "bold"), command=onClick)
b3.place(relx=0.5, y=290, anchor="center") 

root.mainloop() # Keeps the window application open unless user closes it 

