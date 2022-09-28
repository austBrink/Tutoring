# Samuel Barker.

# 7/21/21.

# Ex 7-11.

# Program description (lines  4-7): Program will display the given properties-

# of the Lo Shu Magic Square. Program will accept 2-D list and spot if list-

# is a correctly written Lo Shu Magic Square. Program will also calculate-

# and display total number value from rows, columns, and diagonals. 



import random

# Row numbers. 

ROWS = 3

# Column numbers. 

COLS = 3

# Minimum number value. 

MIN = 1

# Max. number value.

MAX = 9 

def main():

# Create 2D list.

    vals = [[0,0,0],[0,0,0],[0,0,0]]

    userIn = 0

    # Display the list through rows and columns.



    for row in range(ROWS):

        for col in range(COLS):

            print("Give a number from 1-9 (Row " + str(row + 1) + " Column " + str(col + 1) + ")")

            userIn = input()

            vals[row][col] = int(userIn)

    # How can I update print statement after digit is entered??

    #("Give a number from 1-9 (Row 1, Column 2):")

    #("Give a number from 1-9 (Row 1, Column 3):")

    #("Give a number from 1-9 (Row 2, Column 1):")

    #("Give a number from 1-9 (Row 2, Column 2):")

    #("Give a number from 1-9 (Row 2, Column 3):")

    #("Give a number from 1-9 (Row 3, Column 1):")

    #("Give a number from 1-9 (Row 3, Column 2):")

    #("Give a number from 1-9 (Row 3, Column 3):")

            

    print()

                    

    display_square_list(vals)



    # See if list is a Lo Shu magic square.

    if magic_square(vals):

        print('\nThis is a Lo Shu Magic Square.\n')

    else:

        print('\nThis is not a Lo Shu Magic Square.\n')



# magic_square function recieves list as argument.

# List values are displayed through rows and columns. 

def display_square_list(value_list):

    for r in range(ROWS):

        for c in range(COLS):

            print(value_list[r][c], end=' ')

        print()



# magic_square function recieves list as argument. If list meets requirements,-

# function returns true. If not, function will return false. 

def magic_square(value_list):

    status = False

    # Call functions and store return values.

    is_in_range = check_range(value_list)

    is_unique = check_unique(value_list)

    is_equal_rows = check_row_sum(value_list)

    is_equal_cols = check_col_sum(value_list)

    is_equal_diag = check_diag_sum(value_list)

    # Does list meet all the requirements?

    if is_in_range and is_unique and  is_equal_rows and is_equal_cols and is_equal_diag:

        status = True

    return status



# check_range function recieves list as argument. If values from list is-

# within range, it is returned true. If not, function will return false. 

def check_range(value_list):

    status = True

    for r in range(ROWS):

        for c in range(COLS):

            if value_list[r][c] < MIN or value_list[r][c] > MAX:

                status = False

    return status



# check_unique function recieves list as argument. If value from list is-

# unique, it is returned true. If not, function will return false. 

def check_unique(value_list):

    status = True

    search_value = MIN

    count = 0

    while search_value <= MAX and status == True:

        for r in range(ROWS):

            for c in range(COLS):

                if value_list[r][c] == search_value:

                    count += 1

                if count > 1:

                    status = False

        search_value += 1

        count = 0

    return status



# check_row_sum function recieves list as argument. If value from each row is-

# equal, it is true. If not, function will return false. 

def check_row_sum(value_list):

    status = True



    # Sum calculations of the values in the first row.

    sum_row_0 = value_list[0][0] + value_list[0][1] + value_list[0][2]

    # Second row.

    sum_row_1 = value_list[1][0] + value_list[1][1] + value_list[1][2]

    # Third row.

    sum_row_2 = value_list[2][0] + value_list[2][1] + value_list[2][2]

    # If the sum of any of the rows is not equal.

    if (sum_row_0 != sum_row_1) or (sum_row_0 != sum_row_2) or (sum_row_1 != sum_row_2):

        status = False

    return status



# check_col_sum function recieves list as argument. If value from columns is-

# equal, it is true. If not, function will return false. 

def check_col_sum(value_list):

    status = True

    # Sum calculations of the values in the first column.

    sum_col_0 = value_list[0][0] + value_list[1][0] + value_list[2][0]

    # Second column.

    sum_col_1 = value_list[0][1] + value_list[1][1] + value_list[2][1]

    # Third column.

    sum_col_2 = value_list[0][2] + value_list[1][2] + value_list[2][2]

    # If the sum of any columns is not equal.

    if (sum_col_0 != sum_col_1) or (sum_col_0 != sum_col_2) or (sum_col_1 != sum_col_2):

        status = False

    return status



# check_diag_sum function recieves list as argument. If value from diagonals is-

# equal, it is true. If not, function will return false. 

def check_diag_sum(value_list):

    status = True



    # Sum calculations of the values in the first diagonal.

    sum_diag_0 = value_list[0][0] + value_list[1][1] + value_list[2][2]

    # Second diagonal.

    sum_diag_1 = value_list[2][0] + value_list[1][1] + value_list[0][2]

    if sum_diag_0 != sum_diag_1:

        status = False

    return status



# Call main function.

if __name__ == '__main__':

    main()
