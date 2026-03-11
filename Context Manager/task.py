# print('\tTABULATION!')
# print('\t\tTABULATION X2!')
# print('\t\t\tTABULATION X3!')
# print('NO TABULATION!')

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
with Tabulation() as tabulation:
    tabulation.print('TABULATION!')
    with tabulation:
        tabulation.print('TABULATION X2!')
        with tabulation:
            tabulation.print('TABULATION X3')
    tabulation.print('TABULATION!')


