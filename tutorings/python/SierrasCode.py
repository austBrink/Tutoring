
def main():
    integer_list = getData()
    # need to display the list of numbers 
    display(integer_list)
    average_of_list = average(integer_list)
    print('The average of all the numbers in the list are ', average_of_list)
    minimum_of_list = minimum(integer_list)
    print('The lowest number of this list is ', minimum_of_list)
    maximum_of_list = maximum(integer_list)
    print('The highest number from this list is ', maximum_of_list)

def display(user_list):
    listInString = "The list is: "
    for i in range (0,len(user_list)):
        listInString = listInString + str(user_list[i])
        if(i != len(user_list)-1):
            listInString = listInString + ","
    print(listInString)

def getData():
    user_list = []
    num_limit = 10

    for num in range(num_limit):
        num = int(input("Enter a number for item " + str(num+1) + ": "))
        user_list.append(num)

    return user_list

def average(integer_list):
    total = 0

    for value in integer_list:
        total += value

    averageVal = total / len(integer_list)

    return averageVal


def minimum(integer_list):
    lowest_integer = min(integer_list)

    return lowest_integer


def maximum(integer_list):
    highest_integer = max(integer_list)

    return highest_integer


if __name__ == '__main__':
    main()