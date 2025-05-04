# This is for checking exam eligibility
present = float(input("Enter the number of working days: "))
absent = float(input("Enter the nuber of days absent: "))
Eligibility = present / absent * 100
print("Your Exam eligibility is", Eligibility)
if Eligibility <= 75 - 64:
    print("You are not eligible.")
elif Eligibility <= 65.5 - 54:
    print("You are not eligible.")
elif Eligibility <= 55.5 - 1:    
    print("You are not eligible")
 
else:
    Eligibility >= 75-1000000 
    print("You are eligible.")

    
#This is also for checking eligibility

    number = int(input("Enter Number in percentage to check"))
print("Number to be checked :", number)

if number%2==0 :
    print("This is an even number")

else:
    print("This is an odd number")

if number>75:
    print("Number is greater than 75" \
    "You are eligible")
    if number%2==0:
        print("And it is even too")

 

else:
    print("Number is less than 75"   \
    "You are not eligible")

   

    #Calendar
    import datetime

# using now () to get current time
current_time = datetime.datetime.now()

#Printing value of now.
print("Time now at greenwich meridian is : ", end = "")
print(current_time)

# print calendar of year 2021
import calendar
print("\n", calendar.calendar(2025))
