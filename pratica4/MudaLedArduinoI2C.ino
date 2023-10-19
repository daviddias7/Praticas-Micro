
//Importa biblioteca Wire
 #include "Wire.h"

 //Define endereco do arduino
 #define adress 0x08
 

short valor;
int ledPin = 13;


//Define pino
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to

int sensorValue = 0;        // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
  Wire.begin(adress);
  //Registra um evento para ser chamado quando chegar algum dado via I2C
  Wire.onReceive(receiveEvent);
  pinMode(ledPin,OUTPUT);
  
}


void receiveEvent(int howMany) {
  // verifica se existem dados para serem lidos no barramento I2C
  while(Wire.available()) {
    // le o byte recebido
    int received = (int) Wire.read();
    Serial.print("valor recebido: ");
    Serial.println(received1);

    
    // se o byte recebido for igual a 0, apaga o LED
    if (received == 0) {
      digitalWrite(ledPin, LOW);
    }

    // se o byte recebido for igual a 1 acende o LED
    if (received == 1) {
      digitalWrite(ledPin, HIGH);
    }
  }
}

  

void loop() {

  delay(50);
}
