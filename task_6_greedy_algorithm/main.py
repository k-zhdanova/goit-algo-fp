def greedy_algorithm(items, budget):
    # Сортування страв за співвідношенням калорійності до вартості
    sorted_items = sorted(
        items.keys(),
        key=lambda x: items[x]["calories"] / items[x]["cost"],
        reverse=True,
    )
    selected_items = {}
    total_calories = 0

    for item in sorted_items:
        if items[item]["cost"] <= budget:
            selected_items[item] = items[item]
            budget -= items[item]["cost"]
            total_calories += items[item]["calories"]
            if budget <= 0:
                break

    return selected_items, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.keys())
    dp_table = [[0 for x in range(budget + 1)] for x in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if items[item_list[i - 1]]["cost"] <= w:
                dp_table[i][w] = max(
                    items[item_list[i - 1]]["calories"]
                    + dp_table[i - 1][w - items[item_list[i - 1]]["cost"]],
                    dp_table[i - 1][w],
                )
            else:
                dp_table[i][w] = dp_table[i - 1][w]

    # Визначення вибраних страв
    selected_items = {}
    total_calories = dp_table[n][budget]
    w = budget
    for i in range(n, 0, -1):
        if dp_table[i][w] != dp_table[i - 1][w]:
            selected_items[item_list[i - 1]] = items[item_list[i - 1]]
            w -= items[item_list[i - 1]]["cost"]

    return selected_items, total_calories


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    budget = 100

    selected_items, total_calories = greedy_algorithm(items, budget)
    print("Greedy Algorithm")
    print("Selected items:", selected_items)
    print("Total calories:", total_calories)

    selected_items, total_calories = dynamic_programming(items, budget)
    print("\nDynamic Programming")
    print("Selected items:", selected_items)
    print("Total calories:", total_calories)
    


if __name__ == "__main__":
    main()
