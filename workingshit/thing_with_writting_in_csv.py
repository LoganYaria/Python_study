from csv import writer

def writting_in_csv(text):
    list_data = ['1', '1', text,'','88005553535','3','12064','2023-07-22 00:00:00','10','test_desc','SelfCareDZ','test_param','text_not','']
    with open('export1.csv', 'a', newline='') as f_object:
        # Pass the CSV  file object to the writer() function
        writer_object = writer(f_object)
        # Result - a writer object
        # Pass the data in the list as an argument into the writerow() function
        writer_object.writerow(list_data)
        # Close the file object
        f_object.close()


string = 'AAAAAAAAAAA'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
i = 0
k = 0
j = 0
s_1 = 1
s_2 = 1
s_3 = 1
s_4 = 1
symbol = 1
while k < 1_000_000:
    while j != 26:
        string=(string[:i]+alphabet[j]+string[i+1:])#Добавление символа [0]
        writting_in_csv(string)
        k = k + 1
        #print(string)
        j=j+1
    if s_1%26!=0:
         string = (string[:i]+alphabet[0]+string[i+1:])#Сброс строки 0
         i=i+1
         symbol = 1
         string = string[:symbol] + alphabet[s_1] + string[symbol + 1:] #добавление символа [1]
         i=0
         j=0
         s_1= s_1 + 1
    elif s_2%26!=0:
        string = (string[:i] + alphabet[0] + string[i + 1:])  # Сброс строки 0
        string = (string[:i+1] + alphabet[0] + string[i + 2:])  # Сброс строки 1
        symbol = symbol+1
        string = string[:symbol] + alphabet[s_2] + string[symbol + 1:]  # добавление крайнего символа [2]
        s_2 = s_2 + 1
        s_1=1
        j = 0
    elif s_3%26!=0:
        string = (string[:i] + alphabet[0] + string[i + 1:])  # Сброс строки 0
        string = (string[:i+1] + alphabet[0] + string[i + 2:])  # Сброс строки 1
        string = (string[:i + 2] + alphabet[0] + string[i + 3:])  # Сброс строки 3
        symbol = symbol+2
        string = string[:symbol] + alphabet[s_3] + string[symbol + 1:]  # добавление крайнего символа [2]
        s_3 = s_3 + 1
        s_1 = 1
        s_2 = 1
        j = 0
    #new code
    elif s_4%26!=0:
        string = (string[:i] + alphabet[0] + string[i + 1:])  # Сброс строки 0
        string = (string[:i+1] + alphabet[0] + string[i + 2:])  # Сброс строки 1
        string = (string[:i + 2] + alphabet[0] + string[i + 3:])  # Сброс строки 3
        string = (string[:i + 3] + alphabet[0] + string[i + 4:])  # Сброс строки 4
        symbol = symbol+2
        string = string[:symbol] + alphabet[s_4] + string[symbol + 1:]  # добавление крайнего символа [2]
        s_4 = s_4 + 1
        s_1 = 1
        s_2 = 1
        s_3 = 1
        j = 0