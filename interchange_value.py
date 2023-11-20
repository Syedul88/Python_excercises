
def swap(a,b):
    temp = a # a = no value, temp = 10
    a = b # b = no value, a = 20
    b = temp # b = 10
    print("a: ",a)
    print("b: ",b)

swap(60,70)
swap(100,150)


# alternative of swapping

a = 30
b = 40
a,b = b,a
print("a: ",a)
print("b: ",b)