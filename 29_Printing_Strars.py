#Raksith gowda
def function1():
    i = 0
    num = int(input("Enter number of rows:"))
    while True:
        if num > i:
            print(i * "* ")
            i = i + 1
        if num==i:
            break
def function2():
    num = int(input("Enter number of rows:"))
    while True:
        if num > 0:
            print(num * "* ")
            num = num - 1
        if num==0:
            break

a=int(input("Enter boolian code\n0=False\n1=True\n "))
boolian=bool(a)
if boolian == True :
    function1()
elif boolian == False:
    function2()

