import mechanicalsoup
import time

url = 'http://olympus.realpython.org/dice'
browser = mechanicalsoup.Browser()
counter = 1

for i in range(4):
    page = browser.get(url)
    html = page.soup
    result = html.select('#result')[0]
    timestamp = html.select('#time')[0]
    print(f'For {counter} time you have result: "{result.text}" in datetime: {timestamp.text}')
    counter = counter + 1
    if i < 3:
        time.sleep(5)