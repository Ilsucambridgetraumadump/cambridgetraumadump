#Task # 7: Input the name, age and Salary of a person. Give the following output.  
#Mr. XXXX after five years you will be XX years old. Your salary is XXXXXX. I hope this is monthly. 
#Salary is a float variable so you must use the float function rather than int. 
#Name is String so you will not use int or float function. 


name = input("hello who u ")
age = int(input("how old is ya "))
salary = float(input("how much you earn (give it to me) "))



print("Mr. " + name + " after five years you will be " + str(age + 5) + " years old. Your salary is " + str(salary) + ". I do hope this is monthly, my _good_ sir")