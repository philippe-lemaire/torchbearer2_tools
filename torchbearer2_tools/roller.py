import random


class Roller:
    def roll(self, dice, reroll=False):

        raw_result = [random.randint(1, 6) for die in range(dice)]
        successes = len([die for die in raw_result if die >= 4])
        if not reroll:
            self.last_roll_dice = raw_result
            self.last_roll_successes = successes

        return raw_result, successes

    def reroll6(self):
        extra_dice = len([die for die in self.last_roll_dice if die == 6])
        extra_raw_result, extra_successes = self.roll(extra_dice, reroll=True)
        self.last_roll_dice += extra_raw_result
        self.last_roll_successes += extra_successes

        return (
            self.last_roll_dice,
            self.last_roll_successes,
        )
