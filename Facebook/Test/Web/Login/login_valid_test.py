from time import sleep

from selenium.webdriver.common.by import By

from Facebook.Test.BaseTest.Base_Test_Login.base_test import *

from Facebook.Locaters.Login.login_locaters import *

class Test(BaseTest):


    def test_login_correct_input(self):
        drivre = super().init()

        username = drivre.find_element(By.XPATH,f"{username_path}")
        sleep(2)
        username.clear()
        username.send_keys(correct_username)
        sleep(2)
        password = drivre.find_element(By.XPATH,f"{pasword_path}")
        password.clear()
        password.send_keys(correct_password)
        sleep(2)
        drivre.find_element(By.XPATH,f"{login_button_path}").click()
        sleep(2)
        Url = drivre.current_url
        assert Url == "https://www.facebook.com/"
