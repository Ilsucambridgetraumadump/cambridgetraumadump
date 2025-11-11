#Task # 45 : Input a string a print the following outputs one by one.  Use For loop for the first 2, Repeat 
#Loop for the next 2 and While Loop for the last 2 patterns.  
#Suppose if the input string is "house" 

#(iv) house 
#ouse 
#use 
#se 
#e 


word = "house"
i = 0

while True:
    brokenstring = word[i:]
    i = i + 1
    print(brokenstring)
    if i > len(word) - 1:
        break