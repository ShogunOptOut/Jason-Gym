import json
from get_all_users import get_all_users

def save_user():    
    print("Neues Mitglied anlegen")

    userliste = get_all_users()             # Bisherige Mitglieder laden
    
    try:
        new_user = {
            "name": input("Name: "), 
            "alter": int(input("Alter: ")), 
            "email": input("Email-Adresse: "), 
            "hobby": input("Hobby: ")
            }
        
        if new_user["name"] == "":
            print("Bitte Namen ausfüllen.")
            input("Zum Menü")
            return
        
        userliste.append(new_user)

        with open("./users.json", "w", encoding="utf-8") as data:
            json.dump(userliste, data, indent = 4, ensure_ascii = False)
            
        print("Mitglied gespeichert.")
    except:
        print("Fehler beim Speichern. Bitte Name und Alter ausfüllen.")
        