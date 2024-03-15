from urllib.request import urlopen
import re

url = 'http://olympus.realpython.org/profiles/dionysus'

page = urlopen(url) # открываем урл
http_bytes = page.read() # читаем урл
http = http_bytes.decode('utf-8') # декодим урл
expression = '<.*title.*>.*<.*title.*>' # составляем выражение для поиска
title_math = re.search(expression, http, re.IGNORECASE) # ищем title
title_with_tag = title_math.group() #  берем строку из Math
title = re.sub('<.*?>','', title_with_tag) # заменяем теги на пустые символы
print(title)