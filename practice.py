# Write a python program to read three numbers and if any two 
# variables are equal, print that number

a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))

if a==b or a==c:
    print(a)
elif b==c :
    print(b)
else:
    print("No two numbers are same ")