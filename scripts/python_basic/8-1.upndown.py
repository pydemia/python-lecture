# -*- coding: utf-8 -*-


from random import randint
secret = randint(1,100)

print ("숫자를 맞추어보세요! \n1부터 100까지의 숫자 중 하나입니다.")
guess = 0
while guess != secret:
    g = input("생각한 숫자를 적어주세요! : ")
    guess = int(g)
    if guess == secret :
        print(secret)
        print ("정답입니다!")
    else :
        if guess > secret :
            print ("너무 높아요!")
        else :
            print ("너무 낮아요!")
print ("게임이 끝났습니다.")
