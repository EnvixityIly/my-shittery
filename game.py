Attendance = int(input("Enter the total number of people in your class: "))
sq = []
p = 0
a = 0
for x in range(0,Attendance):
    x = x+1
    name = input("Enter the name of the student: ")
    pa = input("Is the student absent or present : ")
    if pa == "Absent":
        a = a+1
        gp = "Absent"
    else:
        p = p + 1
        gp = "Absent"
    lp = gp + " ;"
    sq.append(name)
    sq.append(lp)
    
print(sq)
print("Total present = ", p)
print("Total absent = ", a)



    
