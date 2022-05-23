#Sorting the Lectures based on their start value
def sortLec(LecList):
    return sorted(LecList, key = lambda x: x['start'])

def minHallsRequired(LecList):
    #Sort the list of Lectures
    sortedLecList = sortLec(LecList)
    LecHalls = []
    for Lec in sortedLecList:
        Reserved = False 
        for Hall in LecHalls:
            #Check if the Lecture hall is free
            if Hall['end'] <= Lec['start']: # This Hall is free!
                #if the hall is free reserve it for the lecture 
                # and set the end of the hall as the Time the lecture ends
                Reserved = True
                Hall['end'] = Lec['end']
                break

        #if no Halls are available Reserve a new Hall
        if not Reserved:
            NewHall = {"end": Lec['end']}
            LecHalls.append(NewHall)
    return len(LecHalls)
    
#Driver Code
#input the start and end of each lecture
Lectures=[]
numberOfLec=int(input("number of lectures : "))
for i in range(numberOfLec):
    Lectures.append({"start":input(f"Start of lecture {i+1}: "),
                    "end": input(f"End of lecture {i+1}: ")})
print("List of Lectures and timing:",Lectures)
print("The min no. of Lecture halls required is:",minHallsRequired(Lectures)) 




