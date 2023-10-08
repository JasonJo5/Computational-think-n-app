#Practice

def print_lyric():
    print("im a student")
    print("i sleep all night")

def repeat_lyric():
    print_lyric()
    print_lyric()

repeat_lyric()

def max_min(mylist):
    return [max(mylist), min(mylist)]

if __name__ == "__main__" :
    scorelist = [78, 56, 67, 95, 82]
    result = max_min(scorelist)
    print("result = ", result)
    best, worst = max_min(scorelist)
    print("best = ", best)
    print("worst = ", worst)

def report_score3(sclist):
    aver3=sum(sclist)/len(sclist) #sum = total sum and len is total int
    print("average:",aver3)

scorelist=[78,56,67,95,82]
report_score3(scorelist)

#another way

my_aver = lambda list : sum(list) / len(list)
scorelist = [78, 56, 67, 95, 82]
print("average: ", my_aver(scorelist))

scorelist = [78, 56, 67, 95, 82]
filter_result= filter(lambda x : x < 82,scorelist)
print(filter_result)
print(list(filter_result))


a = 'Endicott'
b = 'none'

def reg_GM (name):
    dept = 'Game'
    print ('Name :', name, ', Div&Dept :', a, b)
    
reg_GM("Hong Game")
print("Div =", a, "Dept =", b)

def swap(a, b):
    print("before swap", a, b)
    temp = a
    a = b
    b = temp
    print("after swap", a, b)
num1, num2 = 5, 33
swap(num1, num2)
print("outside function", num1, num2)

#//////////////////////////////////////////////////////////////////////////////

# ____    _     _   _    _
#  ||    /\    //   ||  //
#  ||   //\\   \\   || //
#  ||  //  \\   \\  || \\
#  || //    \\  //  ||  \\


#ASSIGNMENT 1
Hrs = 0
Rate = 0

def computepay(Hrs,Rate):
    pay = Hrs * Rate
    return pay

while True: #using while true, for a loop so i can put a break.

    try:
        Regular_Hrs = float(input("Enter Hours: "))
        Regular_Rate = float(input("Enter Rate: "))
    except:
        print("please enter numeric number")
        break

    regular_pay = computepay(Regular_Hrs,Regular_Rate) #40x10 = 400
    standar_pay = 40 * Regular_Rate
    over_pay = computepay(Regular_Hrs % 40, Regular_Rate * 1.5) # (5,10x1.5)
    Total_pay = standar_pay + over_pay # 400 + 75 = 475

    if Regular_Hrs <= 40:
        print("your Salary is:",regular_pay)
        break #put break so it wont loop again
    else:
        print("Your Salary is:",Total_pay)
        break #put break so it wont loop again
    

#ASSIGNMENT 2
score = 0
while True:
    try:
        def grades():
            score = int(input("Enter the test score = "))
            if 0 <= score <= 100:
                if score >= 90: 
                    print("Your Grade is: A")
                elif score >= 80: 
                    print("Your Grade is: B")
                elif score >= 70:
                    print("Your Grade is: C")
                elif score >= 60:
                    print("Your Grade is: D")
                else: 
                    print("Your Grade is: F") 

            else:
                print("Error, please enter numeric input between 0 and 100")
        (grades())
        break

    except:
        print("Error, please enter numeric input between 0 and 100")
        continue


#ASSIGNMENT 3

while True:
    N = input("please input positif integer number: ")
    if N == 'done':
        print ('all done')
        break

    try:
        N= int(N)
        def num_divide3(N):
            if N > 0:
                count = 0
                for i in range(1, N + 1): 

                    if (i % 3 == 0):
                        count += 1 
            return count
        print("numbers divisible by 3 among numbers from 1 to",N,":",num_divide3(N))
        
    except:
        print("please enter a positive number")
        continue