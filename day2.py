# Logical operator
# and , or , not

# and
num1 = 10
num2 = 20
print(num1 and num2)

# or
num1 = "helo"
num2 = ""
print(num1 or num2)
print(num2 or num1)

# not
num1 = [] # default [] -> false || [1,2,3] -> true
print(not num1)

#not
num1 = {} # default {} -> false || {name:"hello"} -> true
print(not num1)


# Bitwise operator
# >> , << , & , | , ^

# &
a = 5 # 101
b = 2 # 010
print(a & b)


# identity operators
# is | is not

# example 1
# name = 10
# name1 = 10
# print(name == name1 )# value

# print(name is name1) # value | address
# print(id(name))
# print(id(name1))

#example   (-5 to 256) -> both variable point on same address
num1 = [1,2,3]
num2 = [1,2,3]
num3 = num1

print(num1 == num2)

print(num1 is num2)
print(id(num1))
print(id(num2))
print(id(num3))


# Conditional Statements
# if,elif,else

# if
num1 = 10
num2 = 20
if num1 < num2 :
  print(num2)

# if else
num1 = int(input("enter the number: "))
if num1 :
  print("number:-",num1)
else:
  print("zero",num1)

# if elif else
age = int(input("Enter the number: "))
if age == 18:
  print("your age is: ",age)
elif age > 18 :
  print("your are above then 18 <",age)
else:
  print("you are less than 18 >",age)


# Loops -> for,while,break,continue,pass

#for
# for i in range(5):
#   print("i = ",i)

# #for
# for i in range(1,11):
#   print("number = ",i)


# list
l = [11,12,13,14]
# print(len(l))
# for i in range(4):
#   print(l[i])

# for i in range(len(l)):
#   print(l[i])

# for i in l:
#   print(i)

#while
# num1 = int(input("Enter the number: "))
# i = 0
# while i < num1 :
#   print(i)
#   i += 1

# list
# l = [10,11,12,13,14,15]
# i = 0
# while i < len(l):
#   print(l[i])
#   i += 1

# example for | while
# d = {"name":"helo","age":20,"phone":"00000000"}
# l = d.keys()
# print(l)
# for i in range(len(d.keys())):
#   print(i)


# list example
l = [10,[11,12,13,14,15]]
# print(l[1])

# for i in l[1]:
#   print(i)

# print("second approch")

# for i in range(2,len(l[1])):
#    print(l[1][i])


# break
# for i in range(5):
#   if i == 2:
#     break
#   print(i)


# continue
# i = 0
# while True:
#   print(i)
#   if i == 5:
#     break
#   else:
#     i += 1
#     continue

# pass
i = 0
while True:
  print(i)
  if i == 4:
    pass
  if i == 5:
    break
  else:
    i += 1
    continue
  

# Sets & Set Operations
def numbers(*args):
    print(args[0])

numbers(1,2,3,4)
