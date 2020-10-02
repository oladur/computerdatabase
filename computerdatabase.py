
import time
import _pytest
from selenium import webdriver

from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://computer-database.gatling.io/computers')

def test_player():
    assert True

time.sleep(2)
driver.refresh()


# As a User I want to be able to add a NEW Computer
addNewComputer = driver.find_element_by_xpath('//*[@id="add"]').click()


# As a User When I add a computer, I want to define it's registration
computerName = driver.find_element_by_xpath('//*[@id="name"]')
computerName.send_keys('AZAR')

time.sleep(2)

computerIntroduced = driver.find_element_by_xpath('//*[@id="introduced"]')
computerIntroduced.send_keys('2020-01-01')

time.sleep(2)

computerDiscontinued = driver.find_element_by_xpath('//*[@id="discontinued"]')
computerDiscontinued.send_keys('2020-09-01')

Create = driver.find_element_by_xpath('//*[@id="main"]/form/div/input').click()
def test_player():
    assert True


#validate that filter works
filterbyName = driver.find_element_by_xpath('//*[@id="searchbox"]')
filterbyName.send_keys('AZAR')
filterSearch = driver.find_element_by_xpath('//*[@id="searchsubmit"]').click()

def test_whatever(self):
    assert False

    time.sleep(3)
    driver.refresh()


homePage = driver.find_element_by_xpath('/html/body/header/h1/a').click()

time.sleep(3)
#validate that user can delete existing computer on database
acerIconia = driver.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[4]/td[1]/a').click()

editComputer = driver.find_element_by_xpath('//*[@id="main"]/form[2]/input').submit()

filterbyName = driver.find_element_by_xpath('//*[@id="searchbox"]')
filterbyName.send_keys('Acer Iconia')
filterSearch = driver.find_element_by_xpath('//*[@id="searchsubmit"]').click()


def test_whatever(self):
    assert False







