from time import sleep

from selenium.webdriver.common.by import By

from Facebook.Test.BaseTest.Base_Test_forgotpass_wor.base_test import BaseTest

from Facebook.Locaters.Forgot_passworde.forgot_password_locaters import *






class Test_wrong_data(BaseTest):

    # -------------------------------- incorrect phone num---------------------

    def test_forgotPssword_incorrec_phone(self):
        driver = super().init()
        driver.find_element(By.XPATH, forgot_password).click()
        sleep(1)

        driver.find_element(By.ID, email).send_keys(phone_incorret_value)
        sleep(2)

        driver.find_element(By.XPATH, Search).click()
        sleep(2)

        texts = driver.find_element(By.XPATH, Tag1).text
        assert texts == "Reset Your Password"

        driver.find_element(By.XPATH, contenue).click()
        sleep(2)

        driver.find_element(By.XPATH, cancel).click()
        sleep(2)
        super().wimdow_close()


    # -------------------------instead of phone num write letters ------------------------------------

    def test_forgotPssword_letters_phone(self):
        driver = super().init()
        driver.find_element(By.XPATH, forgot_password).click()
        sleep(1)

        driver.find_element(By.ID, email).send_keys(phon_letters)
        sleep(2)

        driver.find_element(By.XPATH, Search).click()
        sleep(2)

        texts = driver.find_element(By.XPATH, Tag1).text
        assert texts == "Reset Your Password"

        driver.find_element(By.XPATH, contenue).click()
        sleep(2)

        driver.find_element(By.XPATH, cancel).click()
        sleep(2)
        super().wimdow_close()


    # ---------------------------- instead of phone num write letters and num ----------------------------

    def test_forgotPssword_lettersNum_phone(self):
        driver = super().init()
        driver.find_element(By.XPATH, forgot_password).click()
        sleep(1)

        driver.find_element(By.ID, email).send_keys(phone_num_letters)
        sleep(2)

        driver.find_element(By.XPATH, Search).click()
        sleep(2)

        texts = driver.find_element(By.XPATH, Tag1).text
        assert texts == "Reset Your Password"

        driver.find_element(By.XPATH, contenue).click()
        sleep(2)

        driver.find_element(By.XPATH, cancel).click()
        sleep(2)
        super().wimdow_close()

    #  ------------------ instead of phone num write wrong email --------------------------------
    def test_forgotPssword_wrong_email(self):

        driver = super().init()
        driver.find_element(By.XPATH, forgot_password).click()
        sleep(2)

        driver.find_element(By.ID, email).send_keys(wrong_email)
        sleep(2)

        driver.find_element(By.XPATH, Search).click()
        sleep(2)

        texts = driver.find_element(By.XPATH, Tag1).text
        assert texts == "Reset Your Password"

        driver.find_element(By.XPATH, contenue).click()
        sleep(2)

        driver.find_element(By.XPATH, cancel).click()
        sleep(2)
        super().wimdow_close()

