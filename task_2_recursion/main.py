import matplotlib.pyplot as plt
import numpy as np


def draw_tree(x, y, angle, length, depth):
    if depth == 0:
        return
    x_end = x + int(np.cos(np.radians(angle)) * length)
    y_end = y + int(np.sin(np.radians(angle)) * length)

    plt.plot([x, x_end], [y, y_end], "k-")

    new_length = length * 0.8  # Зменшення довжини гілок на кожному кроці

    # Рекурсивний виклик для двох нових гілок
    draw_tree(x_end, y_end, angle - 45, new_length, depth - 1)
    draw_tree(x_end, y_end, angle + 45, new_length, depth - 1)


def main():
    # Ask user for the depth of the tree
    depth = int(input("Enter the depth of the tree: "))
    while depth < 1:
        print("Depth must be greater than 0")
        depth = int(input("Enter the depth of the tree: "))

    # Налаштування графіка
    plt.figure(figsize=(10, 8))
    plt.axis("off")

    # Виклик функції для відображення дерева
    draw_tree(
        0, 0, 90, 70, depth
    )  # Розташування кореня (0,0), початковий кут 90 градусів, довжина 70, глибина рекурсії 10

    plt.show()


if __name__ == "__main__":
    main()
