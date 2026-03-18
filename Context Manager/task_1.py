class Tabulation:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level = self.level + 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        assert self.level >= 0, 'Level cant be above zero!'
        self.level = self.level - 1

    def print(self, text):
        tabulation_literal = '\t' * self.level
        print(tabulation_literal + text)


print('NO TABULATION!')
# Только через with мы вызываем менеджер контекста
with Tabulation() as tabulation:
    tabulation.print('TABULATION!')
    with tabulation:
        tabulation.print('TABULATION X2!')
        with tabulation:
            tabulation.print('TABULATION X3')
    tabulation.print('TABULATION!')

no_tabulation = Tabulation()
# Никакой табуляции т.к. нет конcтрукции with
no_tabulation.print('NO TABULATION')
# Но вот тут табуляция будет
with no_tabulation:
    no_tabulation.print('TABULATION!!!')




from contextlib import contextmanager

level = 0
@contextmanager
def context_tabulation():
    global level
    level += 1
    yield
    level -= 1

def print_with_tabulation(text):
    return '\t' * level + text


with context_tabulation():
    print(print_with_tabulation('Tabulation?'))
    with context_tabulation():
        print(print_with_tabulation('Tabulation?'))
print(print_with_tabulation('Tabulation?'))



