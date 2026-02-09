import json

# list = []

# def liste_speichern():
#     with open("./json/jason gym/users.json", "r", encoding="utf-8") as data:
#         persons = json.load(data)
#         for person in persons:
#             list.append(person)
#         print(list)

#################################################################

def get_all_users():              # speichert die JSON Inhalte in einer Liste
    with open("./users.json", "r", encoding="utf-8") as file:
        daten = json.load(file)
        return daten