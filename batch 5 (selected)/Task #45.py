#Task # 45 : Input a string a print the following outputs one by one.  Use For loop for the first 2, Repeat 
#Loop for the next 2 and While Loop for the last 2 patterns.  
#Suppose if the input string is "house" 
 
#(i) 
#h 
#ho 
#hou 
#hous 
#house 


word = "house"
word2 = ""

for ch in word:
    brokenstring = ch
    word2 = word2 + brokenstring
    print(word2)