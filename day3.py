# Functions and Modules

# function
# def hello():
#   print("hello function is working")

# hello()


#example
# def hello1(a): # a as a parameter
#   print(a)
# hello1(100) # 100 as a argument


#example
# def add(a=2,b=3): # default value
#   print(a+b)
# add(10,5)
# add()

#example
# def power(a,b):
#   print(a**b)

# power(5,2)
# power(2,5)
# power(b=5,a=2) # 32
# power(a=2,b=5) # 32

#example
# def student(*a):
#   print(a)
#   print(type(a))
#   print(a[0])

# student(1,2,3,4,5,6)

# def student(a,b):
#   print(a,b)

# student(10,20)


# question
# def marks(a): # parameter
#   #for loop ,
#   for i in a:
#     print(i)

# marks([10,20,30,40,50])


#question
# def address(a):
#   #loop
#   print(a)
#   for i in a:
#     for j in i:
#       print(j)

# address(["hello","yourname"])




#example
# def sum(a,b):
#   return a+b

# result = sum(10,20)
# print(result)


#Lambda Functions [lambda arguments : expression]
# add = lambda x: x
# print(add(2000))

sum = lambda x,y: x+y
print(sum(10,20))

# a = lambda x:x[0]
# print(a([10,20,30,40]))

#question
a = lambda *x: [i for i in x]
print(a(10,20,30))


#List Comprehensions [expression for item in iterable]
# print([i for i in range(5)])

# #example
# l = [10,20,30,40,50,60]
# print([l[i] for i in range(len(l))])

#question
l = [10,20,[30,40,50,60]]
print([l[2][i] for i in range(len(l[2]))])
print([l[-1][i] for i in range(len(l[-1]))])
     

# Indexing and Slicing

#list
# l = [10,20,30,40,50,"hello",True]
# print(l)
# print(l[0])
# print(l[-1])
# print(l[-2])

# # example of append
# l = ["hello","yourname","python"]
# l.append("for arya mains")
# print(l)
# print(l[0])
# print(l[-1])

# # example of insert
# l = [True,False,10,20]
# l.insert(1,100)
# print(l)


#question
# l = [10,20,30,{"name":"yourname","address":["jaipur","kukas","home town","friend house"]}]
# print(l[3]['address'])
# print(l[-1]['address'])
# for i in l[3]['address']:
#   print(i)

# question
l = [10,20,30,[40,50,[60,70,80]]]
for i in range(len(l[3])-1):
  print(l[3][i])


for i in l[3]:
  print(i)
     

# dict
d = {"name":"hello","age":20}

print(d.keys())
print(d.values())

for i in d.keys():
  print("key=",i)
  print("value=",d[i])


# question
d = {
  "Message": "Number of Post office(s) found: 6",
  "Status": "Success",
  "PostOffice": [
    {
      "Name": "Achrol",
      "Description": "",
      "BranchType": "Sub Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
     {
      "Name": "Jaitpura Khinchi",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
    {
      "Name": "Kali Pahadi",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
    {
      "Name": "Kant",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
    {
      "Name": "Labana",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
    {
      "Name": "Rajpurawas Tala",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    }
  ]
}
     