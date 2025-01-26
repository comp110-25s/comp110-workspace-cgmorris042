"""Tea Party Calculations: Bags, Treats, Cost"""

__author__: str = "730559974"


def main_planner(guests: int) -> None:
    """Total tea bags, treats, and cost"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculation for tea bags based on number of people"""
    return 2 * people


def treats(people: int) -> int:
    """Number of treats based on number of people"""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Cost based on tea and treat amount"""
    return 0.50 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
