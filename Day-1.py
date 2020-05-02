#Print statement

print("Hello, remove triple quotes from code which you need to run..")


#variable
'''
a=10
print("{} variable is {}:".format(a,type(a)))
a="sachin"
print("{} variable is {}:".format(a,type(a)))
a=11.1
print("{} variable is {}:".format(a,type(a)))
print(123456789)
'''


#Taking input from user
'''
a=input("Enter string:")
print("Input is a string type",a)
a=int(input("Enter integer:"))
print("Input is of Integer type",a)
a=float(input("Enter float value:"))
print("Input is of Float type",a)
'''

#list
'''

print("List components:",a)
a.append(1)
print("Appending in list :",a)
a.insert(3,11)
print("Inserting a number at position 3:",a)
a.remove(11)
print("Deleting a specific number from list:",a)
del a[5]
print("Deleting a element from a specific index:",a)
a.pop()
print("Removing last element from a list:",a)
b=a.count(1)
print("Counting a specific element in list: ",b)
b=a.index(5)
print("Finding index of a element from list:",b)
a[0]=99
print("changing the element on 0th index with 99:",a)
a.sort()
print("Printing a sorted list:",a)
a.sort(reverse=True)
print("printing descending sorted list:",a)
print("Max of list:",max(a))
print("Min of list:",min(a))
print("sum of list:",sum(a))
print("Average of list:",sum(a)/len(a))
'''

#slicing in list
'''
a=["Sachin",2,3,4,5,6,7,1,8]
print("Printing first 4 elements of list:",a[0:5])
print("accessing last element of list:",a[-1:])
print("accessing last 4 element of list:",a[-4:])

'''

#tuple
'''
tu=(1,2,4,5,7,8,9,6,4)
print("Printing tuple:",tu)
b=tu.count(4)
print("Counting number of occurr=ence of a element in tuple:",b)
b=tu.index(5)
print("Finding index of a element from tuple:",b)
'''

#Set
'''
s={1,2,1,3,4,5,6,7,8,9}
print("printing element of set:",s)
s.pop()
print("Removing last element of set:",s)
s.add(456)
print("Adding element in a set:",s)
d={8,9,11,22,33}
print("Printing interrsection of 2 sets:",s&d)
print("Printing Union of 2 sets:",s|d)
'''

#Dictionary
'''
d={"sachin":11,"Me":12,"Myself":2}
print("Printing dictionary:",d)
print("Printing keys of dictionary:",d.keys())
print("Printing values of dictionary:",d.values())
print("Printing items of dictionary:",d.items())
'''


#If-Else
'''
a=10
if a==5:
    print("{} is equal to 5.".format(a))
elif a>5:
    print("{} is Greater than 5:".format(a))
else:
    print("{} is less than 5.".format(a))
'''

#For
'''
a=[1,2,3,4,5,6,7,"EXIT",9,10]
for i in range(len(a)):
    if a[i]=="EXIT":
        break
    else:
        print("Element are:{}",a[i])
'''

#PATTERN
'''
#*
#**
#***
#****
for i in range(1,int(input("Enter limit:"))):
    print("*"*i)
'''

'''
#   *
#  * *
# * * *
#* * * *
for i in range(1,10):
    print(" "*(10-i),end="")
    for j in range(i):
        print("*",end=" ")
    print()
'''

#while
'''
i=1
while (i<=11):
    print("I value is :{}".format(i))
    i+=1

#Pattern(Through while loop)
i=1
while(i<11):
    print("*"*i)
    i+=1
'''

#For Else
'''
for i in range(1,11):
    if i==11:
        print("found")
        break
else:
    print("not found")
'''
#Ord and chr Function
'''
aa=65    
print(chr(aa))

sach="A"
print(ord(sach))
'''

#Function
'''
def sachin():
    print("You are in sachin's world!")
sachin()
'''
