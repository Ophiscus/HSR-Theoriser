from tkinter import *
import sys

from Characters.Kafka import Kafka

class Main:
    sys.path.insert(0, '.\Characters')

    def displayStats(name):
        match name :
            case "Kafka":
                print ("kafka input recognised")
                Kafka.Display()
            

    # ---------------------------- UI SETUP ------------------------------- #
    # New tkinter Window
    window = Tk()
    window.title("HSR Dreaemr")
    window.config(padx=20, pady=20,background='black')

    

    #create a button that will load the Kafka stats when clicked uppon
    # Creating a photoimage object to use image 
    photo = PhotoImage(file = r".\Images\Logo\Kafka Logo.png") 
    KafkaButton = Button(window, text="Kafka" , image= photo, command = displayStats("Kafka"))
    KafkaButton.grid(column = 0 ,row = 0)

    window.mainloop()