#  Write a Python function to find the Max of three numbers

def maz(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>c and b>a:
        print(b)
    else:
        print(c)
        
a=int(input("enter  the numbar"))
b=int(input("enter  the numbar"))
c=int(input("enter  the numbar"))
maz(a,b,c)
    
