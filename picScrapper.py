from time import sleep
from urllib.request import urlretrieve
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://sweet-regina.kyte.site/")

for i in range(500):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)

r=driver.find_elements_by_tag_name('img')
i = 0
for img in r:
    try:
        src = img.get_attribute("src")
        urlretrieve(src, "sweetReginaPhotos/"+img.get_attribute("alt")+".png")
        print(img.get_attribute("alt")+".png")
    except:
        print("xd")

driver.close()