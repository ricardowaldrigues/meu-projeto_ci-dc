try:
    from machine import Pin
except ImportError:
    # Mock para simular os pinos GPIO dentro do container Linux
    class Pin:
        OUT = 1
        IN = 0
        def __init__(self, pin_number, mode):
            self.pin_number = pin_number
        def value(self, val=None):
            if val is not None:
                print(f"[SIMULAÇÃO DOCKER] Pino GPIO {self.pin_number} setado para {val}")
            return 0

# Exemplo do restante da sua lógica
led = Pin(2, Pin.OUT)
led.value(1)
print("Execução finalizada no ambiente simulado!")