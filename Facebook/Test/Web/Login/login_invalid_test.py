from time import sleep

from selenium.common.exceptions import

from selenium.webdriver.common.by import By

from Facebook.Test.BaseTest.Base_Test_Login.base_test import *

from Facebook.Locaters.Login.login_locaters import *


class Test_wrong(BaseTest):

    # --------------------- incorrect username --------------------------------

    def test_login_incorrect_username(self):
        drivre = super().init()

        username = drivre.find_element(By.XPATH, f"{username_path}")
        sleep(2)
        username.clear()
        username.send_keys(incorrect_username)
        sleep(2)
        password = drivre.find_element(By.XPATH, f"{pasword_path}")
        password.clear()
        password.send_keys(correct_password)
        sleep(2)
        drivre.find_element(By.XPATH, f"{login_button_path}").click()
        sleep(2)
        Url = drivre.current_url
        assert Url == "https://www.facebook.com/"
        super().wimdow_close()

    # -------------------- incorrect password -----------------------------------

    def test_login_incorrect_password(self):
        drivre = super().init()

        username = drivre.find_element(By.XPATH, f"{username_path}")
        sleep(2)
        username.clear()
        username.send_keys(correct_username)
        sleep(2)
        password = drivre.find_element(By.XPATH, f"{pasword_path}")
        password.clear()
        password.send_keys(incorrct_password)
        sleep(2)
        drivre.find_element(By.XPATH, f"{login_button_path}").click()
        sleep(2)
        Url = drivre.current_url
        assert Url == "https://www.facebook.com/"
        super().wimdow_close()


    #  ----------------------------- incorrect password and username --------------------------------

    def test_login_incorrect_password_username(self):
        drivre = super().init()

        username = drivre.find_element(By.XPATH, f"{username_path}")
        sleep(2)
        username.clear()
        username.send_keys(incorrect_username)
        sleep(2)
        password = drivre.find_element(By.XPATH, f"{pasword_path}")
        password.clear()
        password.send_keys(incorrct_password)
        sleep(2)
        drivre.find_element(By.XPATH, f"{login_button_path}").click()
        sleep(2)
        Url = drivre.current_url
        assert Url == "https://www.facebook.com/"
        super().wimdow_close()


    #  --------------------------------- username with null value ------------------------------------

    def test_login_empity_username(self):
        drivre = super().init()

        username = drivre.find_element(By.XPATH, f"{username_path}")
        sleep(2)
        username.clear()
        username.send_keys(empity_username)
        sleep(2)
        password = drivre.find_element(By.XPATH, f"{pasword_path}")
        password.clear()
        password.send_keys(incorrct_password)
        sleep(2)
        drivre.find_element(By.XPATH, f"{login_button_path}").click()
        sleep(2)
        Url = drivre.current_url
        assert Url == "https://www.facebook.com/"
        super().wimdow_close()