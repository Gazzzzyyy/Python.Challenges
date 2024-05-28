"""
Implement a breadth-first search (BFS) algorithm to traverse a graph. Given the following adjacency list representation
of a graph, perform BFS starting from vertex 'A':

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
"""

from collections import deque


def bfs(graph, start):

    visited = []

    queue = deque([start])

    while queue:

        vertex = queue.popleft()

        if vertex not in visited:
            visited.append(vertex)

            queue.extend(graph[vertex])

    return visited


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }

    result = bfs(graph, "A")
    print(result)  # Output: ['A', 'B', 'C', 'D', 'E', 'F']
