from schools.epita import Epita


if __name__ == '__main__':

    ai_org = Epita("AI", 5)
    ai_org.add_budget(5000)


    members = {
        "Thomas Coco": {
            "age": 22,
            "mail": "thomas.coco@epita.fr"
        },
        "Frero de Jean": {
            "age": 0,
            "mail": "fero.de-jean@epita.fr"
        },
        "Mortier Capricano": {
            "age": 15,
            "mail": "mortier.capricano@epita.fr"
        },
        "Portera Cati": {
            "age": 5,
            "mail": "portera.cati@epita.fr"
        },
        "Raryfime Geatre": {
            "age": 200,
            "mail": "raryfime.geatre@epita.fr"
        },
        "Polo Delte": {
            "age": 1500,
            "mail": "polo.delte@epita.fr"
        },
        "Thor": {
            "age": 5500,
            "mail": "thor@epita.fr"
        }
    }

    names = list(members.keys())
    print(names)

    for i in range(len(members)):

        name = names[i]
        age = members[name]["age"]
        mail = members[name]["mail"]
        ai_org.add_member(name, age, mail)


    ai_org.remove_member("Polo Delte")



