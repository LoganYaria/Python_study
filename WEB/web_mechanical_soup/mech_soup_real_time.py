import mechanicalsoup
import time


url = 'http://olympus.realpython.org/dice'

browser = mechanicalsoup.Browser()
# page = browser.get(url)
# html = page.soup

# # Через MS
for i in range(4):
    page = browser.get(url)
    html = page.soup
    tag = html.select('#result')[0]
    result = tag.text
    print(result)
    if i<3:
        time.sleep(10) # засыпаем процесс на 10 секунд
# # Через BS
# print(html)
# result = html.h2.string
# print(result)

