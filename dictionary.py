import requests
import sys
from bs4 import BeautifulSoup as bs


try:
    word = sys.argv[1]
except:
    print("Error: No word provided!")
    exit(-1)

url = 'https://www.dictionary.com/browse/' + word

try:
    r = requests.get(url)
except:
    print("Error: No internet connection!")
    exit(-1)

soup = bs(r.content, 'lxml')

try:
    header = soup.findAll("span", {'class': 'luna-pos'})
    word_type = header[0].text
    meanings_ol = soup.findAll('ol')[0]
    meanings = meanings_ol.findChildren('li', recursive=False)
except:
    print("Error: Word not found!")
    exit(-1)

print()
print (word + ": " + word_type)
for (i,meaning) in enumerate(meanings):
    print (str(i + 1)+ "." + meaning.text)