```py

username = "Jone"
messages = """Welcome to Python!
           Nice to meet you!
           """

print(username,
      messages)


import datetime as dt

class stopwatch:
    def __init__(self):
        self.start_time = dt.datetime.now()
        
    def stop(self):
        self.end_time = dt.datetime.now()
        elapsed = self.end_time - self.start_time
        print("Start  : ", self.start_time)
        print("End    : ", self.end_time)
        print("Elapsed: ", str(elapsed))
        return elapsed


type(3.0)

int(3.0)

float(2)
float("4")

str(20)



#논리(비교)
3 > 5

len("aa") == 3

```
