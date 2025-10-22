#Task # 26: Generate a random number between 1 and 10 inclusive using the library random.  
#Ask the user to guess it, if the guess is exactly the number print "Bingo" 
#if it is one above or below print "Too Close", if it is 2 below or 2 above then 
#print "Close" otherwise print "You Loose". If the guess is wrong then print the  
#number computer generated(correct one). Test your program multiple times to check that each case is working fine.  

import random 

num = random.randint(1,10)
guess = int(input("GUESS THE NUMBAH "))

if guess == num:
    print("bingo")
elif guess == num - 1 or guess == num + 1:
    print("too close")
    print(num)
elif guess == num -2 or guess == num + 2:
    print("close")
    print(num)
else:
    print("YOU LOSE")
    print(num)