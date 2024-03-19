from urllib.request import urlopen
import re

url = 'http://olympus.realpython.org/profiles/dionysus'
html = urlopen(url).read().decode()
#print(html)

# name_start = html.find('Name:')+len('Name: ')
# name_end = html.find('</h2>')
# name = html[name_start:name_end]
# print(name)
# color_start = html.find('Favorite Color: ')+len('Favorite Color: ')
# color_end = html.find('</center>')
# color = html[color_start:color_end]
# print(color)

pattern_1 = 'Name:.*<'
name_math = re.search(pattern_1, html, re.IGNORECASE)
name_tags =name_math.group()
name_withoit_name = re.sub('Name:','',name_tags)
name = (re.sub('<','',name_withoit_name)).strip()
print(name)

pattern_2 = 'Favorite Color:.*'
color_math = re.search(pattern_2, html, re.IGNORECASE)
color_with_name = color_math.group()
color = re.sub('Favorite Color:','', color_with_name)
print(color.strip())