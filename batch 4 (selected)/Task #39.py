#Task # 44 : Input a number and print if it is a Prime number or not. A Prime number is the one that is 
#only divisible by 1 and itself. Your program should work with logically any positive number(no limit).  
#Check with 199 and 235. 


num = int(input("gimme a maybe-prime"))
i = 2
primeeee = True


if num < 0:
    print("positive nums only")

while i <= num**(1/2):  
    if num%i == 0:
        primeeee = False
    break
    i = i+1

print("primeeee?", primeeee)