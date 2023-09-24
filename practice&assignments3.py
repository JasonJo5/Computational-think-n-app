#Practice 1
x = int(input("enter number ==> "))
if x > 100:
    if x < 1000:
        print("greater than 100 and less than 1000")
    else:
        if x == 1000:
            print("equal to 1000")
        else:
            print("greater than 1000")
else:
    if x == 100:
        print("equal to 100")
    else:
        print("less than 100") 


#Practice 2
score = int(input("Enter Your Score: "))

if score >= 90:
    print("A",end="")
else:
    if score >= 80:
     print("B",end="")
    else:
       if score >= 70:
        print("c",end="")
       else:
        if score >= 60:
         print("D",end="")
        else:
          print("F",end="")
print("Grade")


#Practice 3
score = int(input("Enter Your Score: "))

if score >= 90:
    grade ='A'
elif score >= 80:
    grade ='B'
elif score >= 70:
    grade ='C'
elif score >= 60:
    grade ='D'
else:
   grade ='F'
     
print("Grade is %s" % grade)

prompt = "Speed of Car?\n"
input_speed = input(prompt)
try:
    num_speed = int(input_speed)
    print("Speed of Car is %s" % num_speed)
except:
    print("Please enter a number")


#Practice 4
n = 3
while n > 0:
    print(n)
    n = n - 1
print("end of program")


#Practice 5
sum = 0
count = 1
n = int(input("Enter number greater than 1 : "))
while count <= n:
    sum = sum + count
    count = count + 1

print("sum 1 ~", n, ":", sum)


#Practice 6
sum = 0
count = 1
n = int(input("Enter number greater than 1 : "))
while count <= n:
    sum = sum + count
#    count = count + 1

print("sum 1 ~", n, ":", sum)


#Practice 7
limit = 9
number = int(input("Display a multiplication table of number? "))

for i in range(1, limit):
    result = number * i
    print(number, 'x', i, '=', result)


"""\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"""

# ____    _     _   _    _
#  ||    /\    //   ||  //
#  ||   //\\   \\   || //
#  ||  //  \\   \\  || \\
#  || //    \\  //  ||  \\


#ASSIGNMENT 1
while True:

    hours = 0
    rate = 0

    try:
     hours = int(input("Enter Hours: "))
    except:
     print("Error, please enter numeric input")
     break

    try:
     rate = float(input("Enter Rate: "))
    except:
     print("Error, please enter numeric input")
     break


    if hours <= 40:
     salary = hours*rate
     print ("your Salary is: " + str(salary))
    else:
     if hours >= 40:                                 #45
      salary = (40*rate) + ((hours%40)*rate*1.5)     #45%40 = 5x10.1,5
      print ("your Salary is: " + str(salary))


# ASSIGNMENT 2

score = 0

try:
    score = int(input("Enter Your Score: "))


    if 0 <= score <= 100:
     if score >= 90:
       print("A",end="")
     else:
      if score >= 80:
       print("B",end="")
      else:
        if score >= 70:
            print("C",end="")
        else:
           if score >= 60:
            print("D",end="")
           else:
            if score >= 0:
                print("F",end="")
    
    else:
     print("please enter numeric input between 0 and 100")

    print(" Grade")

except:
  print("please enter numeric input between 0 and 100")

#ASSIGNMENT 3

total_input = 0
total = 0
average = 0

while True:
    
    number = input("Enter a number: ")
    if number == 'done':
        break

    try :
        num1 = float(number)

        total_input = total_input +1
        total = total + num1
        average = total/total_input

    except:
        print('Invaled Input')
        continue
    

    print ('all done')
    print ("Total: ",total," ,Total Input: ",total_input," ,Average: ",average)