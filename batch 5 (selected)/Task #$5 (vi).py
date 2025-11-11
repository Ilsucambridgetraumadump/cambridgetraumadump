#Task # 45 : Input a string a print the following outputs one by one.  Use For loop for the first 2, Repeat 
#Loop for the next 2 and While Loop for the last 2 patterns.  
#Suppose if the input string is "house"

#(vi) 
#h 
#o
#u 
#s 
#e 

word = "house"
i = 0

while i < len(word):
    brokenstring = word[i]
    print(brokenstring)
    i = i + 1