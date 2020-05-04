#constructor
class demo:
    def __init__(self):
        print("I am a costructor.\n")
        print("-"*80)

#Initializing variale with constructor
class demo1():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Value of a is {} Value of b is {} and their sum is :{}\n".format(a,b,a+b))
        print("-"*80)
        

#return
class demo2:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Value of a is {} \nValue of b is {}".format(a,b))
    def multy(self):
        c=self.a*self.b
        return c

#Assigning Default values
class demo3:
    def __init__(self,age=10,reg=101):
        self.age=age
        self.reg=reg
        print("Age is {} \nregistration number is {}\n".format(age,reg))
    def change(self):
        self.age+=10
        self.reg+=100
        print("changed age is {} \nchanged regestration number is {}\n".format(self.age,self.reg))
        print("-"*80)

#Single inheritance
class a():
    def __init__(self):
        print("from parent class")
    def demo_fun(self):
        print("Parent class method")
class b(a):
    def __init__(self):
        print("from child class")

#function overriding
class phone():
    def __init__(self):
        print("from parent class")
    def buy(self):
        print("buy method of Parent class")
        
class smartphone(phone):
    def __init__(self):
        print("from child class")    
    def buy(self):
        print("Buying smartphone")
        super().buy()  #using super keyword for invoking parent class method


#working of multiple inheritance 
class B1: 
    def __init__(self): 
        self.str1 = "Geek1"
        print("Base1") 
  
class B2: 
    def __init__(self): 
        self.str2 = "Geek2"        
        print("Base2") 
  
class Derived(B1, B2): 
    def __init__(self): 
          
        # Calling constructors of B1 and B2 classes 
        B1.__init__(self) 
        B2.__init__(self) 
        print("Derived") 
          
    def printStrs(self): 
        print(self.str1, self.str2) 
         
#multilevel inheritance
class Base(object): 
    def __init__(self, name): 
        self.name = name 
  
    def forName(self): 
        return self.name 
  
class Child(Base): 
    def __init__(self, name, age): 
        Base.__init__(self, name) 
        self.age = age 
    def getAge(self): 
        return self.age 
  

class GrandChild(Child): 
 
    def __init__(self, name, age, address): 
        Child.__init__(self, name, age) 
        self.address = address 
 
    def getAddress(self): 
        return self.address         

#static method
class one():
    def __init__(self):
        print("inside one class.")
    @staticmethod
    def mssg():
        print("static method")

        
if __name__=="__main__":
    #constructor
    demo()
    #adding
    demo1(6,5)
    #return keyword
    ob=demo2(9,5)
    print("Multiplication is :",ob.multy())
    print("-"*80)
    #assign deffault value in constructor to variables
    ob1=demo3()
    ob1.change()
    #for function override
    ob2=b()
    ob2.demo_fun()
    print("-"*80)
    #for single inheritance
    ob3=smartphone()
    ob3.buy()
    print("-"*80)
    #for multiple inheritance
    ob4= Derived() 
    ob4.printStrs()
    print("-"*80)
    #multilevel
    g = GrandChild("SACHIN", 19, "JAIPUR")   
    print(g.forName(), g.getAge(), g.getAddress())
    print("-"*80)
    #static
    one.mssg()
