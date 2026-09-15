
# Task_1: 

x = 1
if(x > 0):
    print(f"This is a string.")


# Task_2:

print(f"statement1")
print(f"statement2")
# the above two statements is written same as in one line.
print(f"statement1") ; print(f"statement2")


# TasK_3: Indentation
x = int(input("Enter a number: "))

# if(x > 0):
# print(f"This statement has no indentation.") # error

if(x > 0):
    print(f"This statement has tab intentation.")

if(x > 0):
 print(f"this statement has single space indentation.")


# Task_4: type checking

a = 10
b = 2.4
c = "This is a string."
d = True

print(f" a = {a}")
print("Type of a = ",type(a))
print(f" b = {b}")
print("Type of b =",type(b))
print(f" c = {c}")
print("Type of c =",type(c))
print(f" d = {d}")
print("Type of d =",type(d))

# Task_5 : escape sequence..

print("My name is Hassam ansar.\nMy roll no is 27.\tThis is back slasht")


# Task_6: strings:

str1 = "This is a 1st string."
str2 = 'This is a 2nd string.'
str3 = ''' This is a 3rd string.'''

print("str1 =",str1)
print("str2 =",str2)
print("str3 =",str3)
# slicing..

print(str1[1 : 5])

# Task_7: list

list = [1, 2, 3, 4, 5]

for i in range(1,len(list)+1):
   print(i)
