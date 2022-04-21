class time:
    def __init__(self,h,m,s):
        self.hour= h 
        self.minute = m
        self.second = s
    def sub (self):
        pass
    def mul (self):
        pass
    def second2time (self):
       time = self.second * 60 / 3600
       print(time)
    def time2sec (self):
        time = self.hour * 3600
        print(time)

classrunner = time (4,2,60)
classrunner.sub()
classrunner.mul()
classrunner.second2time()
classrunner.time2second()