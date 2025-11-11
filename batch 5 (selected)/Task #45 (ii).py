#Task # 45 : Input a string a print the following outputs one by one.  Use For loop for the first 2, Repeat 
#Loop for the next 2 and While Loop for the last 2 patterns.  
#Suppose if the input string is "house" 

#(ii) 
#e 
#se 
#use 
#ouse 
#house

word = "house"

for i in range(1, len(word) + 1):
    print(word[-i:])