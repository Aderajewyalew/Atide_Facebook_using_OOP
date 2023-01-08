
from time import sleep

from selenium.webdriver.common.by import By

from Facebook.Test.BaseTest.Base_terst_Regstore.base_test import *

from Facebook.Locaters.Registore.registore_locaters import *


class Test_worng(BaseTest):

    # ------------------------ wegistore first username null ------------------------------------

    def test_registor_username_null(self):
        driver = super().init()

        sleep(2)
        driver.find_element(By.XPATH,create).click()
        sleep(3)
        driver.find_element(By.NAME,fname).send_keys("")
        sleep(2)
        driver.find_element(By.NAME,lname).send_keys("israel")
        sleep(2)
        driver.find_element(By.XPATH,phone).send_keys("0533863205")
        sleep(2)
        driver.find_element(By.ID,pasword).send_keys("ade2013yal")
        sleep(2)
        driver.find_element(By.NAME,Month).click()
        sleep(2)
        driver.find_element(By.XPATH,Months).click()
        sleep(2)

        driver.find_element(By.NAME,Day).click()
        sleep(2)
        driver.find_element(By.XPATH,Days).click()
        sleep(2)

        driver.find_element(By.NAME,Year).click()
        sleep(2)
        driver.find_element(By.XPATH,Years).click()
        sleep(2)

        driver.find_element(By.XPATH,Male).click()
        sleep(2)

        driver.find_element(By.XPATH,sign_in).click()
        sleep(2)


    # --------------------- registore with lastname null --------------------------------------


    def test_registor_lastname_null(self):
        driver = super().init()

        sleep(2)
        driver.find_element(By.XPATH,create).click()
        sleep(3)
        driver.find_element(By.NAME,fname).send_keys("David")
        sleep(2)
        driver.find_element(By.NAME,lname).send_keys("")
        sleep(2)
        driver.find_element(By.XPATH,phone).send_keys("0533863205")
        sleep(2)
        driver.find_element(By.ID,pasword).send_keys("ade2013yal")
        sleep(2)
        driver.find_element(By.NAME,Month).click()
        sleep(2)
        driver.find_element(By.XPATH,Months).click()
        sleep(2)

        driver.find_element(By.NAME,Day).click()
        sleep(2)
        driver.find_element(By.XPATH,Days).click()
        sleep(2)

        driver.find_element(By.NAME,Year).click()
        sleep(2)
        driver.find_element(By.XPATH,Years).click()
        sleep(2)

        driver.find_element(By.XPATH,Male).click()
        sleep(2)

        driver.find_element(By.XPATH,sign_in).click()
        sleep(2)


    # ---------------------------- registore with phone number null

    def test_registor_phone_no_null(self):
        driver = super().init()

        sleep(2)
        driver.find_element(By.XPATH,create).click()
        sleep(3)
        driver.find_element(By.NAME,fname).send_keys("David")
        sleep(2)
        driver.find_element(By.NAME,lname).send_keys("israel")
        sleep(2)
        driver.find_element(By.XPATH,phone).send_keys("")
        sleep(2)
        driver.find_element(By.ID,pasword).send_keys("ade2013yal")
        sleep(2)
        driver.find_element(By.NAME,Month).click()
        sleep(2)
        driver.find_element(By.XPATH,Months).click()
        sleep(2)

        driver.find_element(By.NAME,Day).click()
        sleep(2)
        driver.find_element(By.XPATH,Days).click()
        sleep(2)

        driver.find_element(By.NAME,Year).click()
        sleep(2)
        driver.find_element(By.XPATH,Years).click()
        sleep(2)

        driver.find_element(By.XPATH,Male).click()
        sleep(2)

        driver.find_element(By.XPATH,sign_in).click()
        sleep(2)


    # --------------------------- registore with password null ----------------------------------

    def test_registor_password_null(self):
        driver = super().init()

        sleep(2)
        driver.find_element(By.XPATH,create).click()
        sleep(3)
        driver.find_element(By.NAME,fname).send_keys("David")
        sleep(2)
        driver.find_element(By.NAME,lname).send_keys("israel")
        sleep(2)
        driver.find_element(By.XPATH,phone).send_keys("0533863205")
        sleep(2)
        driver.find_element(By.ID,pasword).send_keys("")
        sleep(2)
        driver.find_element(By.NAME,Month).click()
        sleep(2)
        driver.find_element(By.XPATH,Months).click()
        sleep(2)

        driver.find_element(By.NAME,Day).click()
        sleep(2)
        driver.find_element(By.XPATH,Days).click()
        sleep(2)

        driver.find_element(By.NAME,Year).click()
        sleep(2)
        driver.find_element(By.XPATH,Years).click()
        sleep(2)

        driver.find_element(By.XPATH,Male).click()
        sleep(2)

        driver.find_element(By.XPATH,sign_in).click()
        sleep(2)







