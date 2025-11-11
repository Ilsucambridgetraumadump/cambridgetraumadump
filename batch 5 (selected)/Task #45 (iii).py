#Task # 45 : Input a string a print the following outputs one by one.  Use For loop for the first 2, Repeat 
#Loop for the next 2 and While Loop for the last 2 patterns.  
#Suppose if the input string is "house"

#(iii) 
#house 
#hous 
#hou  
#ho 
#h 


word = "house"
i = len(word)  

while True:
    brokenstring = word[0:i]
    print(brokenstring)
    i = i - 1
    if i < 0:
        break