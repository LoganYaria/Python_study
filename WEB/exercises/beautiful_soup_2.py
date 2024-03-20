from bs4 import BeautifulSoup
from urllib.request import urlopen
from pathlib import Path

url = 'http://olympus.realpython.org/profiles'
html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
file_path = Path.cwd()/'scrapped.txt'

links = soup.find_all('a')
#print(links)
links_address = []
for link in links:
    links_address.append(link['href'])
print(links_address)
url_pt_1 = 'http://olympus.realpython.org'
for link in links_address:
    full_url = url_pt_1+link
    html_1 = urlopen(full_url).read().decode('utf-8')
    soup_1 = BeautifulSoup(html_1, 'html.parser')
    text_html = soup_1.get_text()
    #print(text_html)
    replaced_text_html = text_html.replace('''\n\n''',' ')
    with file_path.open(mode='a', encoding='utf-8') as file:
        file.write(text_html)