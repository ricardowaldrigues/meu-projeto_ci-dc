import unittest

# Funções de teste para o projeto do LED
def ligar_led():
    return True

def desligar_led():
    return False

def calcular_resistor(tensao, corrente):
    if corrente == 0:
        raise ValueError("Corrente não pode ser zero")
    return tensao / corrente

def status_led(estado):
    return "LIGADO" if estado else "DESLIGADO"

def eh_tensao_valida(tensao):
    return 0 <= tensao <= 12


class TesteLed(unittest.TestCase):

    def test_1_ligar_led(self):
        self.assertTrue(ligar_led())

    def test_2_desligar_led(self):
        self.assertFalse(desligar_led())

    def test_3_calcular_resistor(self):
        self.assertEqual(calcular_resistor(5, 0.02), 250)

    def test_4_status_led(self):
        self.assertEqual(status_led(True), "LIGADO")

    def test_5_tensao_valida(self):
        self.assertTrue(eh_tensao_valida(5))
        self.assertFalse(eh_tensao_valida(15))


if __name__ == '__main__':
    unittest.main()
