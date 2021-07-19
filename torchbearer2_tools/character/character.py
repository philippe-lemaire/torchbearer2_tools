from torchbearer2_tools.character.skills import skills
from torchbearer2_tools.character.traits import traits
from torchbearer2_tools.roller import Roller


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
        self.precedence = {"rating": 0, "passed": 0, "failed": 0}
        self.might = {"rating": 3, "passed": 0, "failed": 0}
        self.persona = 0
        self.fate = 0
        self.skills = {
            skill: {"rating": 0, "passed": 0, "failed": 0} for skill in skills.keys()
        }
        self.wises = {}
        self.traits = {trait: 0 for trait in traits.keys()}
        stock_to_nature_dict = {
            "Dwarf": ["Delving", "Crafting", "Avenging Grudges"],
            "Elf": ["Singing", "Remembering", "Hiding"],
            "Halfling": ["Sneaking", "Riddling", "Merrymaking"],
            "Human": ["Boasting", "Demanding", "Running"],
        }
        self.nature = {
            "current_rating": 3,
            "max_rating": 3,
            "descriptors": stock_to_nature_dict[self.stock],
        }
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
        self.friends = []
        self.enemies = []
        self.inventory = {}
        self.weapon = ""

    def __str__(self):
        return f"""{self.name} is a level {self.level} {self.stock} {self.class_}.
        Current conditions are: {" and ".join([cond for cond in self.conditions.keys() if self.conditions[cond]])}."""

    def __repr__(self):
        return f'Character("{self.name}", "{self.class_}")'

    def roll_with_nature(self, obstacle):
        without = False
        response = ""
        while response not in ["Yes", "Y", "yes", "y", "No", "N", "no", "n"]:
            response = input(
                f"""Is this action involving one of your nature’s descriptors ({", ".join(self.nature['descriptors'])})?"""
            )
        if response in ["No", "N", "no", "n"]:
            without = True

        r = Roller()
        raw_result, successes = r.roll(self.nature["rating"])
        print(f"Result: {raw_result}, {successes} successes.")
        if successes >= obstacle:
            print("You overcame the obstacle")
        else:
            print("You fell short")
            # first propose using Deeper Understanting
            if self.fate > 0:
                response = ""
                while response not in ["Yes", "Y", "yes", "y", "No", "N", "no", "n"]:
                    response = input(
                        f"Was this last roll related to one of your wises ({self.wises.keys()})?"
                    )
                if response in ["Yes", "Y", "yes", "y"]:
                    go_for_it = ""
                    while go_for_it not in [
                        "Yes",
                        "Y",
                        "yes",
                        "y",
                        "No",
                        "N",
                        "no",
                        "n",
                    ]:
                        go_for_it = input(
                            f"Do you want to spend one of your {self.fate} Fate to reroll one wyrm?"
                        )
                    if go_for_it in ["Yes", "Y", "yes", "y"]:
                        self.fate -= 1
                        raw_result, successes = r.deeper_understanding()
                    print(f"Result: {raw_result}, {successes} successes.")
                    if successes >= obstacle:
                        print("You overcame the obstacle")
                    else:
                        print("You fell short, again…")

                        # using luck to reroll 6s at the cost of 1 fate point
                        if (
                            len(
                                [
                                    die
                                    for die in r.last_raw_result
                                    if die.value == 6 and not die.exploded
                                ]
                            )
                            > 0
                            and self.fate > 0
                        ):
                            response = ""
                            while response not in [
                                "Yes",
                                "Y",
                                "yes",
                                "y",
                                "No",
                                "N",
                                "no",
                                "n",
                            ]:
                                response = input(
                                    f"Do you want to spend of of your {self.fate} Fate to reroll 6s?"
                                )
                            if response in ["Yes", "Y", "yes", "y"]:
                                self.fate -= 1
                                raw_result, successes = r.reroll6()
                            print(f"Final result: {raw_result}, {successes} successes.")
                            if successes >= obstacle:
                                print("You finally overcame the obstacle")
                            else:
                                print("You still fall short")
                                if without:
                                    print("Your nature is temporarily reduced by 1.")
                                    self.nature["current_rating"] -= 1
