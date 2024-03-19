from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://olympus.realpython.org/profiles/dionysus'
page = urlopen(url)
html = page.read().decode('utf-8')
print(html)
soup = BeautifulSoup(html,'html.parser')

text = soup.get_text() # .get_text() извлекает весь текст из страницы и удаляет теги
# # print(text) # .replace() для удаления enterов
# # .find проще использовать с пакетом BS чем re
list_img_link = soup.find_all('img') # вернет сущность всех тегов img в списке
# #print(list_img_link)
# #print(type(list_img_link[0])) # в списке возвр объекьы кдасса bs4.element.Tag , не str
image_1,image_2 = list_img_link # распаковка списка
print(image_1.name) # .name свойство возвращает тип тега
print(image_1['src']) # <img src="/static/dionysus.jpg" /> обращение к атрибуту src тега
print(soup.title) # к некоторым тегам можно обращаться через свойства, при том BS подчистит тег от лишних знаков
print(soup.h2)
print(soup.title.string)# получить строку между тегами заголовка
print(soup.find_all('img',src='/static/dionysus.jpg')) #для поиска конкретного тега с опр св-вами