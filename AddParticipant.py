from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

contact_name= input('Which contact needs to be added?')

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get('https://web.whatsapp.com/')
actions = ActionChains(driver)

WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[title='Tekstvak zoekopdracht']")))
myfile = open('chats.txt', 'r')
success = open('success.txt', 'a')
failed = open('failed.txt', 'a')

def Search():
    print('Moving to search bar')
    time.sleep(2)
    #This looks for the searchbar
    search = driver.find_element(By.CSS_SELECTOR, "div[title='Tekstvak zoekopdracht']")
    #This moves the cursor to the searchbar, clicks it
    actions.move_to_element(search).click().pause(1).send_keys(line).send_keys(Keys.ENTER).perform()
    print('Searchbar found')

def No_Chats_Found():
    print('Looking for chats')
    time.sleep(2)
    try:
        nochatsfound = driver.find_element(By.XPATH, "//span[contains(text(), 'Geen chats')]")
    except:    
        print('found group 1')
        return False
    else:
        if nochatsfound.is_displayed():
            print(f'Unable to find {line} in chatlist, continuing with the next group from list.')
            time.sleep(2)
            zoekenannuleren = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Zoeken annuleren']")
            actions.move_to_element(zoekenannuleren).click().perform()
            time.sleep(2)
            return True

def Open_Menu():
    print('Looking for menu button')
    time.sleep(2)
    #this finds the instance of the menu button
    menu = driver.find_element(By.CSS_SELECTOR, "div[role='button'][data-tab='6'][title='Menu']")
    #This moves the cursor to the menu button and clicks it
    actions.move_to_element(menu).click().perform()
    print('opened menu 1')

def Look_For_Groupinfo():
    print('Looking for groupinfo button')
    time.sleep(2)
    try:
        #this looks for the element of groupinformation
        groupinfo = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Groepsinformatie']")
    except:
        zoekenannuleren = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Zoeken annuleren']")
        actions.move_to_element(zoekenannuleren).click().perform()
        return False
    else:
        actions.move_to_element(groupinfo).click().perform()
        print('Opened groupinfo 1')
        return True
    
def Find_Add_Member_Button():
    time.sleep(1)
    print('Looking for add member button')
    try:
        Add = driver.find_element(By.XPATH, "*//div[contains(text(),'Lid toevoegen')]")
    except:
        print(f'Unable to add member, Add button not found')
        zoekenannuleren = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Zoeken annuleren']")
        actions.move_to_element(zoekenannuleren).click().perform()
        return False
    else:
        time.sleep(2)
        actions.move_to_element(Add).click().perform()
        actions.send_keys(contact_name).pause(1).send_keys(Keys.ENTER).perform()
        print('Opened Add member button 1')
        time.sleep(2)
        return True
    

def Member_In_Group():   
        #This checks if the new member is already in the group
        print('Checking if member allready in group')
        searchresultlist = driver.find_element(By.XPATH, "//div[@class='g0rxnol2 g0rxnol2 thghmljt p357zi0d rjo8vgbg ggj6brxn f8m0rgwh gfz4du6o ag5g9lrv bs7a17vp']")
        isadded = searchresultlist.find_element(By.CLASS_NAME, 'vQ0w7')
        if isadded.get_property('innerText') == 'Al toegevoegd aan groep':
            print(f'{contact_name} already member of {line} 1')
            time.sleep(1)
            closewindow = driver.find_element(By.CSS_SELECTOR, "div[role='button'][aria-label='Sluiten']")
            actions.move_to_element(closewindow).click().perform()
            time.sleep(1)
            zoekenannuleren = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Zoeken annuleren']")
            actions.move_to_element(zoekenannuleren).click().perform()
            return True    
        else:
            print('Member not in group')
            return False

            
        
def Member_not_in_group():
    print('Adding member to group')
    confirm = driver.find_element(By.CSS_SELECTOR, "span[aria-label='Bevestigen']")
    actions.move_to_element(confirm).click().perform()
    print('Confirmed first time')
    time.sleep(2)    
    confirm2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button[2]')
    actions.move_to_element(confirm2).click().perform()
    print('Confirmed second time')
    time.sleep(2)
    print('Member added to hroup succesfully')
    zoekenannuleren = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Zoeken annuleren']")
    actions.move_to_element(zoekenannuleren).click().perform()



for line in myfile:
    Search()
    print('Searchbar found 2')
    if No_Chats_Found():
        print('No group/chat found')
        failed.write(f'{line}> no group found\n')
        continue
    else:
        print('Found a chat 2')
        Open_Menu()
        print('Opened menu 2')
        if Look_For_Groupinfo():
            print('Opened group info 2')
            if Find_Add_Member_Button():
                print('Opened Add member button 2')
                if Member_In_Group():
                    print('Member allready in group 2')
                else:
                    print('Member not in group 2')
                    Member_not_in_group()
            else:
                print('Could not find add button 2')
        else:
            print('Groupinfo not found')
            failed.write(f'{line} > groupinfo not found\n')
            continue


else:
    print('finised, check success.txt and failed.txt for the results.')
