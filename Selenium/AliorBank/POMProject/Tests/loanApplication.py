from selenium import webdriver
import unittest
from pyunitreport import HTMLTestRunner
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from AliorBank.POMProject.Pages.loanApplicationPage import LoanApplicationPage
from AliorBank.POMProject.DataGenerators.dataGenerators import DataGenerators


class LoanApplicationTest(unittest.TestCase):

    data = DataGenerators()

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/home/mikolaj/PycharmProjects/Selenium/Drivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_loan_application(self):
        driver = self.driver
        pageURL = "https://wnioski.aliorbank.pl/spinner-process/?partnerId=POR_P_ZERO_S&transactionCode=pozyczki"
        driver.get(pageURL)

        application = LoanApplicationPage(driver)
        data = DataGenerators()

        application.closeCookiesInfo()
        application.enterFirstName(data.generateFirstName())
        application.enterLastName(data.generateLastName())
        application.enterEmailAddress(data.generateEmailAddress())
        application.enterMobileNumber("000000000")
        application.enterCashAmount("500")
        application.choosePeriodOfLoan(1, 11)
        application.clickCheckboxes()
        application.clickAcceptanceButton()
        url = driver.current_url
        self.assertEqual(url, pageURL)
        assert url == "https://wnioski.aliorbank.pl/spinner-process/?partnerId=POR_P_ZERO_S&transactionCode=pozyczki"
        assert "Niepoprawny numer telefonu" in driver.page_source
        assert "Adres e-mail jest niepoprawny." not in driver.page_source
        assert "To pole jest wymagane." not in driver.page_source
        assert "Maksymalna liczba znaków" not in driver.page_source
        assert "Wprowadzono nieprawidłowe znaki" not in driver.page_source
        assert "Podano za niską kwotę pożyczki" not in driver.page_source
        assert "Przekroczyłeś maksymalną kwotę pożyczki." not in driver.page_source

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    outfile = open('/home/mikolaj/PycharmProjects/Selenium/Reports', 'w')
    unittest.main(testRunner=HTMLTestRunner(output='../Reports'))




