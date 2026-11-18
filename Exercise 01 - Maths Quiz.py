from tkinter import * # Imports the TKINTER module
from PIL import ImageTk, Image # Imports Pillow module so JPG images can be used for the GUI 

root = Tk() # Creates the window application 
root.title ('Maths Quiz') # Title for the window application 
root.geometry ('400x500') # Sets the size of the window application
root.configure (bg="#f7ce87") # Sets the window background color
root.resizable (0,0) # Sets the window size to fixed 
root.iconbitmap('Media Images/Logo.ico')

# Making of Label 1 for the Window Application's Heading: includes text, text colors & style, and positioning 
label1 = Label(root, text="Please select your preffered mode of difficulty! 🧸🍯",
          fg = "white", bg= "#7B3728", font=("Papyrus", 18, "bold"), wraplength=350, justify="center") # Wraplength and Justify values were driven from ChatGPT 
label1.pack(pady=30) # Calls the Label 1 so it will display on the GUI 

# Making of Buttons 
def DisplayMenu(): # This function defines and displays the buttons
    def onClick(): # This function allows for buttons to actually do something, it defines what will happen when a button is clicked
        pass 

# Button 1 with text, font style, font color, and positioning 
    b1 = Button(root, text = "1. Easy 🧸ིྀ", fg="white", bg="#7B3728", font=("Papyrus", 15, "bold"), command = onClick)
    b1.place(relx=0.5, y=180, anchor="center") 

# Button 2 with text, font style, font color, and positioning 
    b2 = Button(root, text = "2. Moderate 🧸ིྀ", fg="white", bg="#7B3728", font=("Papyrus", 15, "bold"), command=onClick)
    b2.place(relx=0.5, y=250, anchor="center")

# Button 3 with text, font style, font color, and positioning 
    b3 = Button(root, text = "3. Difficult 🧸ིྀ", fg="white", bg="#7B3728", font=("Papyrus", 15, "bold"), command=onClick)
    b3.place(relx=0.5, y=320, anchor="center") 

DisplayMenu() # Executes the function, therefore buttons will display 

root.mainloop() # Keeps the window application open unless user closes it 

