#ASSIGNMENT 1

'''Write a program that receives a file name and converts the contents of the file line by line to uppercase letters and prints them. 
If the input file does not exist, an error message is displayed and the program terminates.'''

fname = input("Enter file name: ")
#Open file on file explorer
try:
    fhand = open(fname)
#if file is not exist or miss spelling print this
except:
    print("File cannot be opened: ", fname)
#make the data in the file into uppercase letter
else:
    for line in fhand:
        print(line.upper().rstrip())
    fhand.close()

#ASSIGNMENT 2
'''Write a program that reads the mbox.txt file, finds email accounts on the line starting with From:, 
prints the host name, and prints the number of hosts printed.'''

number = 0
fhand = open("C:\\Users\\ASUS\\Desktop\\`\\COMPUTATIONAL THINKING & APPLICATION\\mbox.txt","r")
#Find special character
for line in fhand:
    if line.startswith("From:"):
        i = line.find("@")
        j = line.find(" ", i)
        print(line[i+1:j])
        number = number + 1
#print host
print(" ")
print("Total",number,"host printed")
fhand.close()  

#ASSIGNMENT 3

fname = input("Enter a file name: ") #mbox.txt
try:
    fhand = open(fname)
#if file is not exist or miss spelling print this
except:
    print("File cannot be opened: ", fname)

else:
    number = 0
    sum = 0
    for line in fhand:
        if line.startswith("X-DSPAM-Confidence: "):
            i = line.split()
            j = i[1]
            sum = sum + float(j)
            number = number + 1
#calculation of avarage    
    if number != 0:
        avarage = number/sum
    print("Average spam confidence", avarage)
    fhand.close()