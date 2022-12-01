a=1
while a<10:
    print(a)
    a+=1
# Python doesn't support increment or decrement operator
# While you dont know conditions until this statement becomes false.
# For when you know iterations to complete loop.

# iter will define whether a object is iterable or not.
b="Alishan"
print(b.__iter__)

for c in b:
    print(c)
    print(type(c))
# int is not iterable so use range.

for i in range(5):
    print(i)
    if i==3:
        break

# Indentation is Important!!!!
