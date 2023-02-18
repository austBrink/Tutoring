NUMBER_OF_STUDENTS = 24

print('Please Enter the number of drivers....')
numberOfDrivers = int(input());

studentsPerDriver = 4 

driverlessStudents = NUMBER_OF_STUDENTS % (numberOfDrivers * studentsPerDriver)

if(driverlessStudents == 0):
    print('All the students have a ride')
else:
    print('Some students do not have a ride')
