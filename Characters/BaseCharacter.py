class BaseCharacter:
# loacal variables of parent character class
    Attack = 0
    HP = 0 
    Deffence = 0
    Speed = 0
    EffectHitRate = 0
    EffectRessistance = 0
    DamageBonusType = "N/A"
    DamageBonusPercent = 0

    def setAttack(number):
        #sett the base Attack value of a unit
        Attack = number
    
    def getAttack():
        #returns the attack value of a unit
        return Attack
    
    def setHP(number):
        HP = number
    
    def getHP():
        return  HP
    
    def setDeffence(number):
        Deffence = number

    def getDeffence():
        return Deffence

    def setSpeed(number):
        seed = number
    
    def getSpeed():
        return speed
    
    def setEffectHitRate(number):
        EffectHitRate = number
    
    def getEffectHitRate():
        return EffectHitRate
    
    def setEffectRessistance(number):
        EffectRessistance = number

    def getEffectRessistance():
        return EffectRessistance
    
    
    