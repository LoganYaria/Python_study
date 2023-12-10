def convert_cell_to_far(c):
    """Конвертируем цельсии в фаренгейты"""
    f=(c * 9) / 5 + 32
    return f

def convert_far_to_cell(f):
    """Конвертируем фаренгейты в цельсии"""
    c=((f - 32) * 5) / 9
    return c

tempc = input('Введите температуру по цельсию: ')
print(f'{tempc} градусов цельсия по фаренгейту будет: {round(convert_cell_to_far(float(tempc)),2)}')

tempf = input('Введите температуру по фаренгейту: ')
print(f'{tempf} градусов по фаренгейту будет {round(convert_far_to_cell(float(tempf)),2)} по цельсию')