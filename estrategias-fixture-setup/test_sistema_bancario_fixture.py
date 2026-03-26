import unittest

from dinheiro import Dinheiro, Moeda
from operacao import EstadosDeOperacao
from sistema_bancario import SistemaBancario

class TestOperacoesComFixtureContaBRL(unittest.TestCase):
    # Implicit Setup
    def setUp(self):
        self.sistema = SistemaBancario()
        self.banco = self.sistema.criar_banco("Caixa Econômica", Moeda.BRL)
        self.agencia = self.banco.criar_agencia("Centro")
        self.conta = self.agencia.criar_conta("Marcelo")

    def test_inline_deposito_valido_em_conta_brl_retorna_sucesso(self):
        # Estratégia: Implicit Setup
        # Fixture Setup

        # Exercise SUT
        operacao_deposito = self.sistema.depositar(self.conta, Dinheiro(Moeda.BRL, 12, 30))

        # Result Verification
        self.assertEqual(EstadosDeOperacao.SUCESSO, operacao_deposito.obter_estado())

        # Fixture Teardown

    def test_inline_saque_sem_saldo_em_conta_brl_retorna_saldo_insuficiente(self):
        # Estratégia: Implicit Setup
        # Fixture Setup

        # Exercise SUT
        operacao_saque = self.sistema.sacar(self.conta, Dinheiro(Moeda.BRL, 1, 0))

        # Result Verification
        self.assertEqual(EstadosDeOperacao.SALDO_INSUFICIENTE, operacao_saque.obter_estado())

        # Fixture Teardown

    def test_inline_transferencia_sucesso_move_valor_entre_contas(self):
        # Estratégia: Implicit Setup & Inline Setup
        # Fixture Setup
        conta_destino = self.agencia.criar_conta("Rafael")
        self.sistema.depositar(self.conta, Dinheiro(Moeda.BRL, 100, 0))

        # Exercise SUT
        self.sistema.transferir(self.conta, conta_destino, Dinheiro(Moeda.BRL, 15, 0))

        # Result Verification
        saldo_destino = conta_destino.calcular_saldo()
        self.assertEqual("+15,00 BRL", saldo_destino.formatado())

        # Fixture Teardown
