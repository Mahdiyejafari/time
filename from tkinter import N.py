from tkinter import N


class fraction:
    def __init__(self,n,d,n2,d2):
        self.numerator = n
        self.denominator =d
        self.numerator2 =n2
        self.denominator2 =d2
    def add (self):
        h = (self.numerator*self.denominator2)+(self.denominator*self.numerator2)
        m=  self.denominator*self.denominator2
        c = h/ m
        print ("Add:",c)
    def sub (self):
        h= (self.numerator*self.denominator2)-(self.denominator*self.numerator2)
        m=  self.denominator*self.denominator2
        c = h/ m
        print ("Sub:",c)
    def mul (self):
        h= self.numerator*self.numerator2
        m=  self.denominator*self.denominator2
        c = h/ m

        print ("Mul:",c)
    def div (self):
        h= self.numerator*self.denominator2
        m=  self.denominator*self.numerator2
        c = h / m
        print ("Div:",c)
    def show (self):
        classrunner.add()
        classrunner.sub()
        classrunner.mul()
        classrunner.div()

classrunner = fraction (7,3,6,2)
classrunner.show()