from time import sleep

from selenium.webdriver.common.by import By

from Facebook.Test.BaseTest.Base_Test_forgotpass_wor.base_test import BaseTest

from Facebook.Locaters.Forgot_passworde.forgot_password_locaters import *


class   Test(BaseTest):

    def test_forgot_passwor(self):

        driver = super().init()

        driver.find_element(By.XPATH,forgot_password).click()
        sleep(1)


        driver.find_element(By.ID,email).send_keys(phone)
        sleep(2)

        driver.find_element(By.XPATH,Search).click()
        sleep(2)



        driver.find_element(By.XPATH,contenue).click()
        sleep(2)

        driver.find_element(By.XPATH,cancel).click()
        sleep(2)

        texts = driver.find_element(By.XPATH, Tag1).text
        assert texts == "Reset Your Password"
        super().wimdow_close()