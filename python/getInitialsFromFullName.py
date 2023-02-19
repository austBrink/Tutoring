def main():
    first, middle, last = get_name()
    get_initials(first, middle, last)
    


def get_name():
    first_name = input('Enter your first name: ')

    middle_name = input('Enter your middle name: ')

    last_name = input('Enter your last name: ')

    full_name = (first_name + '\t' + middle_name + '\t' + last_name)

    return first_name, middle_name, last_name

def get_initials(first, middle, last):

    first_initial = first[0]
    middle_initial = middle[0]
    last_initial = last[0]

    print('Your initials are: ' + first_initial + middle_initial + last_initial)




if __name__ == '__main__':
    main()