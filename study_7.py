class Warrior:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount
        print(f"hero took {amount} damage now he has {self.hp} life")
        
char_name = input("please enter hero's name: ")
char_hp = int(input("please enter hero's hp: "))

hero = Warrior(char_name, char_hp)  # instance
hero.take_damage(20)
