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
    #Function to look for the searchbar, clicks it, sends a string to it and confirms using Enter    time.sleep(2)
    print('Looking for searchbar')
    search = driver.find_element(By.CSS_SELECTOR, "div[title='Tekstvak zoekopdracht']")
    actions.move_to_element(search).click().pause(1).send_keys(line).send_keys(Keys.ENTER).perform()
    print('Searchbar found')

def Clear_Search():
        zoekenannuleren = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Zoeken annuleren']")
        actions.move_to_element(zoekenannuleren).click().perform()

def No_Chats_Found():
    #A function that checks if a chat has been found(False) or no chat has been found(True)
    print('Looking for chats/groups')
    time.sleep(2)
    try:
        nochatsfound = driver.find_element(By.XPATH, "//span[contains(text(), 'Geen chats')]")
    except:    
        return False
    else:
        if nochatsfound.is_displayed():
            print(f'Unable to find {line} in chatlist, continuing with the next group from list.')
            time.sleep(2)
            Clear_Search()
            time.sleep(2)
            return True

def Open_Menu():
    #A function that looks for the Menu and clicks it
    print('Looking for menu button')
    time.sleep(2)
    #this finds the instance of the menu button
    menu = driver.find_element(By.CSS_SELECTOR, "div[role='button'][data-tab='6'][title='Menu']")
    #This moves the cursor to the menu button and clicks it
    actions.move_to_element(menu).click().perform()
    print('opened menu')

def Look_For_Groupinfo():
    #A function that looks for the Groupinfo item and clicks it
    print('Looking for groupinfo button')
    time.sleep(2)
    try:
        groupinfo = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Groepsinformatie']")
    except:
        return False
    else:
        actions.move_to_element(groupinfo).click().perform()
        print('Opened groupinfo 1')
        return True
    
def Find_Add_Member_Button():
    #A function that checks if the Add member button is present, clicks it and sends it the contact to be added if so. 
    #In case it is not present, it clears the search bar and exits the function
    time.sleep(2)
    print('Looking for add member button')
    try:
        Add = driver.find_element(By.XPATH, "*//div[contains(text(),'Lid toevoegen')]")
    except:
        print(f'Unable to add member, Add button not found')
        Clear_Search()
        return False
    else:
        time.sleep(2)
        actions.move_to_element(Add).click().perform()
        actions.send_keys(contact_name).pause(1).send_keys(Keys.ENTER).perform()
        print('Opened Add member button 1')
        time.sleep(2)
        return True
    

def Member_In_Group():   
        #This Function checks if the contact is already in the group, closes the window and clears the searchbar if so.
        #Returns False if contact is not in group
        print('Checking if member allready in group')
        searchresultlist = driver.find_element(By.XPATH, "//div[@class='g0rxnol2 g0rxnol2 thghmljt p357zi0d rjo8vgbg ggj6brxn f8m0rgwh gfz4du6o ag5g9lrv bs7a17vp']")
        isadded = searchresultlist.find_element(By.CLASS_NAME, 'vQ0w7')
        if isadded.get_property('innerText') == 'Al toegevoegd aan groep':
            print(f'{contact_name} already member of {line} 1')
            time.sleep(2)
            closewindow = driver.find_element(By.CSS_SELECTOR, "div[role='button'][aria-label='Sluiten']")
            actions.move_to_element(closewindow).click().perform()
            time.sleep(2)
            Clear_Search()
            return True    
        else:
            return False

            
        
def Member_not_in_group():
    #This Function confirms twice the addition of the contact into the group and clears the searchbar achterwards
    print('Adding member to group')
    confirm = driver.find_element(By.CSS_SELECTOR, "span[aria-label='Bevestigen']")
    actions.move_to_element(confirm).click().perform()
    time.sleep(2)    
    confirm2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button[2]')
    actions.move_to_element(confirm2).click().perform()
    time.sleep(2)
    print('Member added to group succesfully')



def Make_Member_Admin():
    print('Making member Admin')
    time.sleep(2)
    #This function makes a member of a group an admin
    MemberList = driver.find_element(By.XPATH, "//div[@class='gsqs0kct oauresqk efgp0a3n tio0brup g0rxnol2 tvf2evcx oq44ahr5 lb5m6g5c brac1wpa lkjmyc96 i4pc7asj bcymb0na przvwfww e8k79tju']")
    Contact = MemberList.find_element(By.CSS_SELECTOR, f"span[title='{contact_name}']")
    actions.move_to_element(Contact).context_click().perform()
    time.sleep(2)
    MakeAdmin = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Groepsbeheerder maken']")
    actions.move_to_element(MakeAdmin).click().perform()
    time.sleep(2)
    confirmwindow = driver.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]')
    confirmbutton = confirmwindow.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div/button[2]')
    actions.move_to_element(confirmbutton).click().perform()
    time.sleep(2)
    Clear_Search()
    print('Member made Admin succesfully')




# For loop that goes through a list of groups/chats/contacts an checks if contact is already in a group. 
#Adds it in case it is not in the group
for line in myfile:
    Search()
    print('Searchbar found 2')
    if No_Chats_Found():
        print('No group/chat found')
        failed.write(f'{line}> no group found\n')
        continue
    else:
        Open_Menu()
        if Look_For_Groupinfo():
            if Find_Add_Member_Button():
                if Member_In_Group():
                    print('Member allready in group')
                    failed.write(f'{line} > Contact allready in group')
                    continue
                else:
                    print('Member not in group 2')
                    Member_not_in_group()
                    Make_Member_Admin()
                    success.write(line)
            else:
                print('Could not find add button')
                failed.write(f'{line} > Unable to find add member button\n')
                continue

        else:
            #If the item groupinfo has not been found, either due to the chat being a direct contact or any other reason, the searchbar will me cleared and selected and the result written to a file. Loop continues
            Clear_Search()
            print('Groupinfo not found')
            failed.write(f'{line} > groupinfo not found\n')
            continue
else:
    print('finised, check success.txt and failed.txt for the results.')
    failed.close()
    success.close()
    myfile.close()
    driver.quit()
