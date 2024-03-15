import re
#.findall() исп для поиска любого регулярного выражения поддходящего условиям
result = re.findall('ab*c', 'abbbbbbcccccdabcabc') #ab*c * - 0 или вхождения одного или более симвлов перед *
print(result) #'abbbbbbc', 'abc', 'abc'
result = re.findall('ab*c', 'abbbbbbcccccd',re.IGNORECASE) # .IGNORECASE для игнорирования регистра
print(result) #abbbbbbc
result = re.findall('a.c', 'acccccdadc',re.IGNORECASE) # . - для вставки любого произвольного знака
print(result) #'acc', 'adc'
result = re.findall('a.*c','fffaaaahuihcopkokoacacac',re.IGNORECASE) # .* - вставка произвольго кол-ва символов
print(result) # aaaahuihcopkokoacacac

specific_result = re.search('ab*c','ABCABBBC',re.IGNORECASE) #исп для конкретного шаблона, вернет Match object
print(specific_result.group()) # ABC первый  результат с наибольшим охватом 11:51

string = 'Everything is <teg> not Enough <teg>'
string_1 = re.sub('<.*>', 'done', string) # заменит <***> на done от первого < до последнего >
print(string_1) # Everything is done
string_2 = re.sub('<.*?>', 'done', string) # заменит <***> на done от  < до  > минимальным путем
print(string_2) # Everything is done not Enough done