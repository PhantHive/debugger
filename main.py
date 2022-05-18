from schools.ipsa import Epita


if __name__ == '__main__':

    ai_org = Epita("AI", 5)
    ai_org.add_budget(5000)
    print("Nouvelle association: AI")
    print("\nBudget initial: 5000 euros")

    members = {
        "Thomas Coco": {
            "age": 22,
            "mail": "thomas.coco@ipsa.fr"
        },
        "Frero de Jean": {
            "age": 0,
            "mail": "fero.de-jean@ipsa.fr"
        },
        "Mortier Capricano": {
            "age": 15,
            "mail": "mortier.capricano@ipsa.fr"
        },
        "Portera Cati": {
            "age": 5,
            "mail": "portera.cati@ipsa.fr"
        },
        "Raryfime Geatre": {
            "age": 200,
            "mail": "raryfime.geatre@ipsa.fr"
        },
        "Polo Delte": {
            "age": 1500,
            "mail": "polo.delte@ipsa.fr"
        },
        "Thor": {
            "age": 5500,
            "mail": "thor@ipsa.fr"
        }
    }

    names = list(members.keys())
    print(f"\n{names}")

    for i in range(len(members)):

        name = names[i]
        age = members[name]["age"]
        mail = members[name]["mail"]
        ai_org.add_member(name, age, mail)

    ai_org.add_budget(15000)
    print("\nBudget supplémentaire de 15000euros")
    print("\n\nBudget asso: 15000euros")
    ai_org.remove_member("Polo Delte")







