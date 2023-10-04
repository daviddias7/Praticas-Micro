#David Felipe Santos e Souza Dias - 11800611
#Vinicius Santos Cubi Paulo - 11965693
from gpiozero import LED
from time import sleep


#instancia o LED
led = LED(4)
led.off()

#Loop de entrada de usuario
while(True):
	#Verifica se o tempo eh um numero e verifica se foi pressionado o ctrl+c
	try:
		tempo = int(input("Insira tempo da contagem (s): "))
	except KeyboardInterrupt:
		exit()
	except:
		print("O tempo inserido precisa ser um numero")
		continue
	#verifica se o tempo eh positivo, caso positivo inicia a contagem		
	if tempo >= 0:
		for i in range(tempo):
			t = tempo - i
			#formata a string para o formato adequado
			m,s = divmod(t,60)
			tStr = "\r" + f'{m :02d}' + ":" + f'{s :02d}'
			print(tStr, end="")
			#espera o tempo
			sleep(1)
			
		break
	else:		
		print("O numero inserido deve ser positivo")

m = 0
s = 0	
tStr = "\r" + f'{m :02d}' + ":" + f'{s :02d}'
print(tStr)

#mantem LED ligado
print("Fim logico")
try:
	while True:
		led.on()
except KeyboardInterrupt:
	#caso o ctrl+c encerre o programa, libera a GPIO
	led.close()
	
