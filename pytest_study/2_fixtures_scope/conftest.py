import pytest

@pytest.fixture
def function_counter():
    counter = + 1
    print(f'Количество function использований: {counter}')
    return counter

@pytest.fixture(scope='class')
def class_counter():
    counter = + 1
    print(f'Количество class использований: {counter}')
    return counter

@pytest.fixture(scope='session')
def session_counter():
    counter = + 1
    print(f'Количество session использований: {counter}')
    return counter

@pytest.fixture(scope='module')
def module_counter():
    counter = + 1
    print(f'Количество module использований: {counter}')
    return counter