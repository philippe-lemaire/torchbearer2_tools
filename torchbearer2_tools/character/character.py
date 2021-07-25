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
        # home
        homes = {
            "Elfhome (Elves only)": {
                "skills": ["healer", "mentor", "pathfinder"],
                "traits": ["Calm", "Quiet"],
            },
            "Dwarven Halls": {
                "skills": ["armorer", "laborer", "stonemason"],
                "traits": ["Cunning", "Fiery"],
            },
            "Religious Bastion": {
                "skills": ["cartographer", "scholar", "theologian"],
                "traits": ["Defender", "Scarred"],
            },
            "Bustling Metropolis": {
                "skills": ["haggler", "sailor", "steward"],
                "traits": ["Extravagant", "Jaded"],
            },
            "Wizard’s Tower": {
                "skills": ["alchemist", "lore master", "sholar"],
                "traits": ["Skeptical", "Thoughtful"],
            },
            "Remote Village": {
                "skills": ["carpenter", "peasant", "weaver"],
                "traits": ["Early Riser", "Rough Hands"],
            },
            "Busy Crossroads": {
                "skills": ["cook", "haggler", "rider"],
                "traits": ["Foolhardy", "Quick-Witted"],
            },
        }
        self.home = pyip.inputMenu(
            choices=list(homes.keys()),
            lettered=True,
            prompt="Please select your home…\n",
        )
        home_skill = pyip.inputMenu(
            choices=homes[self.home]["skills"],
            lettered=True,
            prompt="What skill did you develop at home?\n",
        )
        if self.skills[home_skill]["rating"] == 0:
            self.skills[home_skill]["rating"] = 2
        elif self.skills[home_skill]["rating"] < 4:
            self.skills[home_skill]["rating"] += 1
        else:
            print("Skill already at a rating of 4, too bad…")

        home_trait = pyip.inputMenu(
            choices=homes[self.home]["traits"],
            lettered=True,
            prompt="What trait did you gain from home?\n",
        )
        self.traits[home_trait] += 1

        # social graces
        social_skills = ["haggler", "manipulator", "orator", "persuader"]
        social_grace = pyip.inputMenu(
            choices=social_skills,
            lettered=True,
            prompt="How do you convince people that you’re right or to do what you need?\n",
        )
        if self.skills[social_grace]["rating"] == 0:
            self.skills[social_grace]["rating"] = 2
        elif self.skills[social_grace]["rating"] < 4:
            self.skills[social_grace]["rating"] += 1
        else:
            print("Skill already at a rating of 4, too bad…")

        # Specialty
        specialty_options = [
            "cartographer",
            "cook",
            "criminal",
            "dungeoneer",
            "haggler",
            "healer",
            "hunter",
            "manipulator",
            "pathfinder",
            "persuader",
            "orator",
            "rider",
            "sapper",
            "scavenger",
            "scout",
            "survivalist",
        ]
        specialty = pyip.inputMenu(
            choices=specialty_options, lettered=True, prompt="What’s your specialty?\n"
        )
        if self.skills[specialty]["rating"] == 0:
            self.skills[specialty]["rating"] = 2
        elif self.skills[specialty]["rating"] < 4:
            self.skills[specialty]["rating"] += 1
        else:
            print("Skill already at a rating of 4, too bad…")

        # wises

        self.wises = []
        wises_per_stock = {
            "Dwarf": ["Dwarven Chronicles-wise", "Shrewd Appraisal-wise"],
            "Elf": [
                "Elven Lore-wise",
                "Folly of Humanity-wise",
                "Folly of Dwarves-wise",
            ],
            "Halfling": ["Home-wise", "Needs a Little Salt-wise"],
        }
        selected_wise = pyip.inputMenu(
            choices=wises_per_stock[self.stock],
            prompt="How are you wise?\n",
            lettered=True,
        )
        self.wises.append(selected_wise)
        extra_wise = input(
            prompt="How are you wise?\nChoose a specific domain of wisdom, like a specific town, monster, thing or people."
        )
        self.wises.append(f"{extra_wise}-wise")

        # nature
        self.resources = {"rating": 0, "passed": 0, "failed": 0}
        stock_to_nature_dict = {
            "Dwarf": ["Delving", "Crafting", "Avenging Grudges"],
            "Elf": ["Singing", "Remembering", "Hiding"],
            "Halfling": ["Sneaking", "Riddling", "Merrymaking"],
            "Human": ["Boasting", "Demanding", "Running"],
        }
        self.nature = {
            "current_rating": 0,
            "max_rating": 3,
            "descriptors": stock_to_nature_dict[self.stock],
        }
        ## nature questions

        if self.stock == "Dwarf":
            dwarf_q_1 = "When your kin are slain and their halls plundered, will you spend your blood avenging them? Or will you demand a blood price from the kin slayers and council your people to let sleeping dragons lie?\n"
            dwarf_a_1 = [
                "If you would take revenge at any cost, increase Nature by one.",
                "If you would council your people to resist their blood lust, replace the Avenging Grudges descriptor with Negotiating.",
            ]
            dwarf_q_2 = "Would you plunge ever deeper into the bones of the earth looking for treasures untold? Or do you fear what you would uncover should you dig too deep?\n"
            dwarf_a_2 = [
                "If you dig ever deeper, increase your Nature by one.",
                "If you fear what lies beneath, increase your Born of Earth and Stone trait to level 2.",
            ]
            dwarf_q_3 = "Do you yearn to spend your days crafting wondrous objects from silver and gold? Or do you prefer to spend gold, preferably other people’s?\n"
            dwarf_a_3 = [
                "If you were born to craft wondrous objects, increase your Nature by one.",
                "If you yearn to spend gold, set your starting Resources to 1",
            ]
            answer1 = pyip.inputMenu(prompt=dwarf_q_1, choices=dwarf_a_1, lettered=True)
            answer2 = pyip.inputMenu(prompt=dwarf_q_2, choices=dwarf_a_2, lettered=True)
            answer3 = pyip.inputMenu(prompt=dwarf_q_3, choices=dwarf_a_3, lettered=True)
            if answer1 == dwarf_a_1[0]:
                self.nature["max_rating"] += 1
            else:
                self.nature["descriptors"] = self.nature["descriptors"][:2] + [
                    "Negociating"
                ]
            if answer2 == dwarf_a_2[0]:
                self.nature["max_rating"] += 1
            else:
                self.traits["Born of Earth and Stone"] = 2
            if answer3 == dwarf_a_3[0]:
                self.nature["max_rating"] += 1
            else:
                self.resources["rating"] = 1

        if self.stock == "Elf":
            elf_q_1 = "Have you learned the songs of creation and do you sing them to mend hearts and calm storms? Or do you focus your ancient will into crafting works of unparalleled beauty?\n"
            elf_a_1 = [
                "If you sing the ancient songs, increase your Nature by one.",
                "If you bend your will to crafting Elven artifacts, replace your Singing Nature descriptor with Enchanting.",
            ]
            elf_q_2 = "When evil stalks the world, do you confront it? Or do you retreat to the hidden places of the elves and allow time to defeat your enemies?\n"
            elf_a_2 = [
                "If you confront evil, increase your First Born trait to level 2.",
                "If you retreat and hide, increase your Nature by one.",
            ]
            elf_q_3 = "Do you yearn to follow the gulls to the sea and journey west beyond all knowledge? Or are you prepared to live a life of struggle and grief?\n"
            elf_a_3 = [
                "If you yearn to journey west, increase your Nature by one.",
                "If you are prepared to live a life of struggle, you may replace your home trait with Fiery, Curious or Restless. If you have one of these traits already, increase it by one.",
            ]
            answer1 = pyip.inputMenu(prompt=elf_q_1, choices=elf_a_1, lettered=True)
            answer2 = pyip.inputMenu(prompt=elf_q_2, choices=elf_a_2, lettered=True)
            answer3 = pyip.inputMenu(prompt=elf_q_3, choices=elf_a_3, lettered=True)
            if answer1 == elf_a_1[0]:
                self.nature["max_rating"] += 1
            else:
                self.nature["descriptors"] = self.nature["descriptors"][1:] + [
                    "Enchanting"
                ]
            if answer2 == elf_a_2[1]:
                self.nature["max_rating"] += 1
            else:
                self.traits["First Born"] = 2
            if answer3 == elf_a_3[0]:
                self.nature["max_rating"] += 1
            else:
                self.traits[home_trait] = 0
                new_trait = pyip.inputMenu(
                    choices=["Fiery", "Curious", "Restless"],
                    lettered=True,
                    prompt="Select a trait to get or increase…\n",
                )
                self.traits[new_trait] += 1

        if self.stock == "Halfling":
            halfling_q_1 = "Do you make the most out of every meal, slathering it with butter, lavishing it with syrup, worshipping it with wine? Or do you tighten your belt, shoo away guests and make fast the locks at night?\n"
            halfling_a_1 = [
                "If you make the most out of each meal, increase your Nature by one.",
                "If you tighten your belt with a grim face, replace your Merry-making descriptor with Hoarding.",
            ]
            halfling_q_2 = "When confronted by bullying big folk, do you put them in their place with a witty riddle? Or do you roll up your sleeves and showthem you’re ready to teach them a lesson?\n"
            halfling_a_2 = [
                "If you offer up a clever riddle, increase your Nature by one.",
                "If you roll up your sleeves, increase your Hidden Depths trait to level 2.",
            ]
            halfling_q_3 = "Do you sneak into dragons’ lairs just to see what all the fuss is about? Or do you prefer to announce your intentions and have a frank conversation about your concerns?\n"
            halfling_a_3 = [
                "If you sneak into dragons’ lairs, increase your Nature by one.",
                "If you announce your intentions to have a frank discussion, replace your Sneaking Nature descriptor with Demanding.",
            ]
            answer1 = pyip.inputMenu(
                prompt=halfling_q_1, choices=halfling_a_1, lettered=True
            )
            answer2 = pyip.inputMenu(
                prompt=halfling_q_2, choices=halfling_a_2, lettered=True
            )
            answer3 = pyip.inputMenu(
                prompt=halfling_q_3, choices=halfling_a_3, lettered=True
            )
            if answer1 == halfling_a_1[0]:
                self.nature["max_rating"] += 1
            else:
                self.nature["descriptors"] = self.nature["descriptors"][:2] + [
                    "Hoarding"
                ]
            if answer2 == halfling_a_2[0]:
                self.nature["max_rating"] += 1
            else:
                self.traits["Hidden Depths"] = 2
            if answer3 == halfling_a_3[0]:
                self.nature["max_rating"] += 1
            else:
                self.nature["descriptons"].remove("Sneacking")
                self.nature["descriptors"].append("Demanding")
        # set nature's current rating after the questions
        self.nature["current_rating"] = self.nature["max_rating"]

        self.circles = {"rating": 0, "passed": 0, "failed": 0}
        self.precedence = 3
        self.might = 3
        self.persona = 0
        self.fate = 0

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
