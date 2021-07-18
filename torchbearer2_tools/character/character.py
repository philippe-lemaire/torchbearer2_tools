from torchbearer2_tools.character.skills import skills
from torchbearer2_tools.character.traits import traits


class Character:
    def __init__(self, name, class_):
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
        self.will = {"rating": 0, "passed": 0, "failed": 0}
        self.health = {"rating": 0, "passed": 0, "failed": 0}
        self.resources = {"rating": 0, "passed": 0, "failed": 0}
        self.circles = {"rating": 0, "passed": 0, "failed": 0}
        self.persona = 0
        self.fate = 0
        self.skills = {
            skill: {"rating": 0, "passed": 0, "failed": 0} for skill in skills.keys()
        }
        self.traits = {trait: 0 for trait in traits.keys()}
        stock_to_nature_dict = {
            "Dwarf": "Delving, Crafting, Avenging Grudges",
            "Elf": "Singing, Remembering and Hiding",
            "Halfling": "Sneaking, Riddling, Merrymaking",
            "Human": "Boasting, Demanding, Running",
        }
        self.nature = {"rating": 3, "descriptors": stock_to_nature_dict[self.stock]}
        self.conditions = {
            "fresh": True,
            "hungry_and_thirsty": False,
            "angry": False,
            "afraid": False,
            "exhausted": False,
            "injured": False,
            "sick": False,
            "dead": False,
        }

    def __repr__(self):
        return f"""{self.name} is a level {self.level} {self.class_}.
        Current conditions are: {" and ".join([cond for cond in self.conditions.keys() if self.conditions[cond]])}."""
