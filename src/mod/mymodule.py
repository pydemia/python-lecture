# -*- coding: utf-8 -*-


import datetime as dt

class stopwatch:
    def __init__(self):
        self.start_time = dt.datetime.now()
        
    def stop(self):
        self.__end_time = dt.datetime.now()
        print("Start  : ", self.start_time)
        print("End    : ", self.__end_time)



class elapsed_watch(stopwatch):

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
        elapsed = self.end_time - \  
                  self.start_time
        print("Start  : ", self.start_time)
        print("End    : ", self.end_time)
        print("Elapsed: ", str(elapsed))
        return elapsed
