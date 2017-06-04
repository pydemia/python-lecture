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

