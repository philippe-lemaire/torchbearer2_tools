class Character:
    def init(self, name, class_):
        self.name = name
        self.class_ = class_
        class_to_stock_dict = {
            "Burglar": "Halfling",
            "Magician": "Human",
            "Outcast": "Dwarf",
            "Ranger": "Elf",
            "Theurge": "Human",
            "Warrior": "Human",
        }
        self.stock = class_to_stock_dict[self.class_]
        self.level = 1
        self.belief = ""
        self.creed = ""
        self.instinct = ""
        self.goal = ""
        self.will = 0
        self.health = 0
        stock_to_nature_dict = {
            "Dwarf": "Delving, Crafting, Avenging Grudges",
            "Elf": "Singing, Remembering and Hiding",
            "Halfling": "Sneaking, Riddling, Merrymaking",
            "Human": "Boasting, Demanding, Running",
        }
        self.nature = [3, stock_to_nature_dict[self.stock]]
        self.conditions = {
            "fresh": False,
            "hungry_and_thirsty": False,
            "angry": False,
            "afraid": False,
            "exhausted": False,
            "injured": False,
            "sick": False,
            "dead": False,
        }

    def __repr__(self):
        return f"{self.name} is a level {self.level} {self.class_}"
