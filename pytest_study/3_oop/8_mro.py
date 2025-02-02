class A:
    VAR = 'A'
    VAR2 = 'A2'

    def method(self):
        pass


class B:
    VAR = 'B'

    def method(self):
        print(self.VAR + self.VAR2)
        pass


class C(B, A):  # Кого первым упомянул в родителях, с того и начинается поиск вверх по иерархии

    pass


class D(C):
    pass


d = D()
d.method()
print(d.method)

print(D.__mro__) # Помогает разобраться в в лабиринтах неаследования
print(D.mro())