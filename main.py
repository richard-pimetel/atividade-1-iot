from machine import Pin
from utime import sleep


led_verde = Pin(16, Pin.OUT)
led_amarelo = Pin(17, Pin.OUT)
led_vermelho = Pin(18, Pin.OUT)


TEMPO_VERDE = 20
TEMPO_AMARELO = 10
TEMPO_VERMELHO = 7
SLEEP_ENTRE_CORES = 0.5

print("Iniciando Semáforo...")

while True:

    led_verde.on()
    print(f"VERDE - Ligado por 20 segundos")
    sleep(20)
    led_verde.off() 
    sleep(0.5)


    
    led_amarelo.on()
    print(f"AMARELO - Ligado por 10 segundos")
    sleep(10)
    led_amarelo.off() 
    sleep(0.5)

  
    
    led_vermelho.on()
    print(f"VERMELHO - Ligado por 7 segundos")
    sleep(7)
    led_vermelho.off() 
    sleep(0.5)