import json
from get_all_users import get_all_users

def save_user():    
    print(get_all_users())
    print("Neues Mitglied anlegen")

    userliste = get_all_users()             # Bisherige Mitglieder laden

    new_user = {
        "name": input("Name: "), 
        "alter": int(input("Alter: ")), 
        "email": input("Email-Adresse: "), 
        "hobby": input("Hobby: ")
        }
    
    userliste.append(new_user)

    with open("./users.json", "w", encoding="utf-8") as data:
        json.dump(userliste, data, indent = 4, ensure_ascii = False)
        
    print("Mitglied gespeichert.")
        
        