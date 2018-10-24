# coding=utf-8
# First try of web scraping with requests and Beautiful Soup
# coding: utf-8
from bs4 import BeautifulSoup
import re
import requests
import textwrap
import time

# urls = ["http://www.faz.net/aktuell/politik/ausland/trump-baby-ueber-london-ein-willkommen-auf-die-britische-art-15689150.html",
#         "http://www.faz.net/aktuell/wirtschaft/diginomics/elon-musk-soll-mehr-arbeiten-sagt-investor-james-anderson-15688188.html",
#         "http://www.faz.net/aktuell/politik/sami-a-ex-leibwaechter-von-bin-ladin-abgeschoben-15689217.html",
#         "http://www.faz.net/aktuell/stil/essen-trinken/sternekoch-schanz-zaubert-fremde-galaxien-an-die-mosel-15688374.html",
#         "http://www.faz.net/aktuell/finanzen/finanzmarkt/so-wichtig-ist-amerika-fuer-die-dax-konzerne-15688430.html"
#         ]
# counter = 0
url = "http://www.faz.net/aktuell/wirtschaft/diginomics/elon-musk-soll-mehr-arbeiten-sagt-investor-james-anderson-15688188.html"
regex = re.compile("atc-")
#url = "http://www.faz.net/aktuell/politik/ausland/trump-baby-ueber-london-ein-willkommen-auf-die-britische-art-15689150.html"

# Wait a second to prevent over-requesting
# Make a GET request against the current URL
# Get source code from the response object
# Search for a <p> tag which contains the headline from the text
# Search for a <div> which contains various paragraphs, then print all <p> tags within this container,
# which start with "atc-"

time.sleep(1)
site = requests.get(url)
page_content = BeautifulSoup(site.content, "html.parser")
introtext = page_content.find("p", class_="atc-IntroText").string.strip()
introtext = introtext.replace(u"–", u"-").replace(u"„", u"\"").replace(u"“", u"\"")
partext_container = page_content.find("div", class_="atc-Text").find_all("p", class_=regex)

print(introtext + "\n")
for par in partext_container:
    # TODO replacement doesn't work yet
    text = par.text
    text = text.replace(u"–", u"-").replace(u"„", u"\"").replace(u"“", u"\"")
    print(textwrap.fill(par.text, 200))