from tkinter import * # Imports the TKINTER module
from PIL import ImageTk, Image # Imports Pillow module so JPG images can be used for the GUI 

root = Tk() # Creates the window application 
root.title ('Maths Quiz') # Title for the window application 
root.geometry ('400x500') # Sets the size of the window application
root.configure (bg="#f7ce87") # Sets the window background color
root.resizable (0,0) # Sets the window size to fixed 
root.iconbitmap('Media Images/Logo.ico')

home_page = Frame(root, bg="#f7ce87") # This is the window frame for the home page 
home_page.place(x=0, y=0, relwidth=1, relheight=1) # Main window frame positioning 

# Making of Label 1 for the Window Application's Heading: includes text, text colors & style, and positioning 
label1 = Label(home_page, text="Please select your preffered mode of difficulty! 🧸🍯",
          fg = "white", bg= "#7B3728", font=("Papyrus", 18, "bold"), wraplength=350, justify="center") # Wraplength and Justify values were driven from ChatGPT 
label1.pack(pady=30) # Calls the Label 1 so it will display on the GUI 

def MathsQuiz(difficulty): # Function for the difficulty levels 
    home_page.place_forget() # This will allow for a blank window frame when buttons are clicked 

    quiz_page = Frame(root, bg="#f7ce87") # This is the windown frame for the quiz page with its background color 
    quiz_page.place(x=0, y=0,relwidth=1, relheight=1) # Quiz page's window frame positioning 

    quiz_page_title = Label(quiz_page, text="Maths Quiz 🧸🍯", fg="white", bg="#7B3728", font=("Papyrus", 25, "bold")) # Title and text for the quiz page with its colors and styles
    quiz_page_title.pack(pady=30) # Quiz page positioning 

    difficulty_label = Label(quiz_page, text="Difficulty: " + difficulty, fg="#7B3728", bg="#f7ce87", font=("Papyrus", 16, "bold"))
    difficulty_label.pack(pady=10) 

# Making of Buttons 
def displayMenu(): # This function defines and displays the buttons
    def onClick(): # This function allows for buttons to actually do something, it defines what will happen when a button is clicked
        pass 

# Button 1 with text, font style, font color, and positioning 
    b1 = Button(home_page, text = "1. Easy 🧸ིྀ", fg="white", bg="#7B3728", font=("Papyrus", 15, "bold"), command = lambda: MathsQuiz("Easy 🧸ིྀ"))
    b1.place(relx=0.5, y=180, anchor="center") 

# Button 2 with text, font style, font color, and positioning 
    b2 = Button(home_page, text = "2. Moderate 🧸ིྀ", fg="white", bg="#7B3728", font=("Papyrus", 15, "bold"), command=lambda: MathsQuiz("Moderate 🧸ིྀ"))
    b2.place(relx=0.5, y=250, anchor="center")

# Button 3 with text, font style, font color, and positioning 
    b3 = Button(home_page, text = "3. Advanced 🧸ིྀ", fg="white", bg="#7B3728", font=("Papyrus", 15, "bold"), command=lambda: MathsQuiz("Advanced 🧸ིྀ")) 
    b3.place(relx=0.5, y=320, anchor="center") 

displayMenu() # Executes the function, therefore buttons will display 

root.mainloop() # Keeps the window application open unless user closes it 

