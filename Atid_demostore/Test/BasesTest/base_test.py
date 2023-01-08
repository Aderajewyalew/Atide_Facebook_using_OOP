from selenium import webdriver


class BaseTest():

    def init(self):

         self.driver = webdriver.Chrome()
         self.driver.get("https://atid.store/")
         self.driver.maximize_window()
         return self.driver

    def wimdow_close(self):
        self.driver.quit()
        self.driver.close()
