#Task # 24: Input a number and print if it is special or ordinary 
#Special numbers are the ones that are in the following ranges inclusive 
#20 - 30 
#50 - 60  
#80 - 90  
#All numbers input must be in the range 0 - to 100 and if not an error must be displayed. 

num = int(input("ENTER YOUR NUMBAH "))
if (20 <= num <= 30) or (50 <= num <= 60) or (80 <= num <= 90):
    print("YOU ARE MY SPECIALLL")
else:
    print("dont worry, child, sukuna shall not haunt you (probably)")