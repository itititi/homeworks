import os
from datetime import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        path = 'main.log'
        log_message = f'{datetime.now()}: вызов функции {old_function.__name__} с аргументами {args} и {kwargs}\n'
        try:
            result = old_function(*args, **kwargs)
            log_message += f'{datetime.now()}: функция {old_function.__name__} вернула результат: {result}\n'
            return result
        except Exception as e:
            log_message += f'{datetime.now()}: при вызове функции {old_function.__name__} произошла ошибка: {str(e)}\n'
            raise
        finally:
            with open(path, 'a') as log_file:
                log_file.write(log_message)

    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()