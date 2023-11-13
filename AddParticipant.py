from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get('https://web.whatsapp.com/')
actions = ActionChains(driver)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"(//p[@class='selectable-text copyable-text iq0m558w g0rxnol2'])[1]")))

search = driver.find_element(By.XPATH,"(//p[@class='selectable-text copyable-text iq0m558w g0rxnol2'])[1]")

actions.move_to_element(search).click().send_keys('testgroep'+Keys.ENTER).perform()
menu = driver.find_element(By.XPATH, "(//div[@title='Menu'])[2]")
groupinfo = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Groepsinformatie'")

actions.move_to_element(menu).click().move_to_element(groupinfo).perform()
Add = driver.find_element(By.CSS_SELECTOR, '._8nE1Y[shub-ins="1"]')
WebDriverWait(driver, 20).until(EC.presence_of_element_located(Add))
actions.move_to_element(Add).click().send_keys('Geoffrey Hoedt'+Keys.ENTER)
confirm = driver.find_element(By.CSS_SELECTOR, "span[aria-label='Bevestigen']")
confirm2 = driver.find_element(By.CSS_SELECTOR, ".tvf2evcx.m0h2a7mj.lb5m6g5c.j7l1k36l.ktfrpxia.nu7pwgvd.p357zi0d.dnb887gk.gjuq5ydh.i2cterl7.i6vnu1w3.qjslfuze.ac2vgrno.sap93d0t.gndfcl4n[shub-ins='1']")

actions.move_to_element(confirm).click().move_to_element(confirm2).click()
time.sleep(4)