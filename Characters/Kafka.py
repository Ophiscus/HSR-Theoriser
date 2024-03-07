from Characters.BaseCharacter import BaseCharacter
from tkinter import *

#general layout for an actual character
class Kafka(BaseCharacter):
    Level = 1
    maxLevel = 80
    def __init__(self) :
        setAttack(92)
        setHP(147) 
        setDeffence(66)
        setSpeed(100)
        DamageBonusType = "Lightning"

    #code for the incremental level up
    def LevelUp():
        HP += 7.5
        Attack += 4.5
        Deffence += 3

    #code for one acension stat    
    def Ascend():
        HP += 59
        Attack += 37
        Deffence += 27

    #code to have the stats show on screen when the button is pressed
    def Display():
        #basic frame to hold all the data in
        kafkaFrame= Frame()

        #Basic stats
        unitsHP = Label(text="HP")
        unitsHP.grid(kafkaFrame,column=0,row=0)
        enterHp = Entry(width=500)
        enterHp.grid(kafkaFrame,column=1,row=0)

        unitsAttack = Label(text="Attack")
        unitsAttack.grid(kafkaFrame,column=0,row=1)
        enterAttack = Entry(width=500)
        enterAttack.grid(kafkaFrame,column=1,row=1)

        unitsDefence = Label(text="Defence")
        unitsDefence.grid(kafkaFrame,column=0,row=2)
        enterDefence = Entry(width=500)
        enterDefence.grid(kafkaFrame,column=1,row=2)

        unitsSpeed = Label(text="Speed")
        unitsSpeed.grid(kafkaFrame,column=0,row=3)
        enterSpeed = Entry(width=500)
        enterSpeed.grid(kafkaFrame,column=1,row=3)

        #other stats
        unitsCritRate = Label(text="CritRate")
        unitsCritRate.grid(kafkaFrame,column=0,row=4)
        enterCritRate = Entry(width=500)
        enterCritRate.grid(kafkaFrame,column=1,row=4)

        unitsCritDamage = Label(text="CritDamage")
        unitsCritDamage.grid(kafkaFrame,column=0,row=5)
        enterCritDamage = Entry(width=500)
        enterCritDamage.grid(kafkaFrame,column=1,row=5)

        unitsEffectHitRate = Label(text="Effect Hit Rate")
        unitsEffectHitRate.grid(kafkaFrame,column=0,row=6)
        enterEffectHitRate = Entry(width=500)
        enterEffectHitRate.grid(kafkaFrame,column=1,row=6)

        unitsEffectRessistance = Label(text="Effect Ressistance")
        unitsEffectRessistance.grid(kafkaFrame,column=0,row=7)
        enterEffectRessistance = Entry(width=500)
        enterEffectRessistance.grid(kafkaFrame,column=1,row=7)

        kafkaFrame.pack()
    
        
    
    