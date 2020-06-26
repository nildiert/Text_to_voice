#!/usr/bin/env python3
from gtts import gTTS 
import os
import sys


try:
    language = 'es'
    file = open(sys.argv[1], "r").read().replace("\n", " ")
    speech = gTTS(text = str(file), lang = language, slow = False)
    mp3filename = "{}.mp3".format(sys.argv[2])
    speech.save(mp3filename)
    command = "mv {} ./".format(mp3filename)
    os.system(command)

except Exception as err:
    print(err)
    print("Coloca un argumento.\n")
    print("Ejemplo:")
    print("\tvoice example.txt mp3filename")
    print("El primer argumento es el archivo de texto y el segundo es el nombre del archivo mp3")

