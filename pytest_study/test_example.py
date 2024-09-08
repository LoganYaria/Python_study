def test_zero():
    1/0

def test_some_text_1(): # pytest считает тестом
    pass

def test_some_text_2(): # pytest считает тестом
    pass

def some_function(): # не является тестом
    pass

class TestClass: #pytest будет работать только если внутри класса будет функция с префиксом test
    def test_some_text_3(self):
        pass