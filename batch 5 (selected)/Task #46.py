#Task # 46 : Input a string and a character. Do not use find() method in this question. 
#(i) Find if the input character exist in the string. 
#(ii) Find the number of times the input character exists in the String.

word = input("gimme wurd ")
char = input("gimme char ")
i = 0
is_exist = 0 

for i in range(len(word)):
    ch = word[i]
    if ch == char:
        is_exist += 1
    
print(is_exist)