from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib
import requests
import os
import time

## Path to folder
path = '/PATH/LIKE/THIS/'
## Link to Duck Duck Go image Search
url = 'https://duckduckgo.com/?q=house+fire&t=h_&iar=images&iax=images&ia=images'
## Name of the images downloader
name = 'NAME'
DRIVER_PATH = 'DRIVER/PATH/LIKETHIS'
driver = webdriver.Chrome(DRIVER_PATH)
driver.get(url)

try:
    zci = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "zci-images"))
    )

    urls = zci.find_elements_by_tag_name('img')
    counter = 0
    for page in urls:
        link = page.get_attribute('src')
        urllib.request.urlretrieve(link,os.path.join(path, name+str(counter)+'.png'))
        counter = counter + 1
finally:
    driver.quit()

