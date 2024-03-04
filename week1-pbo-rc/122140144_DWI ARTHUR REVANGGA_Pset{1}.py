class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.guard = False

    def attack_enemy(self, enemy):
        print(f"{self.name} attacks {enemy.name}!\n")
        enemy.take_damage(self.attack)

    def take_damage(self, damage):
        if self.guard:
            damage = 0
            print(f"{self.name} guard activated!\n")
        self.hp -= damage
        print(f"{self.name} takes {damage} damage. {self.name}'s HP: {self.hp}\n")

    def defend(self):
        self.guard = True
        print(f"{self.name} is guarding.\n")

    def stop_guard(self):
        self.guard = False
        print(f"{self.name} stops guarding.")

class Battle:
    def __init__(self, char1, char2):
        self.char1 = char1
        self.char2 = char2
        self.round = 1

    def play_round(self):
        print(f"Round {self.round} ==============================================")
        print(f"{self.char1.name} |{self.char1.hp}|{self.char1.attack}|")
        print(f"{self.char2.name} |{self.char2.hp}|{self.char2.attack}|\n")
        
        print("1. Attack    2. Defense  3. Give up")
        action1 = input(f"{self.char1.name}, select the action: ")
        print("\n1. Attack    2. Defense  3. Give up")
        action2 = input(f"{self.char2.name}, select the action: ")
        print("\n")

        if action1 == "1":
            if action2 == "2":
                self.char2.defend()
            self.char1.attack_enemy(self.char2)
        elif action1 == "2":
            self.char1.defend()
        elif action1 == "3":
            print(f"{self.char1.name} gives up. {self.char2.name} wins!\n")
            return True
        else:
            print("Invalid action. Please choose again. \n")
            return False

        if action2 == "1":
            self.char2.attack_enemy(self.char1)
        elif action2 == "2":
                self.char2.defend()
        elif action2 == "3":
            print(f"{self.char2.name} gives up. {self.char1.name} wins!\n")
            return True
        else:
            print("Invalid action. Please choose again. \n")
            return False
        
        if self.char1.guard == True:
            self.char1.stop_guard()

        if self.char2.guard == True:
            self.char2.stop_guard()

        self.round += 1
        return False

char1 = Character("Atreus", 500, 10)
char2 = Character("Daedalus", 750, 8)

game = Battle(char1, char2)

while not game.play_round():
    pass
