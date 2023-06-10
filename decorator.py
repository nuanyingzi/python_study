# 装饰器
def now():
    print("2023-06-10")


f = now
f()
print(now.__name__)
print(f.__name__)


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


now = log(now)
