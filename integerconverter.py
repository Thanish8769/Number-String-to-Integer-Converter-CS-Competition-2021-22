import tkinter as tk
from tkinter import ttk
from tkinter.constants import COMMAND
from typing import Text
from PIL import Image, ImageSequence, ImageTk
from googletrans.constants import LANGUAGES
import inflect
from googletrans import Translator
from tkinter.ttk import * 
import textblob
import pyttsx3
import sys, time 




root = tk.Tk()

#Makes the title of the application say INTEGER CONVERTER
root.title('INTEGER CONVERTER | By The Brute Force')

#Sets the size to 1280x720
root.geometry("1280x720")

root.iconbitmap('tyler.ico')

#Makes the background as an image
back = tk.PhotoImage(file="number.png")
backLabel = tk.Label(root, image=back)
backLabel.place(x=0, y=0, relwidth=1, relheight=1,)

#The Title saying 'INTEGER CONVERTER'
titleText = tk.Label(root, text="INTEGER CONVERTER")
titleText.config(font= ("Wrong Delivery", 50), bg="black", fg="white",)
titleText.pack()

#The subtext saying 'By: The Brute Force'
subText = tk.Label(root, text="BY THE BRUTE FORCE")
subText.config(font= ("Wrong Delivery", 15), bg="black", fg="white")
subText.pack()

#Another subtext saying 'Enter number below'
subText2 = tk.Label(root, text="ENTER NUMBER BELOW")
subText2.config(font= ("Wrong Delivery", 15), bg="black", fg="white")
subText2.pack(pady=50)

#Box where you input your values
inputBox = tk.Entry(root, bg = "white", fg="black", font =("Wrong Delivery", 30),)
inputBox.place(width=100, height=100)
inputBox.pack()

#Gets the languages from the googletrans package
languages = LANGUAGES
languageList = list(languages.values())



def helpBox():
    tk.messagebox.showinfo(title="Help", message="Are you stupid? Do you not know how to use this, you go to a grammar school. Anyways, if you are a rich person please enter your credit card details 👍")




def numberConverter():  
    global textBlobWords
    global languages
    global word
    global result
    
    converter = inflect.engine()
    number = inputBox.get()
    word = converter.number_to_words(number)
    
   
    
    #Checks if the input is a number or not
    try:
        float(number)
        
        
        result.config(font=("Wrong Delivery", 30), bg="black", fg="white", text=word.upper(), wraplength=700,  justify="center")
       

    except ValueError:
       
        result.config(font=("Wrong Delivery", 30), bg="black", fg="white", text="PLEASE ENTER A NUMBER!")
        
    #The translator
    try:
        #We can't use the name of the language to translate it to it so we must get the key
        for key, value in languages.items():
            if (value == languageCombo.get()):
                toLanguageKey = key
        
        #print(toLanguageKey)
        
        textBlobWords = textblob.TextBlob(word)

        textBlobWords = textBlobWords.translate(from_lang = 'en' , to = toLanguageKey)

        result.config(font=("Wrong Delivery", 30), bg="black", fg="white", text=textBlobWords.upper())
    
        
        #engine = pyttsx3.init()

        #engine.say(textBlobWords)
    
        #engine.runAndWait()

    except Exception as e:
        print('')
        

def speech():
   
    try:

        engine = pyttsx3.init()

        engine.say(textBlobWords)
    
        engine.runAndWait()

    except NameError:
        tk.messagebox.showerror(title="Are you dumb?", message="I can't translate from text to speech when there is no output, dumb guy smh.")

speakerImage = Image.open('speaker.png')

resized = speakerImage.resize((20, 20), Image.ANTIALIAS)

newSpeakerImage = ImageTk.PhotoImage(resized)

speakerButton = Button(root, image=newSpeakerImage, command=speech)
speakerButton.place(x=710, y=403)

#The Convert Button
enterButton = tk.Button(root, font=("Wrong Delivery", 20 ), text="CONVERT!", command=numberConverter, borderwidth=0)
enterButton.pack(pady=30)

#Label that says output
output = tk.Label(root, text='OUTPUT ', font=("Wrong Delivery", 20), bg="black", fg="white")
output.pack()

#'Invisible' Label that will show the results
result = tk.Label(root, text='', bg ="black")
result.pack(pady=20)

#Label that is just a little heading for the language
languageChoice = tk.Label(root, text='CHOOSE LANGUAGE', font=("Wrong Delivery", 15), bg="black", fg="white")
languageChoice.place(x=20, y=630)

#Button to click when you need help 
helpButton = tk.Button(root, font=("Wrong Delivery", 15), text="HELP", command=helpBox, borderwidth=0)
helpButton.place(x=1180, y= 640 )

#Combo box of the languages
languageCombo = Combobox(root, width=50, value=languageList)
languageCombo.current(21)
languageCombo.place(x=20, y= 660)
theLanguage = languageCombo.get() #Gets the value of the current langauge of the combobox


#Stops resizing the gui cos that just annoying an ugly if you resize it
root.resizable(False,False) 

root.mainloop()

