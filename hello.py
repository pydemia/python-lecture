# -*- coding: utf-8 -*-


import sys
import datetime as dt

argument = sys.argv
username = input("이름을 입력하세요 :")
greeting = "Hi, {}!".format(username)
messages = "Welcome to Python!"

print()
print("Argument(s) : ", argument[1:])
print(str(dt.datetime.now()))
print(greeting, messages)

