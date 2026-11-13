import random


def monte_carlo_dice(n: int = 100_000, seed: int = 42) -> tuple[dict[int, int], dict[int, float]]:
    if type(n) is not int or n <= 0:
        raise ValueError("Кількість кидків n має бути додатним цілим числом.")

    rng = random.Random(seed)

    counts = {total: 0 for total in range(2, 13)}

    for _ in range(n):
        first_die = rng.randint(1, 6)
        second_die = rng.randint(1, 6)

        total = first_die + second_die
        counts[total] += 1

    probabilities = {}
    for total, count in counts.items():
        probabilities[total] = count / n

    return counts, probabilities


if __name__ == "__main__":
    n = 100_000
    counts, mc_result = monte_carlo_dice(n=n, seed=42)

    analytical = {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36,
    }

    print(f"Кількість кидків двох кубиків: {n}")
    print(f"{'Сума':>4} | {'Кількість появ':>14} | {'Монте-Карло':>12} | {'Аналітично':>12}")
    print("-" * 54)
    for total in range(2, 13):
        print(
            f"{total:>4} | {counts[total]:>14} | "
            f"{mc_result[total] * 100:>11.2f}% | "
            f"{analytical[total] * 100:>11.2f}%"
        )
