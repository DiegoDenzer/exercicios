from unittest import TestCase
from src.diversos.romeu_julieta import romeu_julieta


class TesteRomeJulieta(TestCase):

    def teste_rj_responde_queijo(self):
        valor_entrada = 3
        valor_saida = 'Queijo'
        self.assertEqual(romeu_julieta(valor_entrada), valor_saida)

    def teste_rj_responde_goiabada(self):
        valor_entrada = 5
        valor_saida = 'Goiabada'
        self.assertEqual(romeu_julieta(valor_entrada), valor_saida)

    def teste_rj_responde_romeu_e_julieta(self):
        valor_entrada = 15
        valor_saida = 'Romeu e Julieta'
        self.assertEqual(romeu_julieta(valor_entrada), valor_saida)