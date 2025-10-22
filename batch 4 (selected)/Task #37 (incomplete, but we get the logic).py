#Task # 37 : Write a program to input a number, (no fixed digits) , print the sum of its digits.  
#152 = 8 is the sum 
#92 = 11 is the sum
#9018 = 18 is the sum    

nom = input("INPUT UR NOM ")
ans = 0

for i in range(1, len(nom)):
    digit = int(nom)%10
    nom = int(nom)//10
    ans = ans + digit

print(ans)