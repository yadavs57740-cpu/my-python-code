#function
def hello():
    print("Hello function is working")
hello()


#example
def hello1(a): # a as a parameter
    print(a)
hello1(100)  # 100 as argument


#example
def add(a=2,b=3): #default value
    print(a+b)
add(10,5)
add()


#example
def power(a,b):
    print(a**b)
power(5,2)
power(2,5)
power(a=5,b=2)
power(a=2,b=5)


#example
def student(*a):
    print(a)
    print(type(a))
    print(a[0])
student(1,2,3,4,5,6)


def student(a,b):
    print(a,b)

#student(1,2,3,4,5,6)
student(10,20)


#question
def marks(a):  #parameter
    #for loop
    for i in a:
        print(i)
marks([10,20,30,40,50])


#question
def address(a):
    #loop
    for i in a:
     for j in i:         
      print(j)
address(["hello","nikita"])


#example
def sum(a,b):
   return a+b
result=sum(10,20)
print(result)

#Lambda functions [lambda arguments:expression]
add=lambda x:x
print(add(100))
sum=lambda x,y:x+y
print(sum(30,20))


a=lambda x:x
print(a([10,20,30,40]))


#question
show=lambda*a:print(a)
show(1,2,3,4,5)


#List comprehensions [expression for item in iterable]
print ([i for i in range(5)])

#example
l=[10,20,30,40,50,60]
print([l[i] for i in range(len(l))])

#question
l=[10,20,[30,40,50,60]]
print([l[2][i] for i in range(len(l[2]))])
print([l[-1][i] for i in range(len(l[-1]))])


#List
l=[10,20,30,40,50,"hello",True]
print(l)
print(l[0])
print(l[1])
print(l[-1])
print(l[-2])

#example
l=["hello","yourname","python"]
l.append("for arya mains")
print(l)
print(l[0])
print(l[-1])

#example of insert
l=[True,False,10,20]
l.insert(1,100)
print(l)

#question
l=[10,20,30,{"name":"nikita","address":["jaipur","kukas","Narnaul","Banaras"]}]
print(l)
print(l[3]["address"])
print(l[-1]["address"])
for i in l[3]["address"]:
    print(i)


#question
l=[10,20,30,[40,50,[60,70,80]]]
for i in range(2):
   print (l[3][i]) 

for i in l[3]:
   print (i)
print(l[3][0])
print(l[3][1])


#Dictionary
d={"name":"hello","age":20}
print(d.keys())
print(d.values())

for i in d.keys():
   print("key=",i)
   print("value",d[i])


#question
