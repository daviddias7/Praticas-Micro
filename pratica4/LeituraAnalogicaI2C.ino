

 #include "Wire.h"

//Endereco i2c do arduino
 #define adress 0x08
 
short valor;



//Pino analogico
const int analogInPin = A0;  // Entrada analogica


void setup() {
  //Inicializa comunicacao serial
  Serial.begin(9600);
	
  //Inicializa comunicacao i2c
  Wire.begin(adress);
  
  //Declara a interrupcao por evento de requisicao i2c
  Wire.onRequest(requestEvent);

  
}

/*Quando a requisicao eh recebida faz leitura do potenciometro,
mapeia o valor para um range de 0 a 255  e envia o valor por i2c para a raspberry pi
tambem faz a impressao no terminal serial do arduino conectado ao computador*/
void requestEvent()
{
  valor = analogRead(A0);
  valor = map(valor, 0 ,1023,0,255);
  Wire.write(valor);
  Serial.print("Requisicao recebida: ");
  Serial.println(valor);
}


void loop() {

  delay(50);
}
