import pytest
@pytest.fixture #объявление
def full_list():
    some_list = []
    for i in range(4):
        some_list.append(i)
    print('List is full')

    yield some_list

    for i in range(4):
        some_list.pop()
    if len(some_list) == 0:
        print('List is empty')



# есть параметр autouse
# Применение:
# @pytest.fixture
# def full_list(autouse=True):
#     pass
#  в таком случае фикстура будет юзаться по дэфолту в каждом тесте