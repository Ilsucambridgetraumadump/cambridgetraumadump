#Task #13: Input a 4-digit number and print the sum of its digits. You may assume that user will only enter 
#4 digit number and invalid data will not be entered.

num = int(input("ENTER YO NUMBER BRUH "))
sum_of_num = 0

for i in range(1,5):
    sum_of_num = sum_of_num + (num%10)
    num = num//10
    
print(sum_of_num)