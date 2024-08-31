# Person and Customer Class for assignment 11
#maria harrison
#user inputs=strings name,address,phone number, customer number, do you want to be on list 
import q03

def main():
    # get the data from the user.
    print("Please enter the following data.")
    name=input("Name: ")
    address=input("Address: ")
    phone_num=input("Phone number: ")
    cust_num=int(input("Customer number: "))
    mail_list=int(input("Do you want to be in our mailing list? (0=no 1=yes): "))
    
    # object with these attributes
    Customer=q03.Customer(name, address, phone_num, cust_num, mail_list)
    
    # show/ print the data recieved.
    print()
    print("Customer created from the data you gave")
    print("------------------------------")
    print("Name:", Customer.get_name())
    print("Address:", Customer.get_address())
    print("Phone number:", Customer.get_phone_num())
    print("Customer number:", Customer.get_cust_num())
    print("Mailing List:", Customer.get_is_on_mail_list())
    
# call main function
main()