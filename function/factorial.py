# Write a Python function to print factorial with function.
def fac(a):
    d=1
    for i in range (a):
        d*=i+1
        
    print(d)
    
a=int(input("enter the number"))
fac(a)
