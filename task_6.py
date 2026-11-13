def greedy_algorithm(items: dict[str, dict[str, int]], budget: int) -> tuple[list[str], int, int]:
    dishes = []
    total_cost = 0
    total_calories = 0

    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    for dish, values in sorted_items:
        cost = values["cost"]
        calories = values["calories"]

        if budget >= cost:
            budget -= cost
            dishes.append(dish)
            total_cost += cost
            total_calories += calories

    return (dishes, total_cost, total_calories)


def dynamic_programming(items: dict[str, dict[str, int]], budget: int) -> tuple[list[str], int, int]:
    dp = [0] * (budget + 1)

    chosen = {
        money: {}
        for money in range(budget + 1)
    }
    for dish, values in items.items():
        cost = values["cost"]
        calories = values["calories"]

        for money in range(budget, cost - 1, -1):
            remaining = money - cost
            candidate = dp[remaining] + calories
            if candidate > dp[money]:
                dp[money] = candidate

                chosen[money] = chosen[remaining].copy()
                chosen[money][dish] = values

    return (
        list(chosen[budget].keys()),
        sum(item["cost"] for item in chosen[budget].values()),
        sum(item["calories"] for item in chosen[budget].values())
    )


def print_result(algo: str, result: tuple[list[str], int, int]):
    dishes, total_cost, total_calories = result

    print()
    print(  f"{algo} algorithm")
    print(  f"Dishes: {", ".join(dishes)}")
    print(  f"Total cost: {total_cost}")
    print(  f"Total calories: {total_calories}")


if __name__ == "__main__":
    value = 100
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    print(f"Value: {value}")
    print_result("Greedy", greedy_algorithm(items, value))
    print_result("Dynamic Programing", dynamic_programming(items, value))
