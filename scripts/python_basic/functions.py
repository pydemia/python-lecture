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

