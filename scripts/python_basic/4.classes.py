# -*- coding: utf-8 -*-


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


#%% 특수 메소드

class myobject(object):
    
    def __init__(self, obj, name):
        
        # Check if listobj is list type OR just you can change it to list
        if not isinstance(obj, list):
            obj = list(obj)
        
        self.data = obj
        self.name = name
        #self.InitData(data)
    
    def __new__(cls, *args, **kwargs):
        #return super(myobject, cls).__new__(cls)
        return super().__new__(cls)
    
    def __str__(self):
        return str(self.data)
    
    #def __call__(self):
    #    print(self.name)
    #    print(self.data)
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        self.data[index] = value
        #return self.data
    
    #def __delitem__(self):
    #    pass
    
    def __len__(self):
        return len(self.data)
    
    def __repr__(self):
        return str(self.data)

    
#새 인스턴스 생성 : __init__, __new__
tmpls = [1,2,3]
myobj = myobject(tmpls, 'Test')

# 속성값 확인
myobj.data
myobj.name

# Type(Class) 확인
type(myobj)


# 값 출력(print & str) : __str__, __repr__
print(myobj)
str(myobj)
myobj

# Indexing : __getitem__
myobj[1]

# Replacing : __setitem__
myobj[2] = 4

# Container 크기 확인 : __len__
len(myobj)
