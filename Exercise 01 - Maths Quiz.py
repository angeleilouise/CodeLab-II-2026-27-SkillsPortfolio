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

def decideOperation(): # Function to decide to use either addition or subtraction 

    operation = random.choice(["+", "-"]) 

    return operation # Returns and displays the operation chosen 

def displayProblem(difficulty): # Function to display the equation problem 

    number1 = randomInt(difficulty) # First number generated 
    number2 = randomInt(difficulty) # Second number generated 

    operation = decideOperation() # Randomly chooses an operator (+ or -)

    if operation == "+": # If operator is + then add number 1 and number 2 together
        correct_answer = number1 + number2 # Correct answer should be the two numbers added together accurately 

    elif operation == "-": # If operator is - then subtract number 2 from number 1
        correct_answer = number1 - number2 # Correct answer should be the two number's subtracted from each other accordingly 

    question = str(number1) + " " + operation + " " + str(number2) + " = ?" # Converts number into strings to combine them into a question 

    return question, correct_answer # Displays the question and correct answer 

def isCorrect(user_answer, correct_answer): # isCorrect function 

    if user_answer == correct_answer: # IF condition that IF user answer is correct then what returns is True
        return True

    else: # ELSE condition that if user answer is not correct it returns False 
        return False

def MathsQuiz(difficulty): # Function for the difficulty levels and this is the start of our QUIZ PAGE FRAME
    home_page.place_forget() # This will allow for a blank window frame when buttons are clicked 

    quiz_page = Frame(root, bg="#f7ce87") # This is the windown frame for the quiz page with its background color 
    quiz_page.place(x=0, y=0,relwidth=1, relheight=1) # Quiz page's window frame positioning 

    score = 0 # User's total points 
    question_number = 1 # Question they are currently answering
    attempts = 0 # How many times the user is attempting to answer the question (attempt 1, attempt 2)

    quiz_page_title = Label(quiz_page, text="Maths Quiz 🧸🍯", fg="white", bg="#7B3728", font=("Papyrus", 25, "bold")) # Title and text for the quiz page with its colors and styles
    quiz_page_title.pack(pady=30) # Quiz page positioning 

    difficulty_label = Label(quiz_page, text="Difficulty: " + difficulty, fg="#7B3728", bg="#f7ce87", font=("Papyrus", 16, "bold")) # This label display the difficulty level the user has selected 
    difficulty_label.pack(pady=10) # Label positioning 

    def nextEquation(): # Calls for the next equation 
        nonlocal attempts, correct_answer

        attempts = 0 # attempts can hit 0 
        question, correct_answer = displayProblem(difficulty) 
        question_label.config(text=question) 
        answer_entry.delete(0, END)

    def nextQuestion(): # Calls for next question 

        nonlocal question_number

        if question_number < 10: #IF question has not reached question 10, it moves forward and calls the next equation 

            question_number += 1

            nextEquation()

        else: # ELSE quiz has been completed and final score will be shown 

            print("Quiz finished!")
            print("Final score:", score)

    question, correct_answer = displayProblem(difficulty) # Displays equation problem

    question_label = Label(quiz_page, text=question, fg="#7B3728", bg="#f7ce87", font=("Papyrus", 25, "bold")) # Label for equation problem with its colors and styles
    question_label.pack(pady=20) # Displays the question_label and positioning 

    answer_entry = Entry(quiz_page, font=("Papyrus", 18), justify="center") # Entry widget for user to enter their input/answer 
    answer_entry.pack(pady=10) # Entry widget positioning 

    feedback_label = Label(quiz_page, text="", fg="#7B3728", bg="#f7ce87", font=("Papyrus", 13, "bold")) # This label displays feedback for each answer user inputs 
    feedback_label.pack(pady=10)

    def checkAnswer(): # Function to check whether answer is correct 
        nonlocal score, attempts, question_number
        user_answer = answer_entry.get() # Gets user answer from answer entry

        if user_answer.lstrip("-").isdigit(): # Allows for negative equations 
            user_answer = int(user_answer) 

            if isCorrect(user_answer, correct_answer): # Full score of 10 points if attempt has not been maxed out 

                if attempts == 0:
                    score += 10

                else: # ELSE user will only get 5 points for a correct answer 
                    score += 5

                feedback_label.config(text="Correct! Well done!🧸❤️") # Feedback label for correct answer 

                nextQuestion() # Call for the next question

            else: # ELSE if attempt 1 is used up, feedback label will say incorrect but user will be given a chance to try again 

                attempts += 1

                if attempts == 1:
                    feedback_label.config(text="Incorrect! Try again!🧸")

                else: # IF attempt has been maxed out with incorrect answer, the next question will be called automatically 
                    feedback_label.config(text="Incorrect! Let's move on..")

                    nextQuestion()

        else: # Handles invalid user inputs 
            feedback_label.config(text="Please enter a valid number!🧸")

    submit_button = Button(quiz_page, text="Submit ♡", fg="white", bg="#7B3728", font=("Papyrus", 15, "bold"), command=checkAnswer) # Submit button 
    submit_button.pack(pady=20) # Displays submit button and defines its positioning 

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

