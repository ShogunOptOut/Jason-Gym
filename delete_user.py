import json
from get_all_users import get_all_users


def delete_user():
    users = get_all_users()
    
    name_delete = input("Welches Mitglied aus der Liste löschen?\n→ ")
    
    for index, person in enumerate(users):
        if name_delete == person["name"]:
            sicherheitsfrage = input(f"""Lösche {person["name"]}? \n y / n \n→ """)
            
            if sicherheitsfrage == "y":
                users.pop(index)
    
                with open("users.json", "w", encoding="utf-8") as file:
                    json.dump(users, file, indent=2, ensure_ascii=False)
            
                print("Mitglied gelöscht.")
                return 
            else:
                print("Vorgang abgebrochen.")
        
    else:
        print("Mitglied nicht gefunden.")