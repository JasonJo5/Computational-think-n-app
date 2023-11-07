#Practice 1
print (int(3.141595))
print (float(365))
print (str(50))
print (float(99)+(100))
my_string = "hello" + "there"
print(type(my_string))
my_string = my_string + 1


#Practice 2
age = input("enter your age: ")
print(type(age))
age = int(input("enter your name: "))
print(type(age))


#Practice 3
width = 17
height = 12.0

width // 2
width /2.0
height / 3
1+2*5


#Practice 4
name = input("enter your name: ")
print ("hello " + name)

"""\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"""

# ____    _     _   _    _
#  ||    /\    //   ||  //
#  ||   //\\   \\   || //
#  ||  //  \\   \\  || \\
#  || //    \\  //  ||  \\


#Assignments 1
hours = float(input("how much hours do you works: "))
rate = float(input("how much rate do you get in hours: "))
salary = hours*rate
# output
print ("your salary is " + str(salary) + " Dollars")


#Assignments 2
celcius =  float(input("Enter Celcius Temparature: "))
fahrenheit = celcius*9/5+32 
#output
print ("Farenheit Tempature is: " + str(fahrenheit) + " Fahrenheit")


#Assignments 3
s = int(input("Enter Second: ")) # 1hour = 60mnt = 3600 sec
hours = s//3600   #3665 = 3665/3600 = 1
n =  s % 3600    #3665 = 3665%3600 = 65
minute = n // 60  #65/60 = 1
second = n % 60  #65%60 = 5
#output
print (str(hours) + " hours, " + str(minute) +  " minute , " + str(second) + " second ,")
