from tkinter import * # Imports Tkinter module 
import random # Imports random values 
from PIL import ImageTk, Image # Allows us to display images in jpg or png 

root = Tk() # Root
root.title("Alexa, Tell me a Joke") # Window application's title 
root.geometry("700x400") # Window application's size 

# Welcome Frame : To welcome users 
welcome_frame = Frame(root, bg="#f1e2e8")  
welcome_frame.place(relx=0, rely=0, relwidth=1, relheight=1) 
welcome_label = Label(welcome_frame, text="Welcome to Alexa's Little Joke Corner! ฅ^>⩊<^ ฅ", font=("Arial Black", 18, "bold"), fg="#d1c2bb", bg="#f1e2e8")
welcome_label.place(relx=0.5, rely=0.35, anchor="center")

# Second Frame is halved horizonatally : Top and Bottom 
top_frame = Frame(root, bg="#f1e2e8")
bottom_frame = Frame(root, bg="#d1c2bb")

# This temporarily removes Second Frame so it won't disrupt visuals in the Welcome Frame 
top_frame.place_forget()
bottom_frame.place_forget()

root.resizable (0,0) # Root sizing 
root.iconbitmap('Media/Logo2.ico') # Logo for the Tkinter Window application 

# Working with the Image 
cat_img = Image.open("Media/Image2.png") # Inserting image 
cat_img = cat_img.resize((200, 200)) # Sizing the image width and height 
cat_img = ImageTk.PhotoImage(cat_img) # Calling the image so it will display

cat_label = Label(bottom_frame, image=cat_img, bg="#d1c2bb") # The image will now display in the home page 
cat_label.image = cat_img # Calls the image variable 
cat_label.place(relx=1.0, rely=1.0, anchor="se") # Positioning and anchoring to the bottom right corner, this was driven from ChatGPT
# End of Working with the Image 

file = open("Media/randomJokes.txt", "r") # This allows Python to open our txt file and read them 

jokes = file.readlines() # Reads the lines in the external file and store them in a list 
file.close() # Allows for the file to be closed 

setup = ""
punchline = ""

def startApp(): # Function 1: Starts the Program 
    welcome_frame.place_forget() # Temporarily removes Welcome Frame 

    top_frame.place(relx=0, rely=0, relwidth=1, relheight=0.5) # Displays Top Frame
    bottom_frame.place(relx=0, rely=0.5, relwidth=1, relheight=0.5) # Display Bottom Frame 

# Start Button displayed in Welcome Frame 
start_button = Button(welcome_frame, text="Start! ♡⋆˚꩜｡", font=("Arial Black", 18, "bold"), fg="#f1e2e8", bg="#d1c2bb", command=startApp)
start_button.place(relx=0.5, rely=0.65, anchor="center") 

def tellJoke(): # Function 2: Tells the Joke 
    global setup, punchline # Allows us to use the updated setup and punchline values from other functions 
    joke = random.choice(jokes) # Randomly selects 1 item from the Jokes list (comes from the text file)
    parts = joke.strip().split("?") # Strip removes whitespace and Split separates the joke from the punchline depending on where it finds the ? mark 

# Position and indexes 
    setup = parts[0] # Joke
    punchline = parts[1] # Punchline 

    setup_label.config(text=setup) # Modifies the existing properties of the widget (displays the joke)
    punchline_label.config(text="") # Allows to remove previous joke so that a new joke may appear 

def showPunchline(): # Function 3: Displays punchline 
    punchline_label.config(text=punchline) # Updates the existing punchline label and displays the punchline from the respective variable 

# Setup (joke line) label
setup_label = Label(top_frame, text="Ready for some good laughs? (˶>⩊<˶)", font=("Arial Black", 15, "bold"), fg="#d1c2bb", bg="#f1e2e8")
setup_label.place(relx=0.5, rely=0.2, anchor="center")

# Punchline label
punchline_label = Label(bottom_frame, text="", font=("Arial Black", 15, "bold"), fg="#f1e2e8", bg="#d1c2bb")
punchline_label.pack(pady=10)

# Buttons : Play Joke Button (to start a joke), Play Punchline Button (to display the punchline), Next Joke Button (to display a new joke), Quit Button (To close the Window)
# Place was use for a precise positioning and Pack was used for placing 

play_joke_button = Button(top_frame, text="Give me a joke! ♡", font=("Arial Black", 13, "bold"), fg="#f1e2e8", bg="#d1c2bb", command=tellJoke)
play_joke_button.place(relx=0.30, rely=0.65, anchor="center")

play_punchline_button = Button(top_frame, text="Show me the punchline! ♡", font=("Arial Black", 13, "bold"), fg="#f1e2e8", bg="#d1c2bb", command=showPunchline)
play_punchline_button.place(relx=0.65, rely=0.65, anchor="center")

next_joke_button = Button(bottom_frame, text="Next Joke ✿ ", font=("Arial Black", 12), bg="#f1e2e8", fg="#d1c2bb", command=tellJoke) 
next_joke_button.pack(pady=5)

quit_button = Button(bottom_frame, text="Exit ✿", font=("Arial Black", 12),  bg="#f1e2e8", fg="#d1c2bb", command=root.destroy)
quit_button.pack(pady=5)

root.mainloop() # Keeps the Window application running unless user decides to close it themselves 