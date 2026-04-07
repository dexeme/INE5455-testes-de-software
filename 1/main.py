import unittest
import datetime

'''
# Fixture Setup
# Exercise SUT
# Result Verification
# Fixture Teardown

Exercício 1 - Python
    Os testes devem incluir a manipulação dos seguintes objetos:
        ▪ datetime.date
        ▪ datetime.time
        ▪ datetime.datetime
        ▪ datetime.timedelta
Métodos a serem testados: criação, replace, toordinal,
weekday...
'''

class DatetimeTests(unittest.TestCase):

    def setup(self):
        pass

    def test_datetime_com_dia_negativo(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(2026, 3, -17)
        # Result Verification
        # Fixture Teardown

    def test_datetime_com_mes_negativo(self):
       # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(2026, -3, 17)
        # Result Verification
        # Fixture Teardown

    def test_datetime_com_ano_negativo(self):
       # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(-2026, 3, 17)
        # Result Verification
        # Fixture Teardown

    def test_dia_29_fevereiro_ano_bissexto(self):
        # Fixture Setup
        data = datetime.date(2028, 2, 29)
        # Exercise SUT
        self.assertEqual(data.day, 29)
        # Result Verification
        # Fixture Teardown

    def test_dia_29_fevereiro_ano_nao_bissexto(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(2026, 2, 29)
        # Result Verification
        # Fixture Teardown

    def test_dia_30_fevereiro_ano_nao_bissexto(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(2026, 2, 30)
        # Result Verification
        # Fixture Teardown

    def test_dia_0(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(2026, 3, 0)
        # Result Verification
        # Fixture Teardown

    def test_mes_0(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(2026, 0, 17)
        # Result Verification
        # Fixture Teardown

    def test_ano_0(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(0, 3, 17)
        # Result Verification
        # Fixture Teardown

    def test_timedelta_diferenca_entre_duas_datas_eh_negativo(self):
        # Fixture Setup
        data1 = datetime.date(2026, 3, 17)
        data2 = datetime.date(2026, 3, 18)
        # Exercise SUT
        diferenca = data1 - data2
        # Result Verification
        self.assertEqual(diferenca.days, -1)
        # Fixture Teardown

    def test_timedelta_diferenca_entre_duas_datas_eh_zero(self):
        # Fixture Setup
        data1 = datetime.date(2026, 3, 17)
        data2 = datetime.date(2026, 3, 17)
        # Exercise SUT
        diferenca = data2 - data1
        # Result Verification
        self.assertEqual(diferenca.days, 0)
        # Fixture Teardown

    def test_timedelta_entre_28_fev_de_um_ano_normal_e_29_fev_de_um_ano_bissexto(self):
        # Fixture Setup
        data1 = datetime.date(2026, 2, 28)
        data2 = datetime.date(2028, 2, 29)
        # Exercise SUT
        diferenca = data2 - data1
        # Result Verification
        self.assertEqual(diferenca.days, 731)
        # Fixture Teardown

    def test_timedelta_entre_duas_datas_diferentes_negativo(self):
        # Fixture Setup
        data1 = datetime.date(2026, 3, 17)
        data2 = datetime.date(2026, 3, 18)
        # Exercise SUT
        diferenca = data1 - data2
        # Result Verification
        self.assertEqual(diferenca.days, -1)
        # Fixture Teardown

    def test_timedelta_entre_duas_datas_diferentes_positivo(self):
        # Fixture Setup
        data1 = datetime.date(2026, 3, 17)
        data2 = datetime.date(2026, 3, 18)
        # Exercise SUT
        diferenca = data2 - data1
        # Result Verification
        self.assertEqual(diferenca.days, 1)
        # Fixture Teardown

    def test_method_to_week_day_terca_feira(self):
        # Fixture Setup
        data = datetime.date(2026, 3, 17)
        # Exercise SUT
        dia_semana = data.weekday()
        # Result Verification
        self.assertEqual(dia_semana, 1)
        # Fixture Teardown

    def test_method_replace_ano_valido(self):
        # Fixture Setup
        data = datetime.date(2026, 3, 17)
        # Exercise SUT
        data_nova = data.replace(year=2025)
        # Result Verification
        self.assertEqual(data_nova.year, 2025)
        self.assertEqual(data_nova.month, 3)
        self.assertEqual(data_nova.day, 17)
        # Fixture Teardown

    def test_method_replace_ano_negativo(self):
        # Fixture Setup
        data = datetime.date(2026, 3, 17)
        # Exercise SUT
        with self.assertRaises(ValueError):
            data.replace(year=-2025)
        # Result Verification
        # Fixture Teardown

    def test_method_toordinal_data_valida(self):
        # Fixture Setup
        data = datetime.date(2026, 3, 17)
        # Exercise SUT
        ordinal = data.toordinal()
        # Result Verification
        self.assertEqual(ordinal, 739692)
        # Fixture Teardown



    def test_criacao_de_time_valido(self):
        # Fixture Setup
        # Exercise SUT
        time = datetime.time(second=1, minute=10, hour=10)
        # Result Verification
        self.assertEqual(time.second, 1)
        self.assertEqual(time.minute, 10)
        self.assertEqual(time.hour, 10)
        # Fixture Teardown

    def test_criacao_de_time_com_segundo_negativo(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.time(second=-1, minute=10, hour=12)
        # Result Verification
        # Fixture Teardown

    def test_criacao_de_time_com_minuto_negativo(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.time(second=1, minute=-10, hour=12)
        # Result Verification
        # Fixture Teardown

    def test_criacao_de_time_com_hora_negativa(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.time(second=1, minute=10, hour=-12)
        # Result Verification
        # Fixture Teardown

    def test_criacao_de_time_segundo_maior_que_59(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.time(second=60, minute=10, hour=10)
        # Result Verification
        # Fixture Teardown

    def test_criacao_de_time_minuto_maior_que_59(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.time(second=1, minute=60, hour=10)
        # Result Verification
        # Fixture Teardown

    def test_criacao_de_time_hora_maior_que_23(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.time(second=1, minute=10, hour=24)
        # Result Verification
        # Fixture Teardown





if __name__ == '__main__':
    unittest.main()