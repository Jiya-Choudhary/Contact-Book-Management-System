print("Contact Book")
Contact = {"A":9427, "B":12345, "C" :20404}
print(Contact)
Options = ["Search","Update","Delete","Exit"]
Names = list(Contact.keys())
print("Options:",Options)
Choice = input("Enter Option: ")
for option in Options:
  if Choice == "Search":
    print("Search Contact")
    S= input("Enter name: ")
    if S in Names:
        print("Name:", S, "; Contact number:", Contact[S])
    else:
        print("Invalid Contact")
    print("Options:",Options)
    Choice = input("Enter Option: ")
  elif Choice == "Update":
    print("Update Contact")
    U = input("Enter name: ")
    P = int(input("Enter new contact number: "))
    if U in Contact and Contact[U]== P:
        print("Already exists")
    else:
        Contact[U] = P
        print("Updated Contact:", "Name: ", U, ", Contact number: ", Contact[U])
        print("New Contacts:", Contact)
    print("Options:",Options)
    Choice = input("Enter Option: ")
  elif Choice == "Delete":
    print("Delete Contact")
    L = input("Enter name: ")
    if L in Names:
        del Contact[L]
        print("Deleted Contact:", L)
        print("New Contacts:", Contact)
    else:
        print("Invalid Contact") 
    print("Options:",Options)
    Choice = input("Enter Option: ")
  elif Choice == "Exit": 
        print("Contact Book Closed")
        break
  else:
    print("Not in Option")