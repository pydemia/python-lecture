```py

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
```
