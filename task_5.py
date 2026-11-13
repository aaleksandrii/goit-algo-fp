from collections import deque
import uuid

import matplotlib.pyplot as plt
import networkx as nx


class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color
    self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is None:
        return graph

    stack = [(node, x, y, layer)]
    while stack:
        node, x, y, layer = stack.pop()
        graph.add_node(node.id, color=node.color, label=node.val)
        pos[node.id] = (x, y)

        if node.right is not None:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            stack.append((node.right, r, y - 1, layer + 1))
        if node.left is not None:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            stack.append((node.left, l, y - 1, layer + 1))

    return graph


def draw_tree(tree_root: Node | None, title: str = "") -> None:
    if tree_root is None:
        return

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.suptitle(title)
    plt.show()


def heap_to_tree(heap: list[int], index: int = 0) -> Node | None:
    if index >= len(heap):
        return None

    root = Node(heap[index])
    stack = [(root, index)]
    while stack:
        node, index = stack.pop()
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if right_index < len(heap):
            node.right = Node(heap[right_index])
            stack.append((node.right, right_index))
        if left_index < len(heap):
            node.left = Node(heap[left_index])
            stack.append((node.left, left_index))

    return root


def make_colors(count: int) -> list[str]:
    colors: list[str] = []
    for index in range(count):
        ratio = index / max(count - 1, 1)
        red = round(32 + (192 - 32) * ratio)
        green = round(64 + (224 - 64) * ratio)
        blue = round(96 + (255 - 96) * ratio)

        colors.append(f"#{red:02X}{green:02X}{blue:02X}")

    return colors


def bfs(root: Node | None, colors: list[str]) -> list[Node]:
    if root is None:
        return []

    queue = deque([root])
    order: list[Node] = []

    while queue:
        node = queue.popleft()
        node.color = colors[len(order)]
        order.append(node)

        draw_tree(root, f"BFS: step {len(order)}/{len(colors)}")

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return order


def dfs(root: Node | None, colors: list[str]) -> list[Node]:
    if root is None:
        return []

    stack = [root]
    order: list[Node] = []

    while stack:
        node = stack.pop()
        node.color = colors[len(order)]
        order.append(node)

        draw_tree(root, f"DFS: step {len(order)}/{len(colors)}")

        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

    return order


def main() -> None:
    heap = [0, 4, 1, 5, 10, 3]
    colors = make_colors(len(heap))

    root = heap_to_tree(heap)
    dfs_order = dfs(root, colors)
    print("DFS:", [node.val for node in dfs_order])

    root = heap_to_tree(heap)
    bfs_order = bfs(root, colors)
    print("BFS:", [node.val for node in bfs_order])


if __name__ == "__main__":
    main()
