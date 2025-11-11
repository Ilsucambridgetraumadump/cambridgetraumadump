#Task # 49 : Input a String and a character, remove all occurrance of the character from this String. for 
#example  
#"Co**mp*u******t*er" 
#"*" 
#"Computer" 

word = input("gimme wourd ")
ch = input("gimme character ")

for i in range(len(word)):
    char = word[i]
    newstirn = word[:i]
    if ch == char:
        newstirn = word[:i - 1]
    
    
print(i, newstirn)
