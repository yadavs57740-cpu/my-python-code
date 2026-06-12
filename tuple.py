#immutable -> not change
t=(10,20,30)
print(t[0])
print(t[-1])

#example
marks=[98,90,80,95]
marks[3]=50
print(type(marks))
print(marks)

#example
marks=[98,90,80,95]
#tuple
t=tuple(marks)
print(type(t))
print(t)

#tuple -> list
m=list(t)
print(type(m))
print(m)
