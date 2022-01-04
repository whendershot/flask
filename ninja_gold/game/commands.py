from typing import ClassVar
import random
from datetime import datetime, timezone

from game.command import Command

class VisitFarm(Command):
    """"""
    MIN_GOLD: ClassVar[int] = 10
    MAX_GOLD: ClassVar[int] = 20

    def __init__(self):
        self.gold_earned = random.randint(self.MIN_GOLD, self.MAX_GOLD)
        self.executed_ts = datetime.now(timezone.utc)

    def execute(self, target) -> Command:
        print(target)
        target['gold_held'] += self.gold_earned
        target['transaction_hist'].append(self.result_string())
        return self

    def result_string(self) -> str:
        return f"Earned {self.gold_earned} gold from the farm! ({self.executed_ts})"

    def display_name () -> str:
        return f"Farm"

    def describe_string() -> str:
        return f"(earns {VisitFarm.MIN_GOLD}-{VisitFarm.MAX_GOLD} gold)"

class VisitCave(Command):
    """"""
    MIN_GOLD: ClassVar[int] = 5
    MAX_GOLD: ClassVar[int] = 10

    def __init__(self):
        self.gold_earned = random.randint(self.MIN_GOLD, self.MAX_GOLD)
        self.executed_ts = datetime.now(timezone.utc)

    def result_string(self) -> str:
        return f"Earned {self.gold_earned} gold from the cave! ({self.executed_ts})"

    def describe_string() -> str:
        return f"(earns {VisitCave.MIN_GOLD}-{VisitCave.MAX_GOLD} gold)"

    def display_name () -> str:
        return f"Cave"

    def execute(self, target) -> Command:
        print(target)
        target['gold_held'] += self.gold_earned
        target['transaction_hist'].append(self.result_string())
        return self

class VisitHouse(Command):
    """"""
    MIN_GOLD: ClassVar[int] = 2
    MAX_GOLD: ClassVar[int] = 5

    def __init__(self):
        self.gold_earned = random.randint(self.MIN_GOLD, self.MAX_GOLD)
        self.executed_ts = datetime.now(timezone.utc)

    def result_string(self) -> str:
        return f"Earned {self.gold_earned} gold from the house! ({self.executed_ts})"

    def describe_string() -> str:
        return f"(earns {VisitHouse.MIN_GOLD}-{VisitHouse.MAX_GOLD} gold)"

    def display_name () -> str:
        return f"House"
    
    def execute(self, target) -> Command:
        print(target)
        target['gold_held'] += self.gold_earned
        target['transaction_hist'].append(self.result_string())
        return self

class VisitCasino(Command):
    """"""
    MIN_GOLD: ClassVar[int] = -50
    MAX_GOLD: ClassVar[int] = 50

    def __init__(self):
        self.gold_earned = random.randint(self.MIN_GOLD, self.MAX_GOLD)
        self.executed_ts = datetime.now(timezone.utc)

    def result_string(self) -> str:
        if self.gold_earned > 0:
            return f"Entered a casino and won {self.gold_earned} gold! Lucky! ({self.executed_ts})"
        else:
            return f"Entered a casino an lost {abs(self.gold_earned)} gold... Ouch.. ({self.executed_ts})"

    def describe_string() -> str:
        return f"(earns/takes 0-{VisitCasino.MAX_GOLD} gold)"

    def display_name () -> str:
        return f"Casino"

    def execute(self, target) -> Command:
        print(target)
        target['gold_held'] += self.gold_earned
        target['transaction_hist'].append(self.result_string())
        return self