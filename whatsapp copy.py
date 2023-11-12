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

# this tells the script to wait until the search bar has been fully loaded
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".to2l77zo")))

#This finds the element the chats are contained in
chatlist = driver.find_element(By.ID,'pane-side')
#gets the visible height of the element the chats are in
client_height = chatlist.get_property("clientHeight")
#gets the total scrollheight of the window
totalheight = driver.execute_script('return document.querySelector("#pane-side").scrollHeight')

scroll = driver.execute_script('return document.querySelector("#pane-side").scrollTop')

#function to find chats and get the chat name, check if it starts with a + and adds it to file containing chat names if true
def get_chatnames(chatlist):
    test = []

    #finds all instances of the element holding the chat title in current viewport:
    all_elements = driver.find_elements(By.CLASS_NAME, '_21S-L')
    for element in all_elements:
        firstelement = element.find_element(By.TAG_NAME, 'span')
        title = firstelement.get_attribute('title')
        if not title.startswith('+') and title not in test:
            test.append(title)
            print(f'{title} has been added to the list\n')
        else:
            pass
    else:
        driver.execute_script(f'document.querySelector("#pane-side").scrollBy(0,806)')
        for i in test:
            try:
                with open('chats.txt', 'a') as myfile:
                    myfile.write(i+'\n')
            except:
                UnicodeEncodeError
        else:
            myfile.close()


while True:
    get_chatnames(chatlist)

