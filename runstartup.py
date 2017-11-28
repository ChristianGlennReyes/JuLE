import serial
import json
import requests

url = 'http://192.168.100.151:8000/getArdData/'

data = serial.Serial('/dev/ttyUSB0', baudrate=9600)

while(True):
    jason = data.readline()[:-2].decode('utf-8')
    ardData = {'ardData': jason}
    req = requests.post(url, ardData)
    print(jason)
