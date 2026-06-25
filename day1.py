# first python code
print("hello arya")


# Syntax, Variables & Data Types
#variable
a = 10
print(a)
print(id(a))

b = 10
print(b)
print(id(b))


# Datatypes -> int, float, str, bool
# integer
a = 10
print(a)
print(type(a))

#float
b = 10.10
print(b)
print(type(b))

# string
c = "hello"
print(c)
print(type(c))

# boolean
d = False
print(d)
print(type(d))


#Type Conversion & Input/Output

# input function used to take input from user
# output function used for print the value of variable
num = input("enter the number:") #100
print(num)
print(type(num))
print(int(num) + 10) # both have type integer
print(num + str(10)) # both have type string
print(num * 10) # num num num num num num num num num num -> value of num variable


# example
num = int(input("enter the number2: "))
print(num)
print(type(num))

# example
name = str(input("enter the name: ")) # no need to add this str()
print(name)
print(type(name))


#Operators & Expressions

# arithematic opr ->
# + - * / // % **

# +
a = 10
b = 20
print(a + b) # 10 + 20

# -
c = 20
d = 10
print(c - d) # 20 - 10

# *
e = 10
f = 5
print(e * f) # 10 * 5

# /
num_1 = 20
num_2 = 2
print(num_1 /  num_2) # float

# //
num_3 = 20
num_4 = 2
print(num_3 // num_4) # float division -> integer

# %
num_5 = 10
num_6 = 3
print(num_5 % num_6)

# **
num_7 = 5
num_8 = 3
print(num_7 ** num_8)

# example (even or odd)
num9 = int(input("Enter the number: "))
num10 = 2
print(num9 % num10) # 0 -> it's even || 1 -> it's odd


# Relational opr -> True or False
# == , < , > , >= , <= , !=

# ==
num1 = 10
num2 = 11
print(num1 == num2)

# < -> less than
num1 = 10
num2 = 11
print(num1 < num2)

# > -> greater than
num1 = 20
num2 = 10
print(num1 > num2)

# >= -> greater than and equal to
num1 = 20
num2 = 10
print(num1 >= num2)

# <= -> less than and equal to
num1 = 20
num2 = 10
print(num1 <= num2)


# != -> not equal
num1 = 20
num2 = 10
print(num1 != num2)


# Assignment opr
# = , += , -= , *= , /= , //= , %=

# = -> assigning opr used to declare a variable

a = 10
b = a + 20
print(b)

# +=
a = 10
a += 20
print(a)

# -=

# *=

# /=

# %=

# //=



# Logical opr
# and , or , not

# and
a = 10
b = 20
print(a and b)


a = -10
b = 10
print(a and b)
print(a or b)

name1 = "hello"
name2 = ""
print(name1 and name2)
print(name1 or name2)