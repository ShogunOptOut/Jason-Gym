import json
from get_all_users import get_all_users
from save_user import save_user

get_all_users()

def menu():
    eingabe = int(input(
        "\n Menü\n"
        "\n 1 • Mitglieder Liste\n"
        " 2 • Mitglied hinzufügen\n"
        " 3 • Mitglied bearbeiten\n"
        " 4 • Mitglied entfernen\n"
        " 0 • Beenden\n"
        "\nEingabe: ")) 
    if eingabe == 1:        
        mitglieder = get_all_users()      # Liste aus der JSON-Datei holen
        
        print("\n Mitglieder Kontakte\n")
        for person in mitglieder:
            print(
                "▬"*80, "\n",
                f" Name: {person['name']}, "
                f" Alter: {person['alter']}, "
                f" Email: {person['email']}"  
            )
        print("▬"*80, "\n")
        input("Zurück zum Menü? ")
    elif eingabe == 2:
        save_user()
        
def main():
    while True:
        menu()

if __name__ == "__main__":
    main()