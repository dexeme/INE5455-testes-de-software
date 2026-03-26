import unittest

from dinheiro import Dinheiro, Moeda
from operacao import EstadosDeOperacao
from sistema_bancario import SistemaBancario

class TestDepositosPorFeature(unittest.TestCase):
    # Implicit Setup
    def setUp(self):
        self.sistema = SistemaBancario()
        self.banco = self.sistema.criar_banco("Caixa Econômica", Moeda.BRL)
        self.agencia = self.banco.criar_agencia("Centro")
        self.conta = self.agencia.criar_conta("Marcio")

    def test_deposito_em_reais_retorna_sucesso(self):
        # Estratégia: Implicit Setup & Inline Setup
        # Fixture Setup
        quantia = Dinheiro(Moeda.BRL, 100, 0)

        # Exercise SUT
        operacao_deposito = self.sistema.depositar(self.conta, quantia)

        # Result Verification
        self.assertEqual(EstadosDeOperacao.SUCESSO, operacao_deposito.obter_estado())

        # Fixture Teardown

    def test_deposito_em_moeda_diferente_retorna_moeda_invalida(self):
        # Estratégia: Implicit Setup & Inline Setup
        # Fixture Setup
        quantia = Dinheiro(Moeda.USD, 10, 0)

        # Exercise SUT
        operacao_deposito = self.sistema.depositar(self.conta, quantia)

        # Result Verification
        self.assertEqual(EstadosDeOperacao.MOEDA_INVALIDA, operacao_deposito.obter_estado())

        # Fixture Teardown

    def test_deposito_com_quantia_zero_retorna_saldo_insuficiente(self):
        # Estratégia: Implicit Setup & Inline Setup
        # Fixture Setup
        quantia = Dinheiro(Moeda.BRL, 0, 0)

        # Exercise SUT
        operacao_deposito = self.sistema.depositar(self.conta, quantia)

        # Result Verification
        self.assertEqual(EstadosDeOperacao.SALDO_INSUFICIENTE, operacao_deposito.obter_estado())

        # Fixture Teardown

    def test_deposito_valido_atualiza_saldo_da_conta(self):
        # Estratégia: Implicit Setup & Inline Setup
        # Fixture Setup
        quantia = Dinheiro(Moeda.BRL, 25, 50)

        # Exercise SUT
        self.sistema.depositar(self.conta, quantia)

        # Result Verification
        saldo = self.conta.calcular_saldo()
        self.assertEqual("+25,50 BRL", saldo.formatado())

        # Fixture Teardown

    def test_depositos_sequenciais_acumulam_saldo(self):
        # Estratégia: Implicit Setup & Inline Setup
        # Fixture Setup
        primeira_conta = Dinheiro(Moeda.BRL, 10, 0)
        segunda_conta = Dinheiro(Moeda.BRL, 5, 25)

        # Exercise SUT
        self.sistema.depositar(self.conta, primeira_conta)
        self.sistema.depositar(self.conta, segunda_conta)

        # Result Verification
        saldo = self.conta.calcular_saldo()
        self.assertEqual("+15,25 BRL", saldo.formatado())

        # Fixture Teardown

    def test_deposito_com_fracionado_maior_que_base_normaliza_valor(self):
        # Estratégia: Implicit Setup & Inline Setup
        # Fixture Setup
        quantia = Dinheiro(Moeda.BRL, 1, 250)

        # Exercise SUT
        self.sistema.depositar(self.conta, quantia)

        # Result Verification
        saldo = self.conta.calcular_saldo()
        self.assertEqual("+3,50 BRL", saldo.formatado())

        # Fixture Teardown

class TestSaquesPorFeature(unittest.TestCase):
    # Implicit Setup
    def setUp(self):
        self.sistema = SistemaBancario()
        self.banco = self.sistema.criar_banco("Banco do Brasil", Moeda.BRL)
        self.agencia = self.banco.criar_agencia("Sul")
        self.conta = self.agencia.criar_conta("Rafael")

    def test_saque_com_saldo_suficiente_retorna_sucesso(self):
        # Estratégia: Implicit Setup & Inline Setup
        # Fixture Setup
        quantia_saque = Dinheiro(Moeda.BRL, 40, 0)
        self.sistema.depositar(self.conta, Dinheiro(Moeda.BRL, 100, 0))

        # Exercise SUT
        operacao_saque = self.sistema.sacar(self.conta, quantia_saque)

        # Result Verification
        self.assertEqual(EstadosDeOperacao.SUCESSO, operacao_saque.obter_estado())

        # Fixture Teardown

    def test_saque_maior_que_saldo_retorna_saldo_insuficiente(self):
        # Estratégia: Implicit Setup & Inline Setup
        # Fixture Setup
        self.sistema.depositar(self.conta, Dinheiro(Moeda.BRL, 20, 0))
        quantia_saque = Dinheiro(Moeda.BRL, 50, 0)

        # Exercise SUT
        operacao_saque = self.sistema.sacar(self.conta, quantia_saque)

        # Result Verification
        self.assertEqual(EstadosDeOperacao.SALDO_INSUFICIENTE, operacao_saque.obter_estado())

        # Fixture Teardown

    def test_saque_em_moeda_diferente_retorna_moeda_invalida(self):
        # Estratégia: Implicit Setup & Inline Setup
        # Fixture Setup
        self.sistema.depositar(self.conta, Dinheiro(Moeda.BRL, 20, 0))
        quantia_saque = Dinheiro(Moeda.USD, 10, 0)

        # Exercise SUT
        operacao_saque = self.sistema.sacar(self.conta, quantia_saque)

        # Result Verification
        self.assertEqual(EstadosDeOperacao.MOEDA_INVALIDA, operacao_saque.obter_estado())

        # Fixture Teardown

    def test_saque_reduz_o_saldo_quando_ha_sucesso_no_saque(self):
        # Estratégia: Implicit Setup & Inline Setup
        # Fixture Setup
        self.sistema.depositar(self.conta, Dinheiro(Moeda.BRL, 80, 0))
        self.sistema.sacar(self.conta, Dinheiro(Moeda.BRL, 30, 0))

        # Exercise SUT
        saldo = self.conta.calcular_saldo()

        # Result Verification
        self.assertEqual("+50,00 BRL", saldo.formatado())

        # Fixture Teardown

    def test_saque_nao_realizado_mantem_saldo_original(self):
        # Estratégia: Implicit Setup & Inline Setup
        # Fixture Setup
        self.sistema.depositar(self.conta, Dinheiro(Moeda.BRL, 35, 0))

        # Exercise SUT
        self.sistema.sacar(self.conta, Dinheiro(Moeda.BRL, 40, 0))

        # Result Verification
        saldo = self.conta.calcular_saldo()
        self.assertEqual("+35,00 BRL", saldo.formatado())

        # Fixture Teardown

    def test_saque_do_valor_total_zera_o_saldo(self):
        # Estratégia: Implicit Setup & Inline Setup
        # Fixture Setup
        self.sistema.depositar(self.conta, Dinheiro(Moeda.BRL, 70, 75))

        # Exercise SUT
        self.sistema.sacar(self.conta, Dinheiro(Moeda.BRL, 70, 75))

        # Result Verification
        saldo = self.conta.calcular_saldo()
        self.assertEqual("0,00", saldo.formatado())

        # Fixture Teardown

class ClasseAuxiliarCriaClassesOrigemDestino:
    def criar_classes_origem_destino(self):
        sistema = SistemaBancario()
        banco = sistema.criar_banco("Santander", Moeda.BRL)
        agencia = banco.criar_agencia("Norte")
        origem = agencia.criar_conta("Antônio")
        destino = agencia.criar_conta("Augusto")
        return sistema, origem, destino

class TestTransferenciasPorFeature(unittest.TestCase):

    def test_transferencia_com_saldo_suficiente_retorna_sucesso(self):
        # Estratégia: Delegated Setup & Inline Setup
        # Fixture Setup
        classe_auxiliar = ClasseAuxiliarCriaClassesOrigemDestino()
        sistema, origem, destino = classe_auxiliar.criar_classes_origem_destino()
        sistema.depositar(origem, Dinheiro(Moeda.BRL, 150, 0))

        # Exercise SUT
        operacao_transferir = sistema.transferir(origem, destino, Dinheiro(Moeda.BRL, 30, 0))

        # Result Verification
        self.assertEqual(EstadosDeOperacao.SUCESSO, operacao_transferir.obter_estado())

        # Fixture Teardown

    def test_transferencia_sem_saldo_retorna_saldo_insuficiente(self):
        # Estratégia: Delegated Setup & Inline Setup
        # Fixture Setup
        classe_auxiliar = ClasseAuxiliarCriaClassesOrigemDestino()
        sistema, origem, destino = classe_auxiliar.criar_classes_origem_destino()
        sistema.depositar(origem, Dinheiro(Moeda.BRL, 10, 0))

        # Exercise SUT
        operacao_transferir = sistema.transferir(origem, destino, Dinheiro(Moeda.BRL, 20, 0))

        # Result Verification
        self.assertEqual(EstadosDeOperacao.SALDO_INSUFICIENTE, operacao_transferir.obter_estado())

        # Fixture Teardown

    def test_transferencia_em_moeda_invalida_retorna_moeda_invalida(self):
        # Estratégia: Delegated Setup & Inline Setup
        # Fixture Setup
        classe_auxiliar = ClasseAuxiliarCriaClassesOrigemDestino()
        sistema, origem, destino = classe_auxiliar.criar_classes_origem_destino()
        sistema.depositar(origem, Dinheiro(Moeda.BRL, 50, 0))

        # Exercise SUT
        operacao_transferir = sistema.transferir(origem, destino, Dinheiro(Moeda.USD, 5, 0))

        # Result Verification
        self.assertEqual(EstadosDeOperacao.MOEDA_INVALIDA, operacao_transferir.obter_estado())

        # Fixture Teardown

    def test_transferencia_sucesso_debita_conta_de_origem(self):
        # Estratégia: Delegated Setup & Inline Setup
        # Fixture Setup
        classe_auxiliar = ClasseAuxiliarCriaClassesOrigemDestino()
        sistema, origem, destino = classe_auxiliar.criar_classes_origem_destino()
        sistema.depositar(origem, Dinheiro(Moeda.BRL, 90, 0))

        # Exercise SUT
        sistema.transferir(origem, destino, Dinheiro(Moeda.BRL, 25, 0))

        # Result Verification
        saldo_origem = origem.calcular_saldo()
        self.assertEqual("+65,00 BRL", saldo_origem.formatado())

        # Fixture Teardown

    def test_transferencia_sucesso_credita_conta_de_destino(self):
        # Estratégia: Delegated Setup & Inline Setup
        # Fixture Setup
        classe_auxiliar = ClasseAuxiliarCriaClassesOrigemDestino()
        sistema, origem, destino = classe_auxiliar.criar_classes_origem_destino()
        sistema.depositar(origem, Dinheiro(Moeda.BRL, 120, 0))

        # Exercise SUT
        sistema.transferir(origem, destino, Dinheiro(Moeda.BRL, 45, 0))

        # Result Verification
        saldo_destino = destino.calcular_saldo()
        self.assertEqual("+45,00 BRL", saldo_destino.formatado())

        # Fixture Teardown
