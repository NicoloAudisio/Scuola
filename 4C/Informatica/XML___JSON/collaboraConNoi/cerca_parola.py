import json

data = json.load(open("collabora.json"))

parola = "Collabora con noi"

print("Cerco il titolo: ", parola)

for i in range(len(data['children'][0]['children'][0]['children'])):
    if data['children'][0]['children'][0]['children'][i]["title"] == parola:
        print("Titolo:", data['children'][0]['children'][0]['children'][i]["title"],
        "\nIndice:", data['children'][0]['children'][0]['children'][i]["index"],
        "\nUrl:", data['children'][0]['children'][0]['children'][i]["uri"])