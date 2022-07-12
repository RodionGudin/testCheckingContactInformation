from selenium import webdriver
from selenium.webdriver.common.by import By

try:

	browser = webdriver.Chrome()
	browser.implicitly_wait(5)

	browser.get("https://www.google.ru/")
	
	googleSearch = browser.find_element(By.NAME, "q")
	googleSearch.send_keys("Byndyusoft")
	

	browser.find_element(By.NAME, "btnK").click()

	browser.find_element(By.XPATH, "//h3[contains(text(),'Byndyusoft')]").click()
	
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)

	#yellowButton
	
	browser.find_element(By.CSS_SELECTOR, ".know-more .btn").click()
	
	#check phone and email

	phoneNumber = "8 800 775-15-21"
	phoneNumberOnPage = browser.find_element(By.XPATH, "//div[@class='popup-callback__footer-contacts']//a[contains(@href,'tel:88007751521')]").text
	assert phoneNumberOnPage == phoneNumber, \
            f"The phone number is not correct: '{phoneNumberOnPage}' instead of '{phoneNumber}'"
	
	
	email = "sales@byndyusoft.com"
	emailOnPage = browser.find_element(By.XPATH, "//div[@class='popup-callback__footer-contacts']//a[contains(@href,'mailto:sales@byndyusoft.com')]").text
	assert emailOnPage == email, \
            f"The Email is not correct: '{emailOnPage}' instead of '{email}'"	


finally:
	
	browser.quit()
