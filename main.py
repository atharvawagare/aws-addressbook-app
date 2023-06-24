from operations import add_entry, open_entry, delete_address_book, update_entry, delete_entry, search_entry
from addressbook import AddressBook

# Get Address Book Object
ab=AddressBook().get_address_book()

choices="""
1. Add New Entry
2. Open Entry
3. Update Entry
4. Delete Entry
5. Search Entry on Specific Field
    - c_name
    - city
    - email
    - joining_fees
6. Close Address Book"""

while True:
    print(choices)
    choice=int(input("Enter Choice: "))

    if choice==1:
        mobile=input("Enter Mobile: ")
        name=input("Enter Name: ")
        city=input("Enter City: ")
        email=input("Enter Email: ")
        joining_fees=int(input("Enter Joining Fees: "))
        add_entry(ab, mobile, name, city, email, joining_fees)
        
    elif choice==2:
        mobile=input("Enter Mobile: ")
        open_entry(ab, mobile)
    
    elif choice==3:
        mobile=input("Enter Mobile: ")
        name=input("Enter Name: ")
        city=input("Enter City: ")
        email=input("Enter Email: ")
        joining_fees=int(input("Enter Joining Fees: "))
        update_entry(ab, mobile, name, city, email, joining_fees)
        
    elif choice==4:
        mobile=input("Enter Mobile: ")
        delete_entry(ab, mobile)
        
    elif choice==5:
        field=input("Enter Field: ")
        value=input("Enter Value: ")
        search_entry(ab, "info."+field.lower(), value)
        
    elif choice==6:
        delete_address_book(ab)
        print("AddressBook Deleted")
        break
    else:
        print("Bad Input")