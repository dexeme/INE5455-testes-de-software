''' 
Estratégias:

1 - Inline Setup: O código de configuração é escrito diretamente dentro do método de teste.
2 - Implicit Setup: O código de configuração é colocado em um método separado, como setUp(), que é executado antes de cada teste.
3 - Delegated Setup: O código de configuração é colocado em uma função ou método separado, e os testes chamam essa função para obter os dados necessários.

Todos os testes devem ter esses comentários (além de especificar qual foi a estratégia adotada):

# Fixture Setup
# Exercise SUT
# Result Verification
# Fixture Teardown

Onde colocar os testes?

Estratégias:
- Classes de Testes por Feature
- Classes de Testes por Fixture

Regras:
- Cada teste deve testar apenas 1 coisa
- No método setup é só o que é comum pra todos os testes

As operações de depositar, sacar e transferir dinheiro devem ser realizadas a partir do SistemaBancario.
'''

'''
▪ Dinheiro:
- test_deposito_com_fracionado_maior_que_base_normaliza_valor
- test_deposito_valido_atualiza_saldo_da_conta
- test_depositos_sequenciais_acumulam_saldo

▪ Valor Monetario:
- test_saque_nao_realizado_mantem_saldo_original
- test_transferencia_sucesso_debita_conta_de_origem
- test_transferencia_sucesso_credita_conta_de_destino

▪ Banco:
- test_deposito_em_reais_retorna_sucesso
- test_deposito_em_moeda_diferente_retorna_moeda_invalida
- test_saque_em_moeda_diferente_retorna_moeda_invalida
- test_transferencia_em_moeda_invalida_retorna_moeda_invalida
- test_inline_deposito_valido_em_conta_brl_retorna_sucesso

▪ Agencia:
- test_saque_com_saldo_suficiente_retorna_sucesso
- test_transferencia_com_saldo_suficiente_retorna_sucesso
- test_inline_transferencia_sucesso_move_valor_entre_contas

▪ Conta:
- test_saque_reduz_o_saldo_quando_ha_sucesso
- test_saque_do_valor_total_zera_o_saldo

▪ SistemaBancario:
- test_deposito_com_quantia_zero_retorna_saldo_insuficiente
- test_saque_maior_que_saldo_retorna_saldo_insuficiente
- test_transferencia_sem_saldo_retorna_saldo_insuficiente
- test_inline_saque_sem_saldo_em_conta_brl_retorna_saldo_insuficiente

'''
import unittest
from test_sistema_bancario_feature import TestDepositosPorFeature, TestSaquesPorFeature, TestTransferenciasPorFeature
from test_sistema_bancario_fixture import TestOperacoesComFixtureContaBRL

testDepositosPorFeature = unittest.TestLoader().loadTestsFromTestCase(TestDepositosPorFeature)
testSaquesPorFeature = unittest.TestLoader().loadTestsFromTestCase(TestSaquesPorFeature)
testTransferenciasPorFeature = unittest.TestLoader().loadTestsFromTestCase(TestTransferenciasPorFeature)
testOperacoesComFixtureContaBRL = unittest.TestLoader().loadTestsFromTestCase(TestOperacoesComFixtureContaBRL)
suite = unittest.TestSuite([testDepositosPorFeature, testSaquesPorFeature, testTransferenciasPorFeature, testOperacoesComFixtureContaBRL])
unittest.TextTestRunner(verbosity=2).run(suite)