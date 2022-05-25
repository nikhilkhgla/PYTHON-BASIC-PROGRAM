# to print a addtion of two number with function
def add(a,b):
    print(a+b)
def subtract(a,b):
    print(a-b)
def multply(a,b):
    print(a*b)
def divied(a,b):
    print(a/b)

    
    
while(1):
    a=int(input(''' +-*/calculater/*-+
          press 1 for add
          press 2 for subtract
          press 3 for multply
          press 4 for divied
          press 5 for quit'''))
    if a==1:
        c=int(input("enter the value"))
        b=int(input("enter the value"))
        add(c,b)
    elif a==2:
        c=int(input("enter the value"))
        b=int(input("enter the value"))
        subtract(c,b)
    elif a==3:
        c=int(input("enter the value"))
        b=int(input("enter the value"))
        multply(c,b)
    elif a==4:
        c=int(input("enter the value"))
        b=int(input("enter the value"))
        divied(c,b)
    elif a==5:
        break
    else:
        print("invalud number")
        
