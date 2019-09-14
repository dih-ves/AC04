from unittest import TestCase
from com.Farina.operacoes import Operacoes

class TestOperacoes(TestCase):
	def setUp(self):
		self.operacoes = Operacoes()
	def test_some(self):
		self.assertEqual(self.operacoes.soma([1,5]),6, "Should be 6")
