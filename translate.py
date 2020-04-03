#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import sys

def download_content(url):
	header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
	res = requests.get(url, headers=header)
	return res.content	

def get_website_content(word):
    html = download_content("https://dictionary.cambridge.org/us/dictionary/english-chinese-traditional/" + word)
    soup = BeautifulSoup(html, 'html.parser')

    return soup

def get_result(soup):
    bodies = soup.findAll("div", {"class": "def-block"})

    text = ""
    i = 1

    # Get definition of the word
    for body in bodies:
        eng_def = body.find("div", {"class": "def"}).getText().strip('\n')
        zh_tw_def = body.find("span", {"class": "trans"}).getText().strip('\n')
        text = text + str(i) + "." + zh_tw_def + "\\n" + eng_def + "\\n"
        i = i + 1		

    return text

if __name__ == '__main__':
    word   = sys.argv[1].strip()
    soup   = get_website_content(word)
    result = get_result(soup)
    
    print (result)
