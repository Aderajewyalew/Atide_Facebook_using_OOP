from time import sleep


from selenium.webdriver.common.by import By

from Atid_demostore.Test.BasesTest.base_test import *

from Atid_demostore.Locaters.locaters import *


class Test(BaseTest):

    # ---------------------------- checking men product by search button  ---------------------------
    def test_search_men_product(self):
        driver = super().init()
        driver.get(website)
        driver.maximize_window()
        sleep(2)
        driver.find_element(By.XPATH, men).click()
        sleep(2)
        driver.find_element(By.XPATH, search).send_keys("Biskut")
        sleep(2)
        driver.find_element(By.XPATH, go).click()

        driver.find_element(By.NAME, add_tochart).click()
        driver.find_element(By.XPATH, view_chart).click()
        price_biskut = driver.find_element(By.XPATH, product_price).text
        assert price_biskut == "10.0 ₪"

    # -----------------------checking store product by searching button -------------------------------
    def test_search_store_product(self):
        driver = super().init()
        driver.get(website)
        driver.maximize_window()
        driver.find_element(By.XPATH, store).click()
        sleep(2)
        driver.find_element(By.XPATH, search).send_keys("car")
        driver.find_element(By.XPATH, go).click()
        driver.find_element(By.XPATH, demi_jeans).click()
        driver.find_element(By.NAME, add_tochart).click()
        driver.find_element(By.XPATH, view_chart).click()
        price_car = driver.find_element(By.XPATH, product_price).text
        assert price_car == "155000.0 ₪"



    # ------------------------------- checking accesserios product by searching button -------------------------------
    def test_search_men_accessories(self):
        driver = super().init()
        driver.get(website)
        driver.maximize_window()
        sleep(2)
        driver.find_element(By.XPATH, accessories).click()
        sleep(2)
        driver.find_element(By.XPATH, search).send_keys("")
        sleep(2)
        driver.find_element(By.XPATH, go).click()

        driver.find_element(By.NAME, add_tochart).click()
        driver.find_element(By.XPATH, view_chart).click()
        price_null = driver.find_element(By.XPATH, product_price).text
        assert price_null == "250.00 ₪"
