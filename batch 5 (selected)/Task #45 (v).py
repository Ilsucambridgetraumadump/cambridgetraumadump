#Task # 45 : Input a string a print the following outputs one by one.  Use For loop for the first 2, Repeat 
#Loop for the next 2 and While Loop for the last 2 patterns.  
#Suppose if the input string is "house"

#(v) 
#e 
#s 
#u 
#o 
#h 


word = "house"
i = len(word) - 1

while i > -1:
    brokenstring = word[i]
    i = i - 1
    print(brokenstring)