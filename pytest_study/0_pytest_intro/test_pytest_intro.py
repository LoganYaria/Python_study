def test_one():
    print('>>>Test one.')
    assert 2 + 2 == 4 # проверь, что справа истина, В асерте код выполняется справа на лево
    assert 2 + 1 == 4 , 'ты еблан?'

def test_two():
    assert 'Here' == 'Where?','Строки не равны' # после "," вывод строки AssertionError: Строки не равны

def test_three():
    string_0='string'
    assert isinstance(string_0,str) # проверяет, является ли объект (первый аргумент) экземпляром или подклассом класса
    # classinfo (второй аргумент).


class TestClass:
    def test_one(self):
        list_to_test_1 = []
        list_to_test_2 = []
        assert list_to_test_1 is list_to_test_2

    def testtwo(self):
        assert 1 is 1