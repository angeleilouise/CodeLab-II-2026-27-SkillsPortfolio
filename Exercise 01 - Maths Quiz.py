from tkinter import * # Imports the TKINTER module
from PIL import ImageTk, Image # Imports Pillow module so JPG images can be used for the GUI 
import random # Allows our quiz to generate random arithmatic equations 

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

def randomInt(difficulty): # Function to generate numbers, includes IF and ELIF conditions 
    if difficulty == "Easy 🧸ིྀ":
        number = random.randint(0, 9) # Single digit numbers

    elif difficulty == "Moderate 🧸ིྀ":
        number = random.randint(10, 99) # Double digits numbers

    elif difficulty == "Advanced 🧸ིྀ":
        number = random.randint(1000, 9999) # Four digits numbers 

    return number # Returns generated numbers 

def decideOperation():

    operation = random.choice(["+", "-"])

    return operation

def displayProblem(difficulty):

    number1 = randomInt(difficulty)
    number2 = randomInt(difficulty)

    operation = decideOperation()

    if operation == "+":
        correct_answer = number1 + number2

    elif operation == "-":
        correct_answer = number1 - number2

    question = str(number1) + " " + operation + " " + str(number2) + " = ?"

    return question, correct_answer

def MathsQuiz(difficulty): # Function for the difficulty levels and this is the start of our QUIZ PAGE FRAME
    home_page.place_forget() # This will allow for a blank window frame when buttons are clicked 

    quiz_page = Frame(root, bg="#f7ce87") # This is the windown frame for the quiz page with its background color 
    quiz_page.place(x=0, y=0,relwidth=1, relheight=1) # Quiz page's window frame positioning 

    score = 0 # User's total points 
    question_number = 1 # Question they are currently answering
    attempts = 0 # How many times the user is attempting to answer the question (attempt 1, attempt 2)

    quiz_page_title = Label(quiz_page, text="Maths Quiz 🧸🍯", fg="white", bg="#7B3728", font=("Papyrus", 25, "bold")) # Title and text for the quiz page with its colors and styles
    quiz_page_title.pack(pady=30) # Quiz page positioning 

    difficulty_label = Label(quiz_page, text="Difficulty: " + difficulty, fg="#7B3728", bg="#f7ce87", font=("Papyrus", 16, "bold"))
    difficulty_label.pack(pady=10) 

# Making of Buttons 
def displayMenu(): # This function defines and displays the buttons (it is placed below MathsQuiz because MathsQuiz should be defined first as we try to call it in this function)
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

