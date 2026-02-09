from get_all_users import get_all_users

def update_user():
    
    auswahl_name = input("Welchen Namen bearbeiten? ➡ ")
    
    for person in get_all_users():
        if auswahl_name == person["name"]:                 
            print("Diese Person bearbeiten:", person["name"])
            new_user_info = {
                "name": input("Name: "), 
                "alter": int(input("Alter: ")), 
                "email": input("Email-Adresse: "), 
                "hobby": input("Hobby: ")
            }
        
        else:
            print("Name nicht gefunden.")   
            menu()
    