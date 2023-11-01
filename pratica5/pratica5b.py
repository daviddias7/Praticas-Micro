
# Para descobrir qual a codificação da Tag com texto gravado anteriormente
from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO
from gpiozero import LED
#desabilitar os avisos
GPIO.setwarnings(False)

#Define os LEDS
led_vermelho = LED(26)
led_verde = LED(19)

#cria o objeto "leitor" para a instância "SimpleMFRC522" da biblioteca
leitor = SimpleMFRC522()
print("Aproxime a tag do leitor para leitura.")
while True: #loop
#cria as variáveis "id" e "texto", e as atribui as leituras da id e do texto coletado da tag pelo leitor, respectivamenteid,
	ident, texto = leitor.read()
	print("ID: {}\nTexto: {}".format(ident, texto)) #exibe as informações coletadas
	if(ident == 497386497680):
		print("Acesso Liberado")
		led_verde.on()
	else:
		print("Acesso Negado")
		led_vermelho.on()
		
	sleep(3) #aguarda 3 segundos para nova leitura
	led_verde.off()
	led_vermelho.off()
