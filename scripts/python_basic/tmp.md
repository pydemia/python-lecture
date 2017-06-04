```py

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
```
