"""Selenium WebDriver tests for DuckDuckGo's calculator.

Run with:
    ../.venv/bin/python -m unittest test_duckduckgo_calculator.py

Use HEADLESS=0 to watch the browser during presentation.
"""

import os
import unittest

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class DuckDuckGoCalculatorTest(unittest.TestCase):
    CALCULATOR_URL = "https://duckduckgo.com/?q=calculator&ia=calculator"
    DISPLAY = (By.ID, "display")
    HISTORY = (By.CSS_SELECTOR, ".tile__history")

    @classmethod
    def setUpClass(cls):
        cls.chrome_binary = os.environ.get("CHROME_BINARY", "/usr/bin/chromium")
        cls.chromedriver = os.environ.get("CHROMEDRIVER", "/usr/bin/chromedriver")

    def setUp(self):
        options = Options()
        options.binary_location = self.chrome_binary
        options.add_argument("--window-size=1366,900")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        if os.environ.get("HEADLESS", "1") != "0":
            options.add_argument("--headless=new")

        self.driver = webdriver.Chrome(
            service=Service(self.chromedriver),
            options=options,
        )
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get(self.CALCULATOR_URL)
        self.wait.until(EC.text_to_be_present_in_element(self.DISPLAY, "0"))

    def tearDown(self):
        self.driver.quit()

    def click_button(self, value):
        button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"button[value='{value}']"))
        )
        try:
            button.click()
        except ElementClickInterceptedException:
            # DuckDuckGo may render a feedback/bot overlay in automated browsers.
            self.driver.execute_script("arguments[0].click();", button)

    def enter(self, *values):
        operators = {"+", "-", "×", "÷", "=", "C", "."}
        for value in values:
            keys = [value] if value in operators else list(value)
            for key in keys:
                self.click_button(key)

    def clear(self):
        self.click_button("C")
        self.assert_display("0")

    def display_text(self):
        return self.wait.until(EC.presence_of_element_located(self.DISPLAY)).text

    def assert_display(self, expected):
        self.wait.until(EC.text_to_be_present_in_element(self.DISPLAY, expected))
        self.assertEqual(expected, self.display_text())

    def history_text(self):
        return self.wait.until(EC.presence_of_element_located(self.HISTORY)).text

    def test_a_soma_dois_numeros_diferentes(self):
        self.enter("12", "+", "34", "=")

        self.assert_display("46")

    def test_b_multiplica_e_divide_resultado_por_dez(self):
        self.enter("7", "×", "8", "=")
        self.assert_display("56")

        self.enter("÷", "10", "=")

        self.assert_display("5.6")

    def test_c_duas_operacoes_diferentes_com_subtracao(self):
        self.enter("91", "-", "23", "=", "+", "45", "=")

        self.assert_display("113")

    def test_d_tres_operacoes_verifica_resultados_e_historico(self):
        operations = [
            (("101", "+", "202", "="), "303", "101 + 202"),
            (("77", "-", "11", "="), "66", "77 - 11"),
            (("13", "×", "4", "="), "52", "13 × 4"),
        ]

        for index, (keys, expected_result, _) in enumerate(operations):
            if index > 0:
                self.clear()
            self.enter(*keys)
            self.assert_display(expected_result)

        history = self.history_text()
        for _, expected_result, expected_expression in operations:
            self.assertIn(expected_expression, history)
            self.assertIn(expected_result, history)


if __name__ == "__main__":
    unittest.main(verbosity=2)
