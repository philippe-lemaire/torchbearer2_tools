from torchbearer2_tools.character.skills import skills
from torchbearer2_tools.character.traits import traits
from torchbearer2_tools.roller import Roller
import pyinputplus as pyip


class Character:
    def __init__(self, name):
        # Name
        self.name = name
        # Class and stock
        classes = [
            "Burglar",
            "Magician",
            "Outcast",
            "Ranger",
            "Theurge",
            "Warrior",
            "Shaman",
            "Skald",
            "Thief",
        ]
        self.class_ = pyip.inputMenu(
            choices=classes, lettered=True, prompt="Select your class…\n"
        )

        class_to_stock_dict = {
            "Burglar": "Halfling",
            "Magician": "Human",
            "Outcast": "Dwarf",
            "Ranger": "Elf",
            "Theurge": "Human",
            "Warrior": "Human",
            "Shaman": "Human",
            "Skald": "Human",
            "Thief": "Human",
        }
        self.stock = class_to_stock_dict[self.class_]
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
        # skills
        class_skills = {
            "Burglar": (
                ("cook", 3),
                ("criminal", 3),
                ("fighter", 3),
                ("hunter", 2),
                ("scout", 2),
                ("scavenger", 2),
            ),
            "Magician": (
                ("arcanist", 4),
                ("lore master", 3),
                ("alchemist", 2),
                ("cartographer", 2),
                ("scholar", 2),
            ),
            "Outcast": (
                ("fighter", 4),
                ("dungeoneer", 3),
                ("armorer", 2),
                ("sapper", 2),
                ("orator", 2),
                ("scout", 2),
            ),
            "Ranger": (
                ("fighter", 3),
                ("pathfinder", 3),
                ("scout", 3),
                ("hunter", 2),
                ("lore master", 2),
                ("survivalist", 2),
            ),
            "Theurge": (
                ("fighter", 3),
                ("ritualist", 3),
                ("orator", 3),
                ("healer", 2),
                ("theologian", 2),
            ),
            "Warrior": (
                ("fighter", 4),
                ("hunter", 3),
                ("commander", 2),
                ("mentor", 2),
                ("rider", 2),
            ),
            "Shaman": (
                ("ritualist", 4),
                ("theologian", 3),
                ("fighter", 2),
                ("healer", 2),
                ("scavenger", 2),
            ),
            "Thief": (
                ("criminal", 3),
                ("manipulator", 3),
                ("scout", 3),
                ("sapper", 2),
                ("fighter", 2),
            ),
            "Skald": (
                ("orator", 4),
                ("manipulator", 3),
                ("fighter", 2),
                ("lore master", 2),
                ("scholar", 2),
            ),
        }
        self.skills = {
            skill: {"rating": 0, "passed": 0, "failed": 0} for skill in skills.keys()
        }
        for skill, rating in class_skills[self.class_]:
            self.skills[skill]["rating"] = rating

        # abilities
        will_health_options = [
            "will: 6, health: 2",
            "will: 5, health: 3",
            "will: 4, health: 4",
            "will: 3, health: 5",
            "will: 2, health: 6",
        ]
        self.will = {"rating": 0, "passed": 0, "failed": 0}
        self.health = {"rating": 0, "passed": 0, "failed": 0}
        abilities_per_class_options = {
            "Burglar": [will_health_options[1]],
            "Magician": will_health_options,
            "Outcast": [will_health_options[3]],
            "Ranger": [will_health_options[2]],
            "Theurge": will_health_options,
            "Warrior": will_health_options,
            "Shaman": will_health_options,
            "Skald": will_health_options,
            "Thief": will_health_options,
        }

        selection = pyip.inputMenu(
            choices=abilities_per_class_options[self.class_],
            prompt="Pick your abilities…\n",
            blank=True,
            lettered=True,
        )

        self.will, self.health = int(selection[6]), int(selection[-1])

        # level
        self.level = 1

        # traits
        self.traits = {trait: 0 for trait in traits.keys()}
        traits_per_class = {
            "Burglar": "Hidden Depths",
            "Magician": "Wizard’s Sight",
            "Outcast": "Born of Earth and Stone",
            "Ranger": "First Born",
            "Theurge": "Touched by the Gods",
            "Warrior": "Heart of Battle",
            "Shaman": "Between Two Worlds",
            "Skald": "Voice of Thunder",
            "Thief": "Devil May Care",
        }
        self.traits[traits_per_class[self.class_]] = 1

        # upbringing (humans only)
        if self.stock == "Human":
            upbringing_skills = [
                "criminal",
                "laborer",
                "pathfinder",
                "haggler",
                "peasant",
                "survivalist",
            ]
            chosen_skill = pyip.inputMenu(
                choices=upbringing_skills,
                lettered=True,
                prompt="Select a skill given or improved by your upbringing…\n",
            )
            if self.skills[chosen_skill]["rating"] == 0:
                self.skills[chosen_skill]["rating"] = 3
            else:
                self.skills[chosen_skill]["rating"] += 1

        self.resources = {"rating": 0, "passed": 0, "failed": 0}
        self.circles = {"rating": 0, "passed": 0, "failed": 0}
        self.precedence = {"rating": 0, "passed": 0, "failed": 0}
        self.might = {"rating": 3, "passed": 0, "failed": 0}
        self.persona = 0
        self.fate = 0

        self.wises = {}

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
        self.belief = ""
        self.creed = ""
        self.instinct = ""
        self.goal = ""

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
