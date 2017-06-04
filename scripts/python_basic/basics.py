# -*- coding: utf-8 -*-


#%% 코드 작성 요령

username = "Jone"
messages = """
Welcome to Python!
Nice to meet you!
"""

print(username, messages)


#%% Data Type

type(3.0)

int(3.0)

float(2)
float("4")

str(20)


#논리(비교)
3 > 5

len("aa") == 3


#%% Numbers

3 + 8
20 - 7
5 * 3
20 / 8
20 // 8
20 % 8
3 ** 5
divmod(20, 8)
pow(3, 5)

#%% String

'aa' + 'bb'
'aa' * 3

mystr = 'abcdefg'

mystr[0]
mystr[2]
mystr[-2]

mystr[2:]

#%% Boolean

a = 256 
b = 256
a is b # True
a == b # True 



a = 257 
b = 257
a is b # False
a == b # True 

x = 5
#--------------#
3 < x and x < 6
#--------------#
#True


x = 5
#---------#
3 < x < 6 
#---------#
#True

#%% Data Structure


mylist = ['q', 'u', 'e', 's', 't', 'i', 'o', 'n'] 

mytuple = 'q', 'u', 'e', 's', 't', 'i', 'o', 'n' 

mydict = {'coffee': 7, 'milk': 11, 'water': 20, 'wine': 'outofstock'} 

myset = {'e', 'l', 'e', 'm', 'e', 'n', 't', 's'} 


#%% 제어문 : if 문

#예제 코드 : 중첩

x = -1
#------------------#
if x < 0:
    if x == -2:
        print("x is -2")
    else:
        print("'x' is negative!")
elif x == 0:
    print("'x' is equal to Zero!")
else:
    print("'x' is positive!")
#------------------#
#“'x' is negative!" 


#%% 제어문 : while 문

x = 3
while x < 7:
    # str() for converting int to str
    print(str(x) + " is less than 7!")
    x += 1


x = 0
while x < 10:
    #if 'x' is even number
    x += 1
    if x % 2 == 0:
        print('Even number! :' , x)
        continue
    print(x)



x = [1, 3, 5, 8, 9]
ord = 0

while ord < len(x):
    num = x[ord]
    if num % 2 == 0:
        print('Even number! :' , num)
        break
    ord += 1

#%% 제어문 : for 문

for i in range(4):
    print(i) 

mylist = ['l', 'o', 'o', 'p'] 
for i in mylist:
    print(i) 




myl = ['l', 'i', 's', 't'] 
xyl = [1, 2]

for i in myl:
    for j in xyl:
        print(i + str(j)) 




import itertools as it 

myl = ['l', 'i', 's', 't'] 
xyl = [1, 2]

for i, j in it.product(myl, xyl):
    print(i + str(j))


#%%  함수 정의하기

def func_name(var1, var2):
    return var1 + var2

func_name(1, 2) 


def adder(a, b):
    print(a + b)

adder(1, 2) 


def adder(a, b):
    return a + b

res = adder(1, 2) 
res


#%% 변수

x = 2 # This 'x' is a global variable.
def funct():
    x = 10 # This 'x' is a local variable.


# 'x'의 값은?
funct()
x


x = 2 # This 'x' is a global variable.
def funct():
    global x
    x = 10 # This 'x' is a local variable.


# 'x'의 값은?
funct()
x


#%% 인자

def adder(string, num1, num2):
    print(string, ': ', num1 + num2)


adder('Result', 2, 3) # ‘Result : 5' 



def adder(srt=None, num1=1, num2=2):
    print(srt, ': ', num1 + num2)


adder(num1=4, srt='Result') # 'Result : 6' 
 
#%% Lambda 함수

# 일반 함수
def adder(num1, num2):
    return num1 + num2

adder(2, 3)


def twice(num1):
    return num1 * 2

twice(10)


# Lambda 함수
adder = lambda x, y: x + y
adder(2, 3)

twice = lambda x: x * 2
twice(10)


# 일급 객체로의 함수 : 일반 함수
numlist = [1, 2, 3, 4]
def editor(numbers, func):
    for i in numbers:
        print(func(i))

def plusone(num):
    return num + 1 

editor(numlist, plusone) 

# 일급 객체로의 함수 : Lambda 함수
numlist = [1, 2, 3, 4]
def editor(numbers, func):
    for i in numbers:
        print(func(i))

editor(numlist, lambda i: i+1) 


#%% 클래스 정의하기

obj = "python"
type(obj)

obj.capitalize()
"python".capitalize() 



class Membership:
    pass

someone = Membership()
someone




class Membership: 
    def __init__(self, name): 
        self.name = name 
    def introduce(self): 
        print(self.name + " is a member") 

# Instance bruce 
bruce = Membership('Bruce Lee')

bruce.introduce()
# Bruce Lee is a member




import datetime as dt

class stopwatch:
    def __init__(self):
        self.start_time = dt.datetime.now()
        
    def stop(self):
        self.__end_time = dt.datetime.now()
        print("Start  : ", self.start_time)
        print("End    : ", self.__end_time)

tmp = stopwatch()
tmp


#%% 상속

class elapsed_watch1(stopwatch):

    def elapse(self):
        self.end_time = dt.datetime.now()
        elapsed = self.end_time - self.start_time
        print("Elapsed: ", str(elapsed))
        return elapsed


class elapsed_watch2(stopwatch):

    def stop(self):
        self.end_time = dt.datetime.now()
        elapsed = self.end_time - self.start_time
        print("Start  : ", self.start_time)
        print("End    : ", self.end_time)
        print("Elapsed: ", str(elapsed))
        return elapsed


class elapsed_watch3(stopwatch):

    def __init__(self, name):
        super().__init__()
        self.name = name
        print("Name  : ", self.name)
        print("Start  : ", self.start_time)
 

    def elapse(self):
        self.end_time = dt.datetime.now()
        elapsed = self.end_time - self.start_time
        print("Elapsed: ", str(elapsed))
        return elapsed


    def stop(self):
        self.end_time = dt.datetime.now()
        elapsed = self.end_time - self.start_time
        print("Start  : ", self.start_time)
        print("End    : ", self.end_time)
        print("Elapsed: ", str(elapsed))
        return elapsed


watch = stopwatch()
watch.stop()
watch.start_time
watch.__end_time

watch1 = elapsed_watch1()
watch1.elapse()

watch2 = elapsed_watch2()
watch2.stop()

watch3 = elapsed_watch3("Python")
watch3.elapse()
watch3.stop()


#%% 모듈, 패키지

from src.mod import mymodule as md
from src.mod.mymodule import stopwatch as sw


tmp = md.stopwatch()
tmp = sw()


from src.op import int_operators, float_operators






