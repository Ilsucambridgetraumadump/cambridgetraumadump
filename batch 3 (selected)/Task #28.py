#Task # 28: Input the marks obtained by a student in 2 test. Ouptut the grade. you dont need to do any validation 
#Distinction if both are above 80. 
#Drop is either is below 40 
#Merit if total of both is above 160  
#Credit if Total of both tests is above 120 
#Pass if above 100 
#Fail otherwise which means total is below OR EQUAL 100 
#82,83 => Distinction 
#98,39   => Drop 
#100,79 => Merit 
#70,75   => Credit 
#60,62   => Pass 
#42,43    => Fail


marks_1 = int(input("gimme marks of 1st test"))
marks_2 = int(input("inpur marks of 2nd test"))

if all(m > 80 for m in (marks_1, marks_2)): #same as marks_1 > 80 and marks_2 > 80
    print("distinction")
elif any(m < 40 for m in (marks_1, marks_2)): #same as marks_1 < 40 or marks_2 < 40
    print("drop")
elif (marks_1 + marks_2) > 160: #same as marks_1 + marks_2. sacalability version: elif sum((marks_1, marks_2)) > 160:
    print("merit")
elif (marks_1 + marks_2) > 120:
    print("credit")
elif (marks_1 + marks_2) > 100:
    print("pass")
else: 
    print("fail")


#https://chatgpt.com/g/g-p-68c24321c1b88191b8be370c45f8804e-as-a2-comp-sci/c/68f47c2c-3988-8322-acbc-210d121135e0
