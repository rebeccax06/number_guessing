import random as rand
from tkinter import *
import tkinter.messagebox

#makes the widget size 500x300, background:white, with title:Number Guessing Game
root = Tk()
root.geometry('500x300')
root['bg']='white'
root.title('Number Guessing Game')

#holds integer data
num = IntVar()

#generates a random number 1 through 100
def genAnswer():
  global answer
  answer = rand.randint(1,100)

#asks users if they want to play again. If they press no, it ends. Otherwise, a new answer is generated  
def confirm():
  playAgain = tkinter.messagebox.askyesno(title = 'Question', icon ='question', message = 'Do you want to play again?')
  if not playAgain:
    root.destroy()
  else: 
    genAnswer()

#checls the users guess and tells them if it is correct, too low, or too high
def numGuessing():
  #gets the input from the entrybox
  guess = num.get()
  #displays that it is too low
  if guess < answer:
    resultLabel.config(text = 'Incorrect. Too Low.',fg = 'red',bg = 'white')
   #calls function again if entry in box changes
    if guess != num.get():
       
     root.after(1000, numGuessing)
   #displays that guess is too high    
  elif guess > answer:
    resultLabel.config(text = 'Incorrect. Too High.',fg = 'red',bg = 'white')
       #calls function again if entry in box changes
    if guess != num.get():
        
      root.after(1000, numGuessing)
  elif guess == answer:
    #displays that guess is right
    resultLabel.config(text = 'Congrats! You guessed the right number.',fg = 'green',bg = 'white')
    #after 2.5 seconds, calls on confirm function
    root.after(2500,confirm)
     

#returns true if input is a digit/no input and false if it isn't
def callback(input):
  if input.isdigit():
    print(input)
    return True
                        
  elif input == "":
    print(input)
    return True

  else:
    print(input)
    return False

#generates an answer at the beginning
genAnswer()

#The register() method returns a string which is assigned to a variable ‘reg’ that is used to call the callback function in the later stages.
reg = root.register(callback)

#title label
title_label = Label(root, text="Number Guessing Game",
fg="Navy Blue", font=("Consolas", 20, ),bg = 'white').pack()

#label for number entry
num_entry_label = Label(root, text = 'Guess A Number 1-100', bg = 'white', fg = 'Navy Blue',font = ('Consolas', 15)).pack(pady = 5)
#entry box
#validate is used to specify when the callback function will be called to validate the input. he “key” value specifies that validation occurs whenever any keystroke changes the widget’s contents.
#validate command is used to specify the callback function.
#%P means the value that the text will have if the change is allowed.
num_entry = Entry(root,textvariable=num,width=30,validate ="key", validatecommand =(reg, '%P')).pack(pady = 5)

#button; calls the numGuessing function when clicked
btn = Button(root, text="Guess",fg="white", bg = 'light grey', font=("Consolas", 10, 'bold') ,command=numGuessing).pack(pady = 5)

#label that tells user whether their answer is correct, too high, or too low
resultLabel = Label(root, text ='', font = ('Consolas', 14,'italic'),bg = 'white')
resultLabel.pack(pady = 5)


  
#calls the main loop
root.mainloop()

