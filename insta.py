from selenium import webdriver
import time

PATH='/home/nagul/Downloads/chromedriver'

driver=webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/")
time.sleep(25)

# locate email form by_class_name
username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')


# send_keys() to simulate key strokes
username.send_keys('nagul_02')
password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

# send_keys() to simulate key strokes
password.send_keys('Nagul12/08/2002')
log_in_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
log_in_button.click()
time.sleep(10)
# locate search form

search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')


# send_keys() to simulate key strokes
search.send_keys('prash_prakash_')
click = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[2]/div')
click.click()