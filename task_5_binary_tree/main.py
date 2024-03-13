import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue
from task_4_pyramid.main import draw_tree, build_heap_tree


def generate_color(visit_order, total_nodes):
    gradient = 255 / total_nodes
    color_intensity = int(gradient * visit_order)
    return f"#{color_intensity:02x}{255-color_intensity:02x}ff"


# Глобальний лічильник для відслідковування порядку відвідування вузлів
visit_counter = 0


def dfs_coloring(node, total_nodes):
    global visit_counter
    if node is not None:
        visit_counter += 1
        node.color = generate_color(visit_counter, total_nodes)
        dfs_coloring(node.left, total_nodes)
        dfs_coloring(node.right, total_nodes)


def bfs_coloring(root, total_nodes):
    if root is None:
        return
    global visit_counter
    visit_counter = 0
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        visit_counter += 1
        node.color = generate_color(visit_counter, total_nodes)
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)


def main():
    heap_array = [1, 6, 5, 7, 8, 9, 10, 17, 19, 21, 22, 25, 33, 36, 40]
    heapq.heapify(heap_array)
    heap_tree = build_heap_tree(heap_array)

    total_nodes = len(heap_array)
    # Використання DFS або BFS для обходу дерева
    # dfs_coloring(heap_tree, total_nodes)
    bfs_coloring(heap_tree, total_nodes)

    draw_tree(heap_tree)


if __name__ == "__main__":
    main()
