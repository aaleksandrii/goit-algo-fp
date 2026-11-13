import heapq


def dijkstra(
    graph: dict[str, dict[str, int]],
    start: str,
) -> dict[str, int | float]:
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        current_dist, current_vertex = heapq.heappop(heap)

        if current_dist > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


graph: dict[str, dict[str, int]] = {
    "A": {"B": 4, "C": 1},
    "B": {"A": 4, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 5},
    "D": {"B": 1, "C": 5, "E": 3},
    "E": {"D": 3},
    "F": {},
}

start = "A"
distances = dijkstra(graph, start)

print(f"Shortest distances from a vertex '{start}':")
for vertex, dist in sorted(distances.items()):
    print(f"  {start} -> {vertex}: {dist}")