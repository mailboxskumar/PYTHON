# In python no need decalre type of variable
# based of the value, it will assign the type

a = 1
b = 10.2
c = "test"
d = 'e'
flag = False
flag = True

# type function will provide type of the variable
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(flag))
print("===========================")

# declaring variables in single line
a, b, c, d = 10, 10.4, "test", True
print(a, b, c, d)
print("===========================")

# assigning same value to multiple variables
a = b = c = 10
print(a, b, c)
print("===========================")

# swapping data
a, b = 10, 20
a, b = b, a
print(a, b)
print("===========================")

# concatenation
print(10 + 20)
print(10.4 + 20.5)
print(10 + 10.5)
print(10 + True)
print(10.5 + True)
print(True + True)
print(False + False)
print("str" + "-str1")
print("===========================")

# Re-declare a Variable: You can re-declare the variable even after you have declared it once
a = 10
print(a)
a = 100
print(a)
print("===========================")

# Deleting a variable
a = 10
print(a)
# del a #Uncomment code to see the error
print(a)
print("===========================")

# Printing data in different ways.
eid, ename, esal = 111, "ratan", 10000.45
print(eid)
print(ename)
print(esal)
print("Emp id=", eid)
print("Emp Name=", ename)
print("Emp Sal=", esal)
print(eid, ename, esal)
print("Emp id=", eid, "Emp name=", ename, "Emp sal=", esal)
