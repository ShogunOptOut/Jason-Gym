import json 
from get_all_users import get_all_users

DATEI = "user.json"

def update_user():
    users = get_all_users()
    auswahl_name = input("Welchen Namen bearbeiten? ➡ ")
    try:
        for index, person in enumerate(users):
            if auswahl_name == person["name"]:                 
                print("Diese Person bearbeiten:", person["name"])
                users[index] = {
                    "name": input("Neuer Name: "), 
                    "alter": int(input("Neues Alter: ")), 
                    "email": input("Neue Email-Adresse: "), 
                    "hobby": input("Neues Hobby: ")
                }

                with open("./users.json", "w", encoding="utf-8") as file:
                    json.dump(users, file, indent=2, ensure_ascii=False)
                print("Mitglied bearbeitet.")
                return
            
        print("Name nicht gefunden.")   
    except:
        print("Name nicht vorhanden.") 
        return       
    