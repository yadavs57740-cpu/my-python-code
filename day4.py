# Nested List

# Slicing
l = [10,20,30,["hello","hello1","hello2",[True,False]]]
l1 = l[-1:-3]
print(l1)
-3,-2,-1 # <-

#slicing
# l1 = l[:3]
# print(l1)

# #example
# print(l[2:])

#example


# Map (Transform values), Filter (Select values), Reduce (Combine values)

# function
# def square(x):
#     return x * x

#map (2 arguments)
# l = [10,20,30]
# l1 = list(map(square,l))
# print(l1)

#example
#map (2 arguments)
# l = [10,20,30]
# l1 = list(map(lambda x:x*x,l))
# print(l1)

# # alternative | without in built function
# l1 = []
# for i in range(len(l)):
#   l1.append(l[i] * l[i])
# print(l1)


#filter
def helo(x):
  return x.endswith('a')

l = ["apple","banana","cat","dog"] # map upper
l1 = list(filter(helo,l))
print(l1)

#example | alternative of filter
l1 = []
for i in l:
  if 'a' == i[-1]:
    l1.append(i)
print(l1)


#reduce

     
# Exception Handling

# try, except, finally

# try except
try:
  num1  = 10
  num2 = 5
  print(num1/num2)
except:
  print("hello except")

# try except
try:
  num1 = 10
  num2 = 0
  print(num1/num2)
except:
  print("hello except")

# try except and final
try:
  num1 = 10
  num2 = 5
  print(num1/num2)
except:
  print("hello except")
finally:
  print("hello finally divide")
