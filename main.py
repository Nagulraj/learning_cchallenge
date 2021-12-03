
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/home/nagul/Downloads/chromedriver')
driver.get('https://www.linkedin.com')
sleep(5)

username = driver.find_element_by_xpath('//*[@id="session_key"]')
username.send_keys('thangarajnagulraj@gmail.com')
sleep(0.5)

password = driver.find_element_by_xpath('//*[@id="session_password"]')
password.send_keys('Nagul12/08/2002')
sleep(0.5)

sign_in_button = driver.find_element_by_xpath('/html/body/main/section[1]/div/div/form/button')
sign_in_button.click()
sleep(5)

driver.get('https://www.google.com')
sleep(3)

search_query = driver.find_element_by_name('q')
search_query.send_keys('site:linkedin.com/in/ AND "python developer"')
sleep(0.5)

search_query.send_keys(Keys.RETURN)
sleep(3)

linkedin_urls = driver.find_elements_by_class_name('iUh30')
linkedin_urls = [url.text for url in linkedin_urls]
sleep(0.5)

print(linkedin_urls)
f=open("link.csv",'w')
for i in linkedin_urls:
    f.writelines(i)
f.close()
