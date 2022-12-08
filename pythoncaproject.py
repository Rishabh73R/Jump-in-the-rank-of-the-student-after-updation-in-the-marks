while True:
    try:
        N=int(input("Enter the number of students: "))
        break
    except ValueError:
        print("Please enter a number")

def rankcalculator(N):
    names=[]
    marks=[]
    updates=[]

for i in range(N):
    
    names.append(input("Enter the name of the student: "))
    
                 
    while True:
        try:
            marks.append(int(input("Enter the marks of the student: ")))
            break
        except ValueError:
            print("Please enter a number")
    while True:
        try:
            updates.append(int(input("Enter the update in marks of the student: ")))
            break
        
        except ValueError:
            print("Please enter a number")
    updatedmarks = []
    for i in range(N):
        updatedmarks.append(marks[i]+updates[i])
    maxmarks = max(updatedmarks)
    index = updatedmarks.index(maxmarks)
    maxname = names[index]
    previousrank = updatedmarks.index(maxmarks)+1
    currentrank = updatedmarks.index(maxmarks)+1
    jump = previousrank-currentrank
    print("The name of the student with maximum marks after updation in marks:",maxname)
    print("The jump in the student’s rank:",jump)

rankmarkcalculator(N)
    
