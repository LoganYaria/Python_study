
#тесты до использования фикстур
def test_01():
    # setup
    some_list = []
    for i in range(4):
        some_list.append(i)
    assert (len(some_list) == 4)
    # tear down
    some_list = []


def test_02():
    # setup
    some_list = []
    for i in range(4):
        some_list.append(i)
    assert (some_list[3] == 3)
    # tear down
    some_list = []

#тесты с использованием фикстур
def test_01_1(full_list):
    # setup in fixture
    assert (len(full_list) == 4)
    # tear down after yield in fixture

def test_02_1(full_list):
    # setup in fixture
    assert (full_list[3] == 3)
    # tear down after yield in fixture