import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class OMK_Paypal(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_paypal(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("https://omk-2.herokuapp.com/")
       time.sleep(3)
       elem = driver.find_element_by_link_text("Give").click()
       driver.find_element_by_link_text("Donate").click()
       driver.find_element_by_link_text("Donate $50").click()
       driver.find_element_by_id("id_quantity").send_keys(2)
       driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/input[3]").click()
       driver.find_element_by_id("id_quantity").send_keys(1)
       driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/table/tbody/tr[1]/td[2]/form/input[2]").click()
       driver.find_element_by_link_text("Checkout").click()
       driver.find_element_by_id("id_first_name").send_keys("Srav")
       driver.find_element_by_id("id_last_name").send_keys("Duddu")
       driver.find_element_by_id("id_email").send_keys("sravy.kv@gmail.com")
       driver.find_element_by_id("id_address").send_keys("Roxbury Plaza")
       driver.find_element_by_id("id_postal_code").send_keys("68137")
       driver.find_element_by_id("id_city").send_keys("Omaha")
       driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/form/p[7]/input").click()
       driver.find_element_by_xpath("/html/body/form/input[12]").click()
       time.sleep(3)
       driver.find_element_by_id("email").send_keys("vinodmalviya-buyer@gmail.com")
      # time.sleep(15)
       #driver.find_element_by_name("login_password").send_keys("11111111")
       #time.sleep(3)
       #driver.find_element_by_name("btnLogin").click()
       #time.sleep(3)
       #driver.find_element_by_id("confirmButtonTop").click()
       #driver.find_element_by_id("merchantReturnBtn").click()

   def test_locateus(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://omk-2.herokuapp.com/")
        time.sleep(3)
        elem = driver.find_element_by_link_text("Locate Us").click()
        driver.find_element_by_name("element.school").send_keys("UNO")
        driver.find_element_by_xpath("/html/body/form/div/div/button").click()
        time.sleep(3)
   def test_Task(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("https://omk-2.herokuapp.com/login_user")
       driver.find_element_by_id("id_username").send_keys("Sravani")
       driver.find_element_by_id("id_password").send_keys("srav12345")
       driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div[1]/form/div[3]/div/button").click()
       driver.find_element_by_xpath("/html/body/div[1]/nav/div[2]/ul/li[7]/a").click()
       #driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/span[1]/span[2]/a/span[2]").click()
       #messaging
       driver.find_element_by_xpath("/html/body/div[1]/nav/div[2]/ul/li[6]/a").click()
       driver.find_element_by_name("to_number").send_keys("Amit")
       driver.find_element_by_name("body").send_keys("Hi Parents, we have scheduled an appointment today at 4PM")
       driver.find_element_by_xpath(" /html/body/div[1]/div/div/form/div[3]/div/button").click()

   def test_twitter(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("https://omk-2.herokuapp.com")
       driver.find_element_by_link_text("Give").click()
       driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/a").click()
       driver.find_element_by_id("username_or_email").send_keys("mukati.aarti012@gmail.com")
       driver.find_element_by_id("password").send_keys("arti123")
       driver.find_element_by_id("allow").click()





















   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()