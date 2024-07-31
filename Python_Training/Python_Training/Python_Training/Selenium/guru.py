from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Python_Training import SeleniumBaseExample

selenium_base = SeleniumBaseExample()
driver = selenium_base.selenium_start("https://demo.guru99.com/test/newtours/reservation.php")
driver.implicitly_wait(10)
# sleep(20)
type_Trip = driver.find_elements(By.NAME ,"tripType")
type_Trip[1].click()
driver.implicitly_wait(2)

amount_of_Passengers = Select(driver.find_element(By.NAME, "passCount"))
amount_of_Passengers.select_by_index(3)
driver.implicitly_wait(2)

departing_From = Select(driver.find_element(By.NAME, "fromPort"))
departing_From.select_by_index(2)
driver.implicitly_wait(2)

departing_From_On = Select(driver.find_element(By.NAME, "fromMonth"))
departing_From_On.select_by_index(6)
driver.implicitly_wait(2)

departing_To = Select(driver.find_element(By.NAME, "toPort"))
departing_To.select_by_index(9)

service_Class = Select(driver.find_elements(By.NAME, "servClass"))
service_Class[2].click



passCount = Select(By.NAME,"passCount")
passCount



selenium_base.selenium_end(driver)