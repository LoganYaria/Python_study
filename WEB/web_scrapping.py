from urllib.request import urlopen

url = 'http://olympus.realpython.org/profiles/aphrodite'
#url = 'http://olympus.realpython.org/profiles/poseidon'
page = urlopen(url) #возвращает HTTPResponse object
html_bytes = page.read() # возвращает последовательность байтов
html = html_bytes.decode('utf=8') # декодирует html_bytes и структурирует текст Тип - строка
title_start = html.find('<title>')+len('<title>') # находим начало тега тайтл и прибавляем самое наименование тега
title_end = html.find('</title>') #находим конец тега
title = html[title_start:title_end] # срез заголовка
print(title)
