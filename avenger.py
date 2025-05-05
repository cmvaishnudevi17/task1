class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
    
    def get_info(self):
        return (f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Super Power: {self.super_power}\n"
                f"Weapon: {self.weapon}\n")
    
    def is_leader(self):
        # Captain America is traditionally considered the leader of the Avengers
        return self.name == "Captain America"

# Create the Avengers team
super_heroes = [
    Avenger("Captain America", 105, "Male", "Super strength", "Shield"),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 49, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 42, "Male", "Fighting skills", "Bow and Arrows")
]

# Display information about each Avenger
for hero in super_heroes:
    print(hero.get_info())
    print(f"Is {hero.name} the leader? {'Yes' if hero.is_leader() else 'No'}")
    print("-" * 40)
