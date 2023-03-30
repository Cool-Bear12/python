import random
import playsound
class Musicbox:
    def __init__(self):
       self.variants = "kozv" # Варианты звуков
       self.score =0
       self.sequence- random.choice(self.variants)# последовательность
    def __next(self):
        dlina = len(self.sequence)+1
        self.sequence = ""
        for _ in range(dlina)
            self.sequence += random.choice(self.variants)
    def proverit(self,otvet):
        if otvet == self.sequence:
            playsound.playsound("sounds/corrct.way")
            self.__sledushiy()
            self.score +=1
        else:
            playsound.playsound("sounds/incorrect.way")
            self.score -= 1
    def igraen(self):
        for letter in seunce:
            playsound.playsound(f"sounds/.mp3")
