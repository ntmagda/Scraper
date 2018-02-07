from selenium import webdriver
import time

from download_images_from_website import GetImagesLinks, download_file
url = "http://www.galerie-zdjec.pl/aktualnosci/czarowne-lato-white-alice-relacja-edycji-lipcowej-2013/attachment/03_wa-wrzesien"
driver = webdriver.Chrome()
driver.get(url)
images_to_download = []
limit = 100
lastHeight = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    newHeight = driver.execute_script("return document.body.scrollHeight")
    src = driver.page_source
    images_to_download = GetImagesLinks(src, url)
    if newHeight == lastHeight or len(images_to_download)> limit:
        for image in images_to_download[:limit]:
            download_file(image, target_folder='images/')
        break
    lastHeight = newHeight