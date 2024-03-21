import mechanicalsoup

# <form action="/login" method="post" name="login">
# Username: <input name="user" type="text"/><br/>
# Password: <input name="pwd" type="password"/><br/><br/>
# <input type="submit" value="Submit"/>
# </form>

url = 'http://olympus.realpython.org/login'

browser = mechanicalsoup.Browser() # делаем консольный браузер
login_page = browser.get(url) # получаем страницу
# # print(login_page) # вывод кода ответа браузера
# # print(login_page.soup) # метод возвращщает объект BS и на вывод отправит html код страницы
login_html = login_page.soup

form = login_html.select('form')[0] # обращаемся к первому тегу form, найдекному в этом html
# # print(type(form))
form.select('input')[0]['value'] = 'zeus' # обращаемся и присваиваем значение zeus первому атрибуту input form
form.select('input')[1]['value'] = 'ThunderDude' # обращаемся и присваиваем значение zeus второму атрибуту input form

profile_page = browser.submit(form, login_page.url) #отправка формы (передаем заолненнуюю форму и http адрес страницы
# # print(profile_page.url)

links = profile_page.soup.select('a')# обращение ко всем ссылкам
print(links)
for link in links: # перебор ссылок
    adress = link['href'] # обращение ко всем атрибутам href
    text = link.text # обращение  к тексту в теге
    print(f'{text}: {adress}')

# # фулловые ссылки
first_part_url = 'http://olympus.realpython.org'
for link in links:
    adress = first_part_url + link['href']
    text = link.text
    print(f'{text}: {adress}')

print(login_page)