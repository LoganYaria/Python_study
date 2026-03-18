# Реализовать менеджер контекста, измеряющий исполенения блока кода при помощи функции time.time
from time import time, sleep

class TimeToManagement:

    def __enter__(self):
        self.time_start = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.counter = time() - self.time_start


with TimeToManagement() as t_t_m:
    sleep(2)
    for i in range(1,1000):
        i ** 100000
print(t_t_m.counter)


from contextlib import contextmanager


@contextmanager
def program_stopwatch():
    start_time = time()
    try:
        yield
    finally:
        time_count = time() - start_time
        print(time_count)

    time_count = time() - start_time
    return time_count

with program_stopwatch():
    print("Начало")
    #raise ValueError("Ошибка!")
    for i in range(1, 1000):  # Этот код не выполнится
        i ** 10000

