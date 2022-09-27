print("please enter a number for available drivers/parents/gaurdians")
parents = int(input())

students = 24 

studentsPerParent = 4 

#we want to know how many students will NOT have a ride. Well, how many WILL? 

studentsWithRide = parents * studentsPerParent

studentsWithNoRide = students - studentsWithRide

print("Total Students: 24")
print("Total Parents " + str(parents))
print("Total students withoutRide " + str(studentsWithNoRide))
print("Total students withRide " + str(studentsWithRide))