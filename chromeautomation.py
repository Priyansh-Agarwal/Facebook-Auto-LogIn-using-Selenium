from selenium import webdriver

driver = webdriver.Chrome()

#open facebook
driver.get("HTTPS://facebook.com")
#Enters emailID
the_emailID = driver.find_element_by_xpath('//*[@id="email"]')
the_emailID.send_keys("#your Email ID")

#enters password
the_password =driver.find_element_by_xpath('//*[@id="pass"]')
the_password.send_keys("your Password")

#clicks login button
login = driver.find_element_by_xpath('//*[@id="u_0_b"]')
login.click()

