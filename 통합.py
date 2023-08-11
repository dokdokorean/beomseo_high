import os
from multiprocessing import Process

def func1():
    os.system('1.py')

def func2():
    os.system('2.py')

def func3():
    os.system('3.py')

if __name__ == '__main__':
    p1 = Process(target=func1)
    p2 = Process(target=func2)
    p3 = Process(target=func3)
    p1.start()
    p2.start()
    p3.start()
