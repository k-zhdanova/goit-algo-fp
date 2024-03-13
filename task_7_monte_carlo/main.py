import random
import matplotlib.pyplot as plt

def simulate_dice_throws(n):
    counts = {total: 0 for total in range(2, 13)}
    
    for _ in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        counts[total] += 1
    
    probabilities = {total: count / n for total, count in counts.items()}
    return probabilities


def main():
    # Симуляція 100000 кидків кубиків
    n = 100000
    probabilities = simulate_dice_throws(n)

    # Створення графіка для візуалізації результатів
    totals = list(probabilities.keys())
    prob_values = [probabilities[total] for total in totals]

    plt.figure(figsize=(10, 6))
    plt.bar(totals, prob_values, color='skyblue')
    plt.xlabel('Сума двох кубиків')
    plt.ylabel('Ймовірність')
    plt.title(f'Ймовірності сум двох кубиків при {n} кидках')
    plt.xticks(totals)
    plt.show()


if __name__ == "__main__":
    main()
