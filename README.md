# Pratica-Micro

## Prática 1

Nessa prática, instalamos uma distribuição linux na raspberry. Foi utilizado um notebook próprio junto ao raspberry imager para a instalação.

Após a instalação, foram realizadas as configurações iniciais e testado o SSH e o VNC através do notebook. Esses são programas de acesso remoto à raspberry. O ssh dá acesso ao terminal somente, e o VNC permite a toda a área de trabalho gráfica.

Então, foram executados os comandos neofetch e pinout e foi extraído o histórico de comandos do terminal. O comando neofetch permite observar a distribuição e versão do sistema operacional. O comando pinout permite observar o layout dos pinos da raspberry.

## Prática 2

Na prática 2, inicialmente instalamos o python-env, que permite a criação de ambientes virtuais para a programação em python. Após isso, criamos um ambiente virtual para trabalharmos e, neste ambiente, instalamos as bibliotecas gpiozero e RPi.GPIO. Ambas as bibliotecas são para a programação dos pinos da raspberry, sendo a primeira em mais alto nível que a segunda. Assim sendo, fizemos dois programas:

### Led Blink
Em ambas as bibliotecas, fizemos um código que pisca um LED em um intervalo de tempo definido no código.

### Botão
Na biblioteca RPi.GPIO, fizemos um código que imprime no terminal quando um botão ligado a um pino for pressionado e solto.

### Timer
Usando a biblioteca gpiozero, fizemos um código em que um usuário insere um valor númerico no terminal e começa a contar esse tempo. Quando o tempo terminar, acende-se um LED. Esse código encontra-se na pasta pratica2.


## Prática 3

Nessa prática, visamos usar periféricos na programação da raspberry. O uso de periféricos na raspberry é uma de suas grandes vantagens, em comparação com sistemas computacionais normais, visto que o facil acesso aos GPIO's da placa facilita a integração de sensores e de sistemas que se comunicam com protocólos distintos. Portanto, fizemos três códigos:

### PWM
Escolhemos um dos pinos e fizemos um PWM simples nesse para um LED conectado a esse pino. Esse PWM aumenta a largura da onda em loop, aumentando a intensidade da luz (a cada 0,1 segundos) conforme o tempo. É usada a biblioteca gpiozero.

### Sensor de Movimento
Utilizando-se o sensor de movimento, foi desenvolvido um código no qual quando o sensor detecta alguma movimentação, ele coloca o PWM do LED e quando não detecta movimento, o deixa em 10% da potência. É usada a biblioteca gpiozero.

### Sensor de Temperatura e Umidade
Utilizando o sensor DHT11 junto as bibliotecas RPi.GPIO e Adafruit_DHT foi possível realizar a medição de temperatura e umidade do sensor e imprimir no terminal esses valores.
