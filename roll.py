import random as rng
class Dice:
    def __init__(self, size = 20, modifier = 0, amount = 1, times = 1) -> None:
        self.size = size
        self.modifier = modifier
        self.amount = amount
        self.times = times

        self.rolls = []

    def Roll(self):
        self.rolls.append(Dice.Roll(size=self.size, modifier=self.modifier, amount=self.amount, times=self.times))
        return self.rolls[-1]

    LOG = []

    @staticmethod
    def Roll(size = 20, modifier = 0, amount = 1, times = 1):
        totalroll = [f"{amount}d{size}+{modifier}x{times}"]


        for j in range(times):
            qtroll = 0
            qtrolldesc = ""
            for i in range(amount):
                qroll = rng.randint(1, size)
                qtroll += qroll
                qtrolldesc += f"{qroll}+"
            qtroll+=modifier
            qtrolldesc+=f"{modifier}"
            totalroll.append([qtrolldesc, qtroll])

        Dice.LOG.append(totalroll)
        return totalroll