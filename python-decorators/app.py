import time


def verot_veiktspeju(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time() - t1
        print(func.__name__, t2)

    return wrapper


@verot_veiktspeju
def f1():
    time.sleep(0.01)


@verot_veiktspeju
def f2():
    time.sleep(0.01)


@verot_veiktspeju
def f3():
    time.sleep(1)


f1()
f2()
f3()
