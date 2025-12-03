from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//p[contains(@class, 'forgot-password')]")
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def navigate_to_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
    
    def login(self, username, password):
        self.send_keys(self.USERNAME_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
    
    def is_login_successful(self):
        return self.is_element_present(self.DASHBOARD_HEADER)