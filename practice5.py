fruit = "banana"
letter = fruit[1]
print(letter)

x = 3
w = fruit[x-1]
print(w)


str1 = "forever"
print(str1[3]) #e
print(str1[0]+str1[6])

str2 = "young"
print(str1+str2)
print(str1*2)

fruit = "banana"
index = 0

while index < len(fruit):
    letter = fruit[index]
    print(index,letter)
    index = index + 1

for letter in "banana":
    print(letter)

word = "banana"
count = 0
for letter in word:
    if letter == "a":
        count = count + 1
print(count)

str1 = "Monty Python"   #start : stop : step    # 0 1 2 3 4 5 6 7 8 9 10 11
print(str1 [0:12])                              # M o n t y   P y t h  o  n
print(str1[0:12:2])     #skip every 2 step

str1 = "Monty Python" #change the y into i
new_str1 = str1[:7]+ "i"+ str1[8:] #start : stop : step
print(new_str1)

str1 = "monty phyton"
str2 = "monty python"
int1 = 8
int2 = 9

print(str1==str2)
print(int1>int2)


word = "forever young"
print(len(word)) # 15   length of string
print(max(word)) # y     largest character in string 
print(min(word)) #        smallest character in string 
print(list(word)) # ['F', 'o', 'r', 'e', 'v', 'e', 'r', ' ', 'y', 'o', 'u', 'n', 'g', '!', ' ']      convert string to list
print(tuple(word)) # ('F', 'o', 'r', 'e', 'v', 'e', 'r', ' ', 'y', 'o', 'u', 'n', 'g', '!', ' ')      convert string to tuple
print(sum(str1)) # error
print(word.upper())
print(word.lower())
print(word.isupper())
print(word.islower())

str1 = "Monty Python"
str2 = "monty Pyhton"

print(str1 > str2)
print(str1 < str2)

word = "banana"
print(word.isalpha())
print(word.isdigit())

print("banana".isalpha())       #True  (banana is alphabet)
print("good morning".isalpha()) #False (space is not alphabet)
print("1000".isdigit())         #True  (1000 is number)
print("100.5".isdigit())        #False (.is not number)

word = "Banana"
print(word.find("a"))       #1
print(word.find("na"))      #2
print(word.find("na",3))    #4
print(word.find("ba"))      #-1 if substring is not found its showing -1
print(word.find("Na"))      #-1 if substring is not found its showing -1
word1 = (word.upper())
print(word1)

greeting = "Have a nice day"
print(greeting.startswith("Ha"))            #True
print(greeting.startswith("h"))             #False
print(greeting.lower().startswith("h"))     #true
print(greeting.replace("nice","good"))      #False

print(greeting.split())

str1 = "a:b:c:d"
print(str1.split(":"))
delimeter = ":"
print(str1.split(delimeter))

str1 = "From brian.adams@uct.ac.za Sat  Jan 6 09:14:16 2008"
print(str1[17:26])

data = "From @jasonjoevanka Sat  Jan 6 09:14:16 2008"
atpos = data.find("@")      
print(atpos)      
sppos = data.find(" ", atpos)      
print(sppos)      
host = data[atpos+1:sppos]      
print(host)


camels = 42

print("I have %d Camels" % camels)

print("in %d years and %d days I have spotted %g %s" %(3,12,0.1,"camels"))

print("I eat {} and a {number} of {name1}".format("burger", number = 100, name1 = "chicken"))

name = "Jason"
age = 18

print(f"My name is {name} and im {age} years old")
print(f"next year I am {age+1} next year old")

str1 ="he is "
str2 = 20
str3 =" years old"

print(f"{str1}{str2}{str3}")

text1 = "hello world!!!"
print(text1.split())
text2 = "dog;cat,monkey;bird,fish"
print(text2.split(";"))

String = (input("please enter string:"))
String_upper = String.find("P")
String_lower = String.find("ython")

String_upper1 = (String_upper.upper())
String_lower1 = (String_lower.lower())

print(String_upper,String_lower)

#//////////////////////////////////////////////////////////////////////////////

# ____    _     _   _    _
#  ||    /\    //   ||  //
#  ||   //\\   \\   || //
#  ||  //  \\   \\  || \\
#  || //    \\  //  ||  \\

#Assignment 1
while True:
    str1 = input("please enter 2 word: ") #pine apple
    
    if " " in str1:                       #pine" "apple
        letter = str1.find(" ")
        letter1 = str1[0:letter]
        letter2 = str1[letter:len(str1)] # from " " until di rest of the str1 (len)
       
        if letter1 < letter2:
          print(letter1,"Comes First")
        else:
          print(letter2,"Comes First")

    if str1 == 'done':
        print ('-- bye !!')
        break
    continue


#Assignment 2
words = input("Enter string: ")
print("Input string is :", words)

index = 0
while index < (len(words)):   #0-len words
   index = index + 1      
   print(words[-index])       #from behind


#Assignment 3
string = input("please enter string:")
uppercase = 0
lowercase = 0
number = 0
other = 0

for letter in string:
    if letter.isupper():            #Uppercase letter
        uppercase = uppercase + 1
    elif letter.islower():          #Lowercase letter
        lowercase = lowercase + 1
    elif letter.isdigit():          #Digit (number)
        number = number + 1
    else:
        other = other + 1           #other character means (space, :, !)

print("- Uppercase letter:", uppercase)
print("- Lowercase letter:", lowercase)
print("- Number:", number)
print("- Other character:", other)


#Assignment 4
new_string = ""
string = input("Pleas enter string:")

while True:
    for letter in string:
        string1 = (string.upper())
        if (letter != ",") and (letter != ".") and (letter != ":") and (letter != "!") and (letter != "?"):
            new_string = new_string + letter.upper()

    if string == "done":
        print("Bye !")
        break

    print(new_string)
    break