#take 2 input
def Normal_add(a,b):
    print(a+b)

#Take 2 input and multiple them
def multiply(a,b):
    print("multiplication is :",a*b)
    
#take multiple input and add them
def add(a,*b):
    a=a
    for i in b:
       a+=int(i)
    print("sum",a)

#Accessing another function within function
def child():
    print("In child function.")
def parent():
    print("in parent function.")
    child()
    print("Back to parent function")

#Printing table
def table(a):
    for i in range(1,11):
        print("{} X {} = {}".format(a,i,a*i))

#Passing liast a arument
def argumen(name):
    for i in range(len(name)):
        print("{} name is : {}".format(i+1,name[i]))

#Decorators
def sachin(func):
    def one():
        print("before execution::")
        func()
        print("after execution:")
    return one
#@sachin
def outs():
    print("outside world::::")
    
#Return
def ret(a,b):
    c=a+b
    return c


#MAIN FUNCTION    
if __name__=="__main__":
    #for add
    Normal_add(9,10)
    print("-"*50)
    #multiply
    multiply(9,4)
    print("-"*50)
    #multi input addition
    add(1,2,3,4,5,6,7,8,9,10)
    print("-"*50)
    #functiom
    parent()
    print("-"*50)
    #list as argument
    li=["Sachin","Rajnikant","Tamanna","Sanvi","Dhruv"]
    argumen(li)
    print("-"*50)
    #decorator
    outs=sachin(outs)
    outs()
