#ASSIGNMENT 1
def chop(string1):
    if len(string1) >= 2:
        del string1[0]
        del string1[-1]
    else:
        print()
        pass
def middle(string2):
    if len(string2) >= 2:
        string2 = string2[1:-1]
        return string2
    else:
        return []
    
List = [1, 2, 3, 4]
print("My list before call chop function =>", List)
chop(List)
print("My list after call chop function  =>", List)

List1 = [1, 2, 3, 4]
print("My first list before call middle function =>", List1)
List2 = middle(List1)
print("My list after call middle function =>", List1)
print("New list after call middle function =>", List2)
    
#ASSIGNMENT 2
fhand = open("C:\\Users\\ASUS\\Desktop\\`\\COMPUTATIONAL THINKING & APPLICATION\\romeo.txt","r")
List = []
for line in fhand:
    line = line.split()
    for wrd in line:
        if wrd not in List:
            List.append(wrd)
List = sorted(List)
print (List)
fhand.close()

#ASSIGNMENT 3
fhand = open("C:\\Users\\ASUS\\Desktop\\`\\COMPUTATIONAL THINKING & APPLICATION\\mbox.txt","r")
count = 0

for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    print(words[1])
    count = count + 1
print("Total %d lines were printed" % count)

#ASSIGNMENT 4
list = []

while True:
    inp = input("Please enter an integer: ")
    if inp == "done":
        print("---------- Bye !! --------------")
        break
    try:
        inp = int(inp)
        list.append(inp)
        if len(list) > 0:
            average = sum(list) / len(list)
            print(list,", average=", average)
    except ValueError:
        print("Invalid input, enter a correct integer or 'done'.")