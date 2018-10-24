# Web scraping with requests & Beautiful Soup
import re
import requests
from bs4 import BeautifulSoup
import time

url = "http://www.faz.net/aktuell/politik/ausland/nach-may-attacke-lobt-trump-beziehungen-zu-grossbritannien-15689296.html"

time.sleep(1)
site = requests.get(url)
page_content = BeautifulSoup(site.content, "html.parser")
introtext = page_content.find("p", class_ = "atc-IntroText").string.strip()
partext_container = page_content.find("div", class_ = "atc-text").find_all("p", class_ = re.compile("atc-"))

print(introtext + "\n")
for par in partext_container:
    print(par.text)