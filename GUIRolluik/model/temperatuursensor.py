'''
Created on 4 Nov 2018

@author: seanv
'''
import serial
from model import serialSettings as settings
from model import rolluik as sesam

def getTemperatuurArduino(rolluik):
    comport=settings.rolluikDict.get(rolluik)
    serial = serial.Serial(comport= comport, baudrate = settings.baudrate, timeout = settings.timeout)
    serial.write(b't') #Moet ook licht zijn in C-code
    temperatuur = serial.read() #of readline().decode('ascii') als er ascii gebruikt is =)
    return temperatuur

def getTemperatuur(rolluik):
    return settings.temp[rolluik-1]

def updateTemperatuur(rolluik):
    settings.temp[rolluik-1] = getTemperatuurArduino(rolluik)
    
def setTemperatuur(rolluik, temperatuur):
    settings.temp[rolluik-1] = temperatuur
    if(int(temperatuur) > settings.maxTemp):
        sesam.sluitRolluik(int(rolluik))
    else:
        sesam.openRolluik(int(rolluik))