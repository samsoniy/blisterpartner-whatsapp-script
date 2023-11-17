from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


contact_name = input('Which contact needs to be added?')

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get('https://web.whatsapp.com/')
actions = ActionChains(driver)

WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[title='Tekstvak zoekopdracht']")))
myfile = open('filteredchats.txt', 'r')
success = open('success.txt', 'a')
failed = open('failed.txt', 'a')

for line in myfile:

#This looks for the searchbar
    search = driver.find_element(By.CSS_SELECTOR, "div[title='Tekstvak zoekopdracht']")
    #This clears the searchbar from any text
    time.sleep(2)
    #This moves the cursor to the searchbar, clicks it, sends a string to type and presses enter to submit
    actions.move_to_element(search).click().send_keys(line).send_keys(Keys.ENTER).perform()
    time.sleep(2)
    try: 
        nochatsfound = driver.find_element(By.XPATH, "//span[contains(text(), 'Geen chats,')]")
        if nochatsfound.is_displayed():
            print(f'Unable to find {line} in chatlist, continuing with the next group from list.')
            failed.write(f'\n{line}-> Unable to find chat in chatlist.')
            time.sleep(2)
            zoekenannuleren = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Zoeken annuleren']")
            actions.move_to_element(zoekenannuleren).click().perform()
            continue
    except:
        pass
        
    try:
        #this finds the instance of the menu button
        menu = driver.find_element(By.CSS_SELECTOR, "div[role='button'][data-tab='6'][title='Menu']")
        #This moves the cursor to the menu button and clicks it
        actions.move_to_element(menu).click().perform()
        time.sleep(2)
    except:
        print(f'Unable to find menu button for {line}')
        failed.write(f'{line}-> unable to find menu button')
        continue

    try:
        #this looks for the element of groupinformation
        groupinfo = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Groepsinformatie']")
        if groupinfo.is_displayed():
            actions.move_to_element(groupinfo).click().perform()
            time.sleep(2)
            try:    
                Add = driver.find_element(By.XPATH, "//*div[contains(text(), 'Lid toevoegen')]") 
                if Add.is_displayed():
                    actions.move_to_element(Add).click().perform()
                    time.sleep(2)
                    actions.send_keys(contact_name).perform()
                    time.sleep(2)
                    try:    
                        #This checks if the new member is already in the group
                        allreadyadded = driver.find_element(By.XPATH, "//div[contains(text(), 'Al toegevoegd')]")
                        if allreadyadded:
                            print(f'User already part of {line}, continuing with the next group in the list')
                            failed.write(f'\n{line} -> User already part of group')
                            close = driver.find_element(By.CSS_SELECTOR, 'div[role="button"][aria-label="Sluiten"]')
                            actions.move_to_element(close).click().perform()
                            time.sleep(2)
                            zoekenannuleren = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Zoeken annuleren']")
                            actions.move_to_element(zoekenannuleren).click().perform()
                            time.sleep(2)
                            continue
                    except:
                        pass

                    notadded = driver.find_element(By.CSS_SELECTOR, "button[class='i5tg98hk f9ovudaz przvwfww gx1rr48f shdiholb phqmzxqs gtscxtjd ajgl1lbb thr4l2wc cc8mgx9x eta5aym1 d9802myq e4xiuwjv g0rxnol2 ln8gz9je'][ tabindex='-1'][ type='button'][ role='checkbox']")
                    actions.move_to_element(notadded).click().perform()
                    time.sleep(2)
                    confirm1 = driver.find_element(By.CSS_SELECTOR, 'span[aria-label="Bevestigen"]')
                    actions.move_to_element(confirm1).click().perform()
                    time.sleep(2)
                    confirm2 = driver.find_element(By.XPATH," //div[@class='tvf2evcx m0h2a7mj lb5m6g5c j7l1k36l ktfrpxia nu7pwgvd p357zi0d dnb887gk gjuq5ydh i2cterl7 i6vnu1w3 qjslfuze ac2vgrno sap93d0t gndfcl4n'][normalize-space()='Lid toevoegen']")
                    if confirm2.is_displayed():
                        actions.move_to_element(confirm2).click().perform()
                        print(f'Participant has been added to {line}')
                        success.write('\n'+ line)
                        zoekenannuleren = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Zoeken annuleren']")
                        actions.move_to_element(zoekenannuleren).click().perform()
                    elif not confirm2.is_displayed:
                        print(f'Unable to find the second confirm button for {line}')
                        failed.write(f'\n{line} -> unable to find second confirm button')
                        zoekenannuleren = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Zoeken annuleren']")
                        actions.move_to_element(zoekenannuleren).click().perform()
                        continue
                elif not Add.is_displayed(): 
                    print(f'Unable to add participant to {line}, as you are not an admin of this group - 1')
                    failed.write(f'\n{line}-> not an admin for group')
                    time.sleep(1)
                    zoekenannuleren = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Zoeken annuleren']")
                    actions.move_to_element(zoekenannuleren).click().perform()
                    time.sleep(2) 
                    continue
            except:
                print(f'Unable to find the add button for {line}, probably you are not an admin for this group.')
                failed.write(f'\nYou are not an admin for {line}')
                time.sleep(1)
                close = driver.find_element(By.CSS_SELECTOR, 'div[role="button"][aria-label="Sluiten"]')
                actions.move_to_element(close).click().perform()

        elif not groupinfo.is_displayed():
            print(f'Unable to find groupinformation menu for {line}, continuing with next item from the list.')
            failed.write(f'\n{line}-> Unable to find groupinformation button in menu')
            zoekenannuleren = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Zoeken annuleren']")
            actions.move_to_element(zoekenannuleren).click().perform()
            time.sleep(2)
            continue
    except:
        print(f"Unable to find groupinfo button for {line}")
        failed.write(f'{line}-> Unable to find groupinfo button')
else:
    print(f"{contact_name} has been added to all the groups in the specified list, check the failed.txt and success.txt files to check the end result")

