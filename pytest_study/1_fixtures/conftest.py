import pytest
@pytest.fixture #объявление
def full_list():
    some_list = []
    for i in range(4):
        some_list.append(i)
    print('List is full')

    yield some_list

    some_list = []
    print('List is empty')
