'''
Created on 9 Nov 2018

@author: seanv
'''
import serial
from model import serialSettings as settings
from model import rolluik as sesam

def getUltrasoonArduino(rolluik):
    comport=settings.rolluikDict.get(rolluik)
    serial = serial.Serial(comport= comport, baudrate = settings.baudrate, timeout = settings.timeout)
    serial.write(b'd') #Moet ook licht zijn in C-code
    temperatuur = serial.read() #of readline().decode('ascii') als er ascii gebruikt is =)
    return temperatuur

def getUltrasoon(rolluik):
    return settings.temp[rolluik-1]

def updateUltrasoon(rolluik):
    settings.temp[rolluik-1] = getUltrasoonArduino(rolluik)