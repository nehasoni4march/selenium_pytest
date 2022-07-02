from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest


def test_login():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.orangehrm.com/hris-hr-software-demo/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    time.sleep(5)




    driver.find_element(By.ID,"Form_submitForm_FirstName").send_keys("Neha")
    driver.find_element(By.NAME,"LastName").send_keys("Soni")
    driver.find_element(By.NAME,"Email").send_keys("nehasoni4march@gmail.com")
    driver.find_element(By.NAME,"Contact").send_keys("987654321")

    countryid=driver.find_element(By.NAME,"Country")
    Select(countryid).select_by_visible_text("India")

    time.sleep(5)
    driver.quit()

def test_menu():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.orangehrm.com/hris-hr-software-demo/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    time.sleep(5)

    driver.find_element(By.LINK_TEXT, "Platform").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Why OrangeHRM").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Resources").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Company").click()
    time.sleep(5)
    driver.quit()

def test_about():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.orangehrm.com/hris-hr-software-demo/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Company").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT,"About Us").click()
    time.sleep(1)
    a=driver.find_elements(By.XPATH, "//div[@class='about-content']")
    for ele in a:
        print(ele.text)
    time.sleep(5)
    driver.quit()

def test_contactsales():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.orangehrm.com/hris-hr-software-demo/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    time.sleep(1)

    driver.find_element(By.LINK_TEXT, 'Why OrangeHRM').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Case Studies").click()
    time.sleep(2)
    value=driver.find_elements(By.CLASS_NAME, "case-study-content")[0].text
    print(value)

    # itemlist = driver.find_elements(By.CLASS_NAME, "case-study-content")
    # time.sleep(2)
    # for item in itemlist:
    #     print(item.text)








