from selenium import webdriver
from selenium.webdriver.common.by import By

import time

def scrap_data(link="", next_xpath=""):
    #initialize chrome dengan spesifikasi tertentu
    driver = webdriver.Firefox()

    #navigate ke glassdoor
    driver.get(link)

    time.sleep(15)

    #list of tech company in jakarta
    company_list = []

    #selama masih ada next button di pagination
    while(1):
        time.sleep(10)
        #untuk menampung text dari content 
        temp = []
        
        index = 1
        
        #ambil 10 div didalam content
        while(index < 12):
            try:
                child_div = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div/div[3]/div[" + str(index) + "]")
                if(child_div.text == ""):
                    index += 1
                    continue
                temp.append(child_div.text)
            except:
                index += 1
                continue
            index += 1

        #tambahkan semua text company yang sudah tercatat ke company_list
        company_list.append(temp)

        if(next_xpath == None):
            break

        try:
            driver.find_element(By.XPATH, next_xpath).click()
        except:
            break

    driver.quit()

    return company_list