#Task #12:  Input the time in seconds and print in hours , minutes and second.  
#Test your program with 4000 seconds . Your output should be in the given format.  
#1 hr, 6 min, 40 seconds 


time_secs = int(input("gimme the time"))

time_hrs = time_secs//3600          #4000/3600 = quotient (hrs)
time_mins = (time_secs%3600)//60    #4000/3600 -> remainder/60 -> quotient (mins)
secs = (time_secs%3600)%60          #4000/3600 -> remainder/60 -> remainder (seconds) 
print(str(time_hrs) + "hr, " + str(time_mins) + " min " + str(secs) + " seconds")


# mod = remainder = %
# div = quotient = //