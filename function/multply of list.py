# Write a Python function to multiply all the numbers in a list.
def multiply(a):
    d=1
    for i in a:
        d*=i
    print(d)
    
n = int(input("Enter number of elements  "))
a = list(map(int,input("\nEnter the numbers ").strip().split()))[:n] 
multiply(a)
