from selenium import webdriver 

from selenium.webdriver.common.keys import Keys 

browser= webdriver.Firefox() 
browser.get("https://dropbox.com/register") 

list_of_inputs = browser.find_elements_by_xpath("//div/input[starts-with(@id, 'pyxl')]") 
list_of_inputs[7].send_keys("first name") 
list_of_inputs[8].send_keys("last name") 
list_of_inputs[9].send_keys("email") 
list_of_inputs[10].send_keys("password") 
list_of_inputs[11].click() 

password.send_keys(Keys.RETURN)

