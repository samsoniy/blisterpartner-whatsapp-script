from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
    
chats = []

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 20)
actions = ActionChains(driver)

# this tells the script to wait until the search bar has been fully loaded and after that wait another 3 seconds to be sure
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[1]/div/div[2]/button/div[2]")))
time.sleep(5)

#This finds the element the chats are contained in and scrolls down to the bottom of the element to load all chats into its memory
scroll = driver.find_element(By.ID,'pane-side')

counts = 1

while True:
    #finds all chats instances according to their CSS Class and stores them in a variable
    all_elements = driver.find_elements(By.CLASS_NAME, '_21S-L')
    #For loop to go over every instance of a chat found and takes the groupname and adds it to a list
    for element in all_elements:
        firstelement = element.find_element(By.TAG_NAME, 'span')
        title = firstelement.get_attribute('title')
        if not title.startswith('+') and title not in chats:
            counts += 1
            chats.append(title)
            print(f'{title} has been added to the list')
    else:
        print(f'No more elements found. {counts} groups have been added to the list')
        with open('groupchats.txt', 'a') as myfile:
            for i in chats:
                try:
                    myfile.write(i + '\n')
                except:
                    pass


    scroll_height = scroll.get_property("clientHeight")
    driver.execute_script('document.getElementById("pane-side").scrollTop += ' + str(scroll_height), "")
    time.sleep(1)
