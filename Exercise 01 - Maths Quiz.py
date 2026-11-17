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

root.mainloop() # Keeps the window application open unless user closes it 

