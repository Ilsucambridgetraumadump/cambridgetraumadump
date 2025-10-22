#Task 36 : Write a program to input two numbers, B and P. Find B raised to the power of P. For example if 
#B = 3, and P = 4 your output should be 81. You cannot use the power (**) operator in python and (^) 
#operator in pseudocode.  


B = int(input("input first nom"))
P = int(input("enter 2nd nom"))
ans = B

for i in range(1, P):
    ans = ans * B 

print(ans)