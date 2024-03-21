import mechanicalsoup

url = 'http://olympus.realpython.org/login'

browser = mechanicalsoup.Browser()
page = browser.get(url)
print(page.url)
html_page = page.soup
form = html_page.select('form')[0]
form.select('input')[0]['value'] = 'zeus'
form.select('input')[1]['value'] = 'ThunderDude'
inside_page = browser.submit(form, page.url)

print(inside_page.soup.title.string)

login = input('Enter login: ')
psw = input('Enter psw: ')
wrong_login_form = html_page.select('form')[0]
wrong_login_form.select('input')[0]['value'] = login
wrong_login_form.select('input')[1]['value'] = psw
wrong_enter_page = browser.submit(wrong_login_form,page.url)
wrong_enter_page_text = wrong_enter_page.soup.get_text()

print(wrong_enter_page_text.find('Wrong username or password!'))
if wrong_enter_page_text.find('Wrong username or password!') != -1:
    print('You entered wrong login or psw')
else:
    print('Welcome, ThunderDude!')

