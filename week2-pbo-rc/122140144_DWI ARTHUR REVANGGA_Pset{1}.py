import random

class Father:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Mother:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Child:
    def __init__(self, father, mother):
        self.father_blood_type = father.blood_type
        self.mother_blood_type = mother.blood_type
        self.child_blood_type = self.inheritance()

    def inheritance(self):
        alleles = {
            "O" : ["O", "O"],
            "A" : ["A", "A"],
            "A" : ["A", "O"],
            "B" : ["B", "B"],
            "B" : ["B", "O"],
            "AB" : ["A", "B"]
        }
        
        father_allele = random.choice(self.father_blood_type)
        mother_allele = random.choice(self.mother_blood_type)

        child_blood_type = father_allele + mother_allele
        return child_blood_type

father_blood_type = input("Enter father's blood type: ")
mother_blood_type = input("Enter mother's blood type: ")

father = Father(father_blood_type)
mother = Mother(mother_blood_type)
child = Child(father, mother)

print(f"Child's blood type: {child.child_blood_type}")
