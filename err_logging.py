# err_logging.py
import logging


def foo(s):
    return 100 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
    finally:
        print('finally...')


main()


class FooError(ValueError):
    pass


def foo1(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


foo1('0')

