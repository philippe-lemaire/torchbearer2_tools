import random


class Dice:
    """Basic dice representation, with boolean to store if it has been exploded or not."""

    def __init__(self):
        self.value = random.randint(1, 6)
        self.exploded = False

    def __repr__(self):
        if not self.exploded and self.value == 6:
            return f"{self.value}*"
        return str(self.value)


class Roller:
    """Roller object. Instanciate and then use the Roller.roll() method to initiate a new roll,
    or Roller.reroll6() method to reroll 6s from last roll."""

    def roll(self, num_dice, reroll=False):
        """Basic roller function."""
        raw_result = [Dice() for die in range(num_dice)]
        successes = len([die for die in raw_result if die.value >= 4])
        if not reroll:
            self.last_raw_result = raw_result
            self.successes = successes
        return raw_result, successes

    def deeper_understanding(self):
        """This method rerolls one single failed dice on a roll related to one of their wises."""
        if len([die for die in self.last_raw_result if die.value <= 3]) == 0:
            print("""No wyrm to reroll""")
            return None
        index_to_remove = 0
        for index, die in enumerate(self.last_raw_result):
            if die.value <= 3:
                index_to_remove = index
        self.last_raw_result.pop(index_to_remove)
        new_dice = Dice()
        self.last_raw_result.insert(index_to_remove, new_dice)
        if new_dice.value >= 4:
            self.successes += 1
        return self.last_raw_result, self.successes

    def reroll6(self):
        """This method rerolls any 6s that came out (and eventual new 6s) when characters
        spend Persona points or use an ability allowing them to reroll 6s on their last roll."""
        to_explode = 0
        while True:
            for die in self.last_raw_result:
                if die.value == 6 and not die.exploded:
                    die.exploded = True
                    to_explode += 1

            if to_explode == 0:
                break
            new_raw_result, new_successes = self.roll(to_explode, reroll=True)
            self.last_raw_result += new_raw_result
            self.successes += new_successes
            to_explode = 0
        return self.last_raw_result, self.successes
