"""
Description: Ruleta rusa
Autor: Ethan Yahel Sarricolea Cortés
"""

import random
import time

pos = random.randint(1,6)

tiros=0

class Revolver():
    def __init__(self):
        self.vivo=True
        self._charger = 6
        self.__bulletSpace = 0
        self.terminal = Terminal()

    def rotate_charger(self,pos):
        if self.vivo:
            self.__bulletSpace = random.randint(1,6)
            self.terminal.clear_line(self.terminal.textos[1])
            time.sleep(5)
            if pos == self.__bulletSpace:
                self.terminal.clear_line(self.terminal.textos[2])
                time.sleep(2)
                self.vivo= False
            else:
                self.terminal.clear_line(self.terminal.textos[3])
                time.sleep(2)
        else:
            pass

class Terminal():
    def __init__(self):
        self.texto_anterior:str
        self.textos = ["Presiona una tecla para continuar... ","Giro...",
                       "¡Bang! Haz muerto","No paso nada"]

    def play(self):
        print(input(self.textos[0]))
        self.texto_anterior=self.textos[0]

    def clear_line(self,text):
        if len(self.texto_anterior)>len(text):
            espacio = (len(self.texto_anterior)-len(text))
            print("\b"*len(self.texto_anterior), end='', flush=True)
            print(text+(" "*espacio), end='', flush=True)
        else:
            print("\b"*len(self.texto_anterior), end='', flush=True)
            print(text, end='', flush=True)

# Comienzo del juego

arma = Revolver()

print(f"Tu numero de la suerte es: {pos}")
arma.terminal.play()

for i in range(arma._charger):
    if arma.vivo:
        arma.rotate_charger(pos)
        tiros+=1
        continue
    else:
        break
print()
print("¡¡Sobreviviste!!" if arma.vivo else f"El {tiros} tiro te mato...")
