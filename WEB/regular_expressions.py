import re
#.findall() исп для поиска любого регулярного выражения поддходящего условиям
result = re.findall('ab*c', 'abbbbbbcccccd') #ab*c * - 0 или вхождения одного или более симвлов перед *
print(result)#abbbbbbc
result = re.findall('ab*c', 'abbbbbbcccccd',re.IGNORECASE) # .IGNORECASE для игнорирования регистра
print(result)#abbbbbbc
result = re.findall('a.c', 'acccccd',re.IGNORECASE) # . - для вставки любого произвольного знака
print(result)#acc