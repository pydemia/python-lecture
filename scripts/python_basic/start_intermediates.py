# -*- coding: utf-8 -*-


#%% Python 중급 맛보기

# Decorators

# Define a Decorator
def plusone(func):
    def function(*args):
        res = func(*args):
        print('res + 1:', res+1)
        return res+1
    return function

# Define another Decorator
def double(func):
    def function(*args):
        res = func(*args)
        print('res*2:', res*2)
        return res*2
    return function 

# Usage 1
@plusone
def adder(a, b):
    return a+b

adder(1, 2)

# Usage 2
@double
@plusone
def adder(a, b):
    return a+b

adder(1, 2)


from datetime import datetime as dt 
from functools import wraps


def time_profiler(func):

    @wraps(func) 
    def profiler(*args, **kwargs):

        start_tm = dt.now() 
        print("JobStart :", start_tm)

        res = func(*args, **kwargs)

        end_tm = dt.now()
        print("JobEnd :", end_tm)

        elapsed_tm = end_tm – start_tm
        print("Elapsed :", elapsed_tm)

        return res

    return profiler 


@time_profiler
def adder(a, b):
    return a+b

adder(1, 2)


#%% Iterator

# From list
mylist = [1, 2, 3] 
myiter = iter(mylist)

# From set
myset = set(mylist)
myiter = iter(mylist)

# From dict : dict_keys
mydict = {'a': 1, 'b': 2, 'c': 3}
myiter = iter(mydict)


# next() Method
mylist = [1, 2, 3]
myiter = iter(mylist)
next(myiter) # 1 
next(myiter) # 2 
next(myiter) # 3 
next(myiter) # StopIteration


# itertools Examples
import itertools as it


counter = it.count(start=3)
next(counter) # 3 
next(counter) # 4 
next(counter) # 5


mylist = [1, 2, 3]
number = it.cycle(mylist)
next(number) # 1 
next(number) # 2 
next(number) # 3 
next(number) # 1 
next(number) # 2 


#%% Comprehension

# List Comprehension
mylist = [2, 3, 4, 5, 6, 7]

mycomp = [i for i in mylist]
mycomp #[2, 3, 4, 5, 6, 7] 

mycomp = [i for i in range(2, 8) if i % 2 != 0]
mycomp #[3,5,7]

mylist = ['a', 'b', 'c']
xylist = [1, 2]
ids = [(word, num*2) for word in mylist for num in xylist] 


# Dictionary Comprehension
mylist = [1, 2, 3, 4, 5, 6, 7]
{item : item**2 for item in mylist if item < 4} 



#%% Generators

# List Comprehension
(expression for items in iterables)
(expression for items in iterables if condition)

import sys
print(sys.getsizeof( [i for i in range(100) if i % 2] )) # 528
print(sys.getsizeof( [i for i in range(1000) if i % 2] )) # 4272

print(sys.getsizeof( (i for i in range(100) if i % 2) )) # 88
print(sys.getsizeof( (i for i in range(1000) if i % 2) )) # 88 


# Lazy Evaluation

def operation_checker(x):
    print('Operating...')
    return x

# List
cont = [operation_checker(i) for i in range(10) if i % 2]
for _ in cont:
    print(_)

# Generator
cont = (operation_checker(i) for i in range(10) if i % 2)    
for _ in cont:
    print(_)


# count_recorder
def mygenerator():
    i = 0
    while True:
        yield i
        i += 1

mygen = mygenerator()


next(mygen)
next(mygen)
next(mygen)
next(mygen) 
next(mygen)


# Fibonacci Sequence
import itertools as it


def fibonacci():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev+curr

fibo = fibonacci()
list(it.islice(fibo, 0, 13))

next(fibo) 
next(fibo)
