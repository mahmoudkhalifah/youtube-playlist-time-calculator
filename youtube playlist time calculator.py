from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

def openWebpage(url):
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get(url)
    time.sleep(3)
    return driver

def scrollToEndOfPage():
    scrollHeight = 1200
    maxHeight = int(driver.find_element(by= By.TAG_NAME,value='ytd-browse').size["height"])
    while scrollHeight < maxHeight:
        driver.execute_script(f'window.scrollTo(0,{scrollHeight});')
        if(scrollHeight + 600 >=maxHeight):
            time.sleep(1)
        if(maxHeight!= int(driver.find_element(by= By.TAG_NAME,value='ytd-browse').size["height"])):
            maxHeight = int(driver.find_element(by= By.TAG_NAME,value='ytd-browse').size["height"])
        scrollHeight+=600

def calculateTotalTime():
    mins = 0
    secs = 0
    for time in driver.find_elements(by= By.CLASS_NAME,value='ytd-thumbnail-overlay-time-status-renderer'):
        if(time.text!=""):
            splitted_time_string = time.text.split(":")
            mins += int(splitted_time_string[0])
            secs += int(splitted_time_string[1])
    mins+= int(secs/60)
    secs%=60
    hours = int(mins/60)
    mins%=60
    return hours,mins,secs


if __name__ == "__main__":
    url = input("enter playlist's url: ")
    driver = openWebpage(url=url)
    scrollToEndOfPage()
    hours,mins,secs = calculateTotalTime()
    print(f'total time is: {hours:02d}:{mins:02d}:{secs:02d}')
    driver.close()
    input("Press any key to close")





