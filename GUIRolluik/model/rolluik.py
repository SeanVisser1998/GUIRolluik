'''
Created on 4 Nov 2018

@author: seanv
'''
import serial
import serial.tools.list_ports as list_ports
from model import serialSettings as settings

#Scan voor rolluik

scannedPorts = ['COM4']
def scanCOM():
    scannedPorts.append(list_ports.comports())
    

#Rolluik identificeren
ID_COM = {}

def getID():
    ID_COM.clear() #Leegt de dictionary eersts

    for port in settings.rolluikPoort:
        daddy = serial.Serial(comport=port, baudrate=settings.baudrate, timeout= settings.timeout)
        daddy.Write(b'e')
        ID = daddy.readline.decode('ascii')
        ID_COM[ID] = port #Vogt port toe aan ID_COM als waarde van ID(ID:COM)

def getCOM(ID):
    return ID_COM.value.get(ID)

# Status opvragen enzo

def getStatus(rolluiknummer):
    comport = settings.rolluikDict.get(rolluiknummer) #-1 omdat eenheid 1 is index 0
    daddy = serial.Serial(comport=comport, baudrate = settings.baudrate, timeout = settings.timeout)
    daddy.Write(b'hihi') #moet ook 'hihi' zijn in C om rolluik status op te vragen
    status = daddy.readline.decode('ascii')
    if status == 1:
        return 'open' 
    else:
        return 'dicht'

# Open / sluit shizle
def sluitAlle():
    for comport in settings.rolluikDict.values():
        daddy = serial.Serial(comport = comport, baudrate = settings.baudrate, timeout = settings.timeout)
        daddy.write(b'g') #moet ook 'sluit' zijn in C om rolluik te sluiten
    
    for rolluik in range(len(settings.rolluikNaam)):
        settings.status[rolluik] = 'red'

def openAlle():
    for comport in settings.rolluikDict.values():
        daddy = serial.Serial(comport = comport, baudrate = settings.baudrate, timeout = settings.timeout)
        daddy.write(b'h') #moet ook 'open' zijn in C om rolluik te openen

def sluitRolluik(rolluiknummer):
    comport = settings.rolluikDict.get(rolluiknummer)
    daddy = serial.Serial(comport=comport, baudrate = settings.baudrate, timeout = settings.timeout)
    daddy.Write(b'g') #moet ook 'sluit' zijn in C om rolluik te sluiten
    settings.status[rolluiknummer] = 'red'

def openRolluik(rolluiknummer):
    comport = settings.rolluikDict.get(rolluiknummer)
    daddy = serial.Serial(comport=comport, baudrate = settings.baudrate, timeout = settings.timeout)
    daddy.Write(b'h') #moet ook 'open' zijn in C om rolluik te openen
    settings.status[rolluiknummer] = 'green'
    