"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        fish_pop_age: list = []
        bear_pop_age: list = []
        for fish in self.fish:
            if fish.age < 3:
                fish_pop_age.append(fish)
        for bear in self.bears:
            if bear.age < 5:
                bear_pop_age.append(bear)
        self.fish = fish_pop_age
        self.bears = bear_pop_age

    def bears_eating(self):
        if len(self.fish) >= 5:
            self.remove_fish(3)
            for bear in self.bears:
                bear.eat(3)

        return None

    def check_hunger(self):
        well_fed_bears: list = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                well_fed_bears.append(bear)
        self.bears = well_fed_bears

    def repopulate_fish(self):
        fish_getting_it_on = (len(self.bears) // 2) * 4
        while fish_getting_it_on > 0:
            self.fish.append(Fish())
            fish_getting_it_on -= 1

    def repopulate_bears(self):
        bears_getting_it_on = len(self.bears) // 2
        while bears_getting_it_on > 0:
            self.bears.append(Bear())
            bears_getting_it_on -= 1

    def view_river(self) -> None:
        print(f"~~~day{self.day}~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        while self.day <= 6:
            self.one_river_day()

    def remove_fish(self, amount: int):
        for _ in range(0, amount):
            self.fish.pop(0)
