# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 22:33:10 2021
@author: D4ITON
@email: dalthonmh@gmail.com
@licence: MIT
@url: https://github.com/D4ITON/apagado.git
"""

import os

print("""
      Programa el apagado del equipo
      ------------------------------
¿En cuánto tiempo deseas apagar el equipo? especifica
agregando s = segundos, m = minutos y h horas
ejemplo: 20s | 15m | 1h
""")
time = input("> ")
time_number = int(time[:-1])
time_code = time[-1]


def show_time_code_in_words(time_code = ""):
    if time_code == "s":
        return "segundos"
    elif time_code == "m":
        return "minutos"
    elif time_code == "h":
        return "horas"
    else:
        return "desconocido"

time_code_name = show_time_code_in_words(time_code)

def calculate_time_number_in_secods(time_number = 0, time_code = ""):
    if time_code == "s":
        return time_number
    elif time_code == "m":
        return time_number * 60
    elif time_code == "h":
        return time_number * 60 * 60
    else:
        return False

time_in_seconds = calculate_time_number_in_secods(time_number, time_code)

os.system("cmd /c shutdown -s -t {}".format(time_in_seconds))
print("el sistema se apagará en {} {}".format(time_number, time_code_name))
is_cancel = input("Si quieres cancelar el apagado puedes escribir 'cancelar'. ")

if is_cancel == "cancelar":
    os.system("cmd /c shutdown -a")
    

