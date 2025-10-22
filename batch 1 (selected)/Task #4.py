#Task # 4 : Input the marks obtained by a students in three tests. Input the Maximum obtainable marks 
#also. You may assume that all test have the same Maximum obtainable Marks. Print the Total Marks, 
#Total Percentage and Average Marks of the Student. Your output must all be in one print statement 
#using concatenation of variables and string constants. 

Test1 = int(input("input marks of 1st test "))
Test2 = int(input("input marks of 2nd test "))
Test3 = int(input("input marks of 3rd test "))
MaxMarks = int(input("enter max possible parks "))

TotalMarks = Test1 + Test2 + Test3
TotalPercentage = (TotalMarks/(MaxMarks * 3)) * 100
AvgMarks = TotalMarks/3

print("total marks = " + str(TotalMarks) + " total percentage = " + str(TotalPercentage) + "%, average marks = " + str(AvgMarks))