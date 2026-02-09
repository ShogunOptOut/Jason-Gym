import json
from get_all_users import get_all_users
from save_user import save_user
from update_user import update_user
from delete_user import delete_user


def print_boxed(text):
    lines = text.split('\n')
    width = max(len(s) for s in lines)

    print('┌' + '─' * (width + 2) + '┐')
    for line in lines:
        print('│ ' + line.ljust(width) + ' │')
    print('└' + '─' * (width + 2) + '┘')



def menu():
    print_boxed(
        "\n Menü\n"
        " Bitte Nummer wählen:"
        "\n 1 • Mitglieder Liste\n"
        " 2 • Mitglied hinzufügen\n"
        " 3 • Mitglied bearbeiten\n"
        " 4 • Mitglied entfernen\n"
        " 0 • Beenden\n"
    )

    eingabe = int(input("➡ "))

    
    if eingabe == 1:                
        mitglieder = get_all_users()      # Liste aus der ursprünglichen JSON-Datei holen
        
        print("\n Mitglieder Kontakte\n")
        for person in mitglieder:
            print(
                "▬"*80, "\n",
                f" Name: {person['name']}, "
                f" Alter: {person['alter']}, "
                f" Email: {person['email']}",
                f" Hobby: {person['hobby']}"  
            )
        print("▬"*80, "\n")
        input("Zurück zum Menü? ")
        
    elif eingabe == 2:
        save_user()
        
    elif eingabe == 3:
        update_user()
        
    elif eingabe == 4:
        delete_user()
        
    elif eingabe == 0:
        print("Auf Wiedersehen!")
        exit()


if __name__ == "__main__":      # falls Datei nur importiert wird, startet das Progr. nicht gleich
    while True:
        menu()