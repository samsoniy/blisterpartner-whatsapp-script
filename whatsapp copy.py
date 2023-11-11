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
scroll_height = driver.execute_script('return document.scrollTop', chatlist)
#gets the current scrolled position
chatelement_scrollheight = driver.execute_script("return window.pageYOffset", chatlist)

myfile = open('chats.txt', 'a',newline='\n')
readmyfile = open('chats.txt ','r')
                  
#function to find chats and get the chat name, check if it starts with a + and adds it to file containing chat names if true
def get_chatnames(chatlist):
    #len(all_elements) is 15. After looping 15 times the function should stop.
    counts = 0

    all_elements = driver.find_elements(By.CLASS_NAME, '_21S-L')

    #finds all instances of the element holding the chat title in current viewport
    for element in all_elements:
        counts += 1
        print(counts)
        firstelement = element.find_element(By.TAG_NAME, 'span')
        title = firstelement.get_attribute('title')
        if counts == 16:
            break
        elif title in readmyfile:
            continue
        elif not title.startswith('+') and title not in readmyfile:
            print(f'{title} has been added to the list\n')
            try:
                myfile.write(title+'\n')
            except:
                UnicodeEncodeError

        elif title.startswith('+'):
            pass
    else:
        pass



while True:
        driver.execute_script(f'document.querySelector("#pane-side").scrollBy(0,404)')
        get_chatnames(chatlist)
        time.sleep(1)



