from abc import ABCMeta,abstractmethod
#abstract class
class product(metaclass=ABCMeta):
    @abstractmethod
    def mssg(self):
        print("sachin")

class phone(product):
    def mssg(self):
        print("HELLO")

#exception handling
def excep():
    a=[0,1,2,4,5,6,7,8,9]
    for i in range(len(a)):
        try:
            b=9/a[i]
            print("after dividing:{:.3f}".format(b))
        except:
            print("an unwanted error occur.")
#try except finally
def tef():
    try:
        n=int(input("Enter an integer input:"))
        print("The input was:",n)
    except:
        print("An error occured due to invalid input.")
    finally:
        print("it will execute if an error occur or not.")

#fileopen
def fi_op():
    i=input("enter file name:")
    f=open(i,"w")
    f.write("hey buddy how are you.")
    f.close()

def fi_re():
    i=input("Enter file to read:")
    f=open(i,"r")
    print(f.read())
    f.close()

def fi_ap():
    i=input("Enteer file to append anything:")
    f=open(i,"a")
    f.write("\nThis is appended line")
    f.close

def fi_cr():
    i=input("Enteer new file name:")
    f=open(i,"x")
    f.write("nayi file bnegi")
    f.close()


if __name__=="__main__":
    p=phone()
    print("-"*50)
    excep()
    print("-"*50)
    #tef()
    print("-"*50)
    fi_op()
