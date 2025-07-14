a = False
b = False
c = a or b
print(a, "OR ", b ,"= ",c)
a = True
b = False
c = a or b
print(a, " OR ", b ,"= ",c)
a = False
b = True
c = a or b
print(a, "OR ", b ," = ",c)
a = True
b = True
c = a or b
print(a, " OR ", b ," = ",c)
print("---OR---")


a = True
b = not a
print(a, "NOT ", b)
print('---NOT---')

