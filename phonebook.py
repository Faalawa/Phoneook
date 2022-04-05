selected_option = input("what do you want to do(1-5)?")
if selected_option == "2":
    name = input("what is the contact's name?")
    phone_number = input("what is their phone number?")
    phonebook[name] = phone_number
    print("contact added successfully!")
    print(menu)

if selected_option == "3":
    name = input("what is the contact's name")
    delete_entry = input("what is the contact's name")
    print("entry deleted")
    print(menu)

if selected_option == "4":
    phonebook = {
        "Melisa": "584-394-5857",
        "Igor": "857-485-2935",
        "Jazz": "334-584-2345"
    }
    print(menu)

if selected_option == "5":
    print("Bye")
     



    
