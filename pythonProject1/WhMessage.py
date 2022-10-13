import pywhatkit
from flask import Flask

def message(numero,mes,ora,min):
    pywhatkit.sendwhatmsg(numero,mes, ora, min)