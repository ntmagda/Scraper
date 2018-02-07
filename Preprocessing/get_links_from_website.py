from bs4 import BeautifulSoup
import urllib.request
import re
import requests

url = "https://www.google.pl/search?q=magda+nowak+trzos&dcr=0&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi77tmSr4DZAhXKhqYKHTmpCdQQ_AUICigB&biw=1396&bih=668"
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")

for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    print( link.get('href'))