from time import sleep

from selenium.webdriver.common.by import By

from Facebook.Test.BaseTest.Base_terst_Regstore.base_test import *

from Facebook.Locaters.Registore.registore_locaters import *


class Test(BaseTest):

    def test_registor_correctly(self):
        driver = super().init()

        sleep(2)
        driver.find_element(By.XPATH, create).click()
        sleep(3)
        driver.find_element(By.NAME, fname).send_keys("David")
        sleep(2)
        driver.find_element(By.NAME, lname).send_keys("israel")
        sleep(2)
        driver.find_element(By.XPATH, phone).send_keys("0533863205")
        sleep(2)
        driver.find_element(By.ID, pasword).send_keys("ade2013yal")
        sleep(2)
        driver.find_element(By.NAME, Month).click()
        sleep(2)
        driver.find_element(By.XPATH, Months).click()
        sleep(2)

        driver.find_element(By.NAME, Day).click()
        sleep(2)
        driver.find_element(By.XPATH, Days).click()
        sleep(2)

        driver.find_element(By.NAME, Year).click()
        sleep(2)
        driver.find_element(By.XPATH, Years).click()
        sleep(2)

        driver.find_element(By.XPATH, Male).click()
        sleep(2)

        driver.find_element(By.XPATH, sign_in).click()
        sleep(10)

        txt = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/h2[1]"
        assert txt == "Enter the confirmation code from the text message"
