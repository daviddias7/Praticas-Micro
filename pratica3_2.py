from gpiozero import MotionSensor, PWMLED
#importa as classes
from signal import pause #a função pause é importada do módulo signal para manter o programa em execução indefinidamente e responder a eventos enquanto aguarda uma interrupção

pir = MotionSensor(4) #cria um objeto pir que representa o sensor de movimento (PIR) na GPIO 4

led = PWMLED(21) # objeto LED na GPIO 16

def ledBaixo():
	led.value = 0.1
	
def ledAlto():
	led.value = 1

pir.when_motion = ledAlto # ação para ser executada quando o sensor de movimento detecta movimento - liga o LED

pir.when_no_motion = ledBaixo # caso contrário

pause() # aguarda novos eventos
