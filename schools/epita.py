import csv


class Epita:
    '''
    :param nb_org: Number of Epita organization
    '''

    max_budget = 50000
    nb_org = 0

    def __init__(self, name, cmt):
        '''
        :param name: Organization name
        :param cmt: Number of committee member
        '''

        Epita.nb_org += 1

        self.nb_member = cmt
        self.budget = 0
        self.org_name = name
        self.nb_cmt = cmt
        self.cur_id = 0000
        self.file_path = f"src/epita_{self.org_name}.csv"

        with open(self.file_path, "w", newline='') as f:

            HEADER = [self.org_name, "member ID", "name", "age", "email"]
            writer = csv.writer(f)
            writer.writerow(HEADER)

            f.close()

    def add_budget(self, budget):

        temp = self.budget + budget
        if (Epita.max_budget >= temp):
            self.budget = budget
        else:
            print(f"Votre budget dépasse le budget max toléré {Epita.max_budget}")

    def add_member(self, nm, age, mail):

        self.cur_id += 1
        if type(nm) == str or type(age) == int or type(mail) == str:

            if ("@" not in mail):
                print("Vous avez saisis un mail incorrect")
            else:
                member_id = self.org_name + str(self.cur_id) + nm[0: 2].upper()
                self.save_csv(member_id, nm, age, mail)
                print("Membre ajouté")
        else:

            print("Un nom ne doit pas être un nombre, un age doit être un nombre et un mail ne doit pas être"
                  "un nombre :)")


    def save_csv(self, mb_id, nm, age, mail):

        f = open(self.file_path, "a", newline='')

        writer = csv.writer(f)
        writer.writerow([self.org_name, mb_id, nm, age, mail])

        f.close()

    def remove_member(self, nm):

        temp_list = []
        i = 0
        self.cur_id += 1
        with open(self.file_path, "r") as f:

            for row in csv.reader(f):
                if row[2] != nm:
                    temp_list.append(row)
                    temp_list[i][1] = self.org_name + str(self.cur_id) + nm[0: 2].upper()

            f.close()

        with open(self.file_path, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(temp_list)


    def __del__(self):

        Epita.nb_org -= 1
        print(f"Epita possède maintenant: {Epita.nb_org} associations.")
