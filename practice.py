# Write a python program to read three numbers and if any two 
# variables are equal, print that number

# a=int(input("enter first number"))
# b=int(input("enter second number"))
# c=int(input("enter third number"))

# if a==b or a==c:
#     print(a)
# elif b==c :
#     print(b)
# else:
#     print("No two numbers are same ")


# -------------------------------------------------------------------------------------------



# 2. Write a python program to read two numbers and find the smallest among them using ternary operator

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

small = a if a < b else b
print("Smallest number:", small)

# -------------------------------------------------------------------------------------------

# 3. Write a python program to read three numbers and find the largest among them without ternary operator

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)