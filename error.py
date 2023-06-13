# try:
#     print('try...')
#     r = 10 / int('a')
#     print('result:', r)
# except ValueError as e:
#     print('Value error:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
#     print('No error')
# finally:
#     print('finally...')
# print('END')


def foo(s):
    return 100 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print("Error:", e)
    finally:
        print('finally...')


main()
