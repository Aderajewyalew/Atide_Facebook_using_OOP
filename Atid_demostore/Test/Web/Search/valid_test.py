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
        driver.find_element(By.XPATH, search).send_keys(product_men)
        sleep(2)
        driver.find_element(By.XPATH, go).click()

        driver.find_element(By.NAME, add_tochart).click()
        driver.find_element(By.XPATH, view_chart).click()
        price_men = driver.find_element(By.XPATH, product_price).text
        assert price_men == "110.00 ₪"

    # -----------------------checking store product by searching button -------------------------------
    def test_search_store_product(self):
        driver = super().init()
        driver.get(website)
        driver.maximize_window()
        driver.find_element(By.XPATH, store).click()
        sleep(2)
        driver.find_element(By.XPATH, search).send_keys(product_store)
        driver.find_element(By.XPATH, go).click()
        driver.find_element(By.XPATH, demi_jeans).click()
        driver.find_element(By.NAME, add_tochart).click()
        driver.find_element(By.XPATH, view_chart).click()
        price_store = driver.find_element(By.XPATH, product_price).text
        assert price_store == "150.00 ₪"

    def test_search_men_accessories(self):
        driver = super().init()
        driver.get(website)
        driver.maximize_window()
        sleep(2)
        driver.find_element(By.XPATH, accessories).click()
        sleep(2)
        driver.find_element(By.XPATH, search).send_keys(product_accessories)
        sleep(2)
        driver.find_element(By.XPATH, go).click()

        driver.find_element(By.NAME, add_tochart).click()
        driver.find_element(By.XPATH, view_chart).click()
        price_accessories = driver.find_element(By.XPATH, product_price).text
        assert price_accessories == "250.00 ₪"
