from AliorBank.POMProject.Locators.locators import Locators
from selenium.webdriver.common.keys import Keys


class LoanApplicationPage():

    def __init__(self, driver):
        self.driver = driver

    def closeCookiesInfo(self):
        self.driver.find_element_by_link_text(Locators.closeCookies_button_link_text).click()

    def enterFirstName(self, firstName):
        self.driver.find_element_by_id(Locators.firstName_textbox_id).clear()
        self.driver.find_element_by_id(Locators.firstName_textbox_id).send_keys(firstName)

    def enterLastName(self, lastName):
        self.driver.find_element_by_id(Locators.lastName_textbox_id).clear()
        self.driver.find_element_by_id(Locators.lastName_textbox_id).send_keys(lastName)

    def enterEmailAddress(self, emailAddress):
        self.driver.find_element_by_id(Locators.emailAddress_textbox_id).clear()
        self.driver.find_element_by_id(Locators.emailAddress_textbox_id).send_keys(emailAddress)

    def enterMobileNumber(self, mobileNumber):
        self.driver.find_element_by_name(Locators.mobileNumber_textbox_name).clear()
        self.driver.find_element_by_name(Locators.mobileNumber_textbox_name).send_keys(mobileNumber)

    def enterCashAmount(self, cashAmount):
        self.driver.find_element_by_name(Locators.cashAmount_textbox_name).clear()
        self.driver.find_element_by_name(Locators.cashAmount_textbox_name).send_keys(cashAmount)

    def choosePeriodOfLoan(self, years, months):
        period = self.driver.find_elements_by_css_selector(Locators.loanPeriod_select_css_selector)
        for i in range(years):
            period[0].send_keys(Keys.ARROW_DOWN)
        for i in range(months):
            period[1].send_keys(Keys.ARROW_DOWN)

    def clickCheckboxes(self):
        self.driver.find_element_by_class_name(Locators.agreement_checkbox_class_name).click()
        relatedAgreementCheckboxes = self.driver.find_elements_by_class_name(Locators.agreement_checkbox_class_name)
        for i in range(len(relatedAgreementCheckboxes) - 1):
            relatedAgreementCheckboxes[i+1].click()

    def clickAcceptanceButton(self):
        self.driver.find_element_by_css_selector(Locators.acceptance_button_css_selector).click()


