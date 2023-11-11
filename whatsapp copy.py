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
WebDriverWait(driver, 15)
actions = ActionChains(driver)

# this tells the script to wait until the search bar has been fully loaded
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[1]/div/div[2]/button/div[2]")))

#This finds the element the chats are contained in
chatlist = driver.find_element(By.ID,'pane-side')

#gets the current height of the element the chats are in
chatelement_height = chatlist.get_property("clientHeight")

chatelement_scrollheight = chatlist.get_property("scrollHeight")

#function to find chats and get the chat name, check if it starts with a + and adds it to file containing chat names if true
def get_chatnames():
    #finds all instances of the element holding the chat title in current viewport
    all_elements = driver.find_elements(By.CLASS_NAME, '_21S-L')
counts = 0

    #For loop to go over every instance of a chat found and get the title
    for element in all_elements:
        firstelement = element.find_element(By.TAG_NAME, 'span')
        title = firstelement.get_attribute('title')
        if not title.startswith('+'):
            counts += 1
myfile = open('groupchat.txt', 'a')
            myfile.write(title)
myfile.close()
            print(f'{title} has been added to the list')
        else:
print(f'{counts} groups have been added to the list.')
#scrolls down in the element holding the chats
driver.execute_script('document.getElementById("pane-side").scrollTop += clientHeight', "")
break

while driver.execute_script('document.getElementById('pane-side').scrollTop') != chatelement_scrollheight:
get_chatnames(chatlist)
else:
print('The bottom of the active chat list has been reached and all groups should have been added.')
break




