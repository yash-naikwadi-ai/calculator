def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("invalid(not difined)")
    else:
        return a/b
        
a=float(input("Enter 1st no="))
b=float(input("Enter 2nd no="))
while True:
    choice=int(input("Which of the operation do u want(1,2,3,4):\n1. ADDITION\n2. DUBTRACTION\n3. MULTIPLICATION\n4. DIVISION(plz do not use zero)=\n"))
    if choice in range (1,5):
        if choice==1:
            print(a,"+",b,"=",add(a,b))
            break
        if choice==2:
            print(a,"-",b,"=",sub(a,b))
            break
        if choice==3:
            print(a,"x",b,"=",mul(a,b))
            break
        if choice==4:
            print(a,"/",b,"=",div(a,b))
            break
    else:
        print("strictly choose from 1 to 4 operation")
        continue
