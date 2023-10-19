#importa biblioteca smbus e time
import smbus2 as smbus
import time

#inicializa o smbus e define endereco do arduino
bus = smbus.SMBus(1)
slaveAddress = 0x08

#funcao para enviar dado para o arduino
def SendArduinoData(val): 
	bus.write_byte(slaveAddress,val)
	print("enviado")
		
#requisita continuamenta informacao ao usuario para enviar ao arduino    
while 1:
	val = int(input("Insira 1 para ligar e 0 para desligar o LED: "))
	SendArduinoData(val)
	time.sleep(0.25)
