#Importa bibliotecas
import smbus2 as smbus
import time

#Inicia SMbus
bus = smbus.SMBus(1)

#Define endereço do arduino
slaveAddress = 0x08

#Funcao que faz o request dos valores do arduino
def RequestArduinoData(): 
	#le valor do arduino
	data_received_Arduino = bus.read_byte ( slaveAddress)
	print(data_received_Arduino)
		
    
while 1:
	#Requisita valor do arduino e aguarda 250ms
	RequestArduinoData() 
	time.sleep(0.25)

