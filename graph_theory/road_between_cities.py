"""
You are given an undirected, unweighted graph represented as an adjacency list. Each node in the graph represents
a city, and each edge represents a road between two cities.
You need to find out if there is a path from a starting city to a destination city. If a path exists, return
the sequence of cities in the path. If there are multiple paths, return any one of them.

Write a function find_path(graph, start, destination) that takes in the following parameters:

graph: A dictionary where keys are city names (strings) and values are lists of neighboring city names.
start: The starting city name (string).
destination: The destination city name (string).
The function should return a list of city names representing the path from the start city to the destination city.
If no path exists, return an empty list.

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
destination = 'F'

# Expected output: ['A', 'C', 'F'] or ['A', 'B', 'E', 'F']
print(find_path(graph, start, destination))
"""


def find_path(graph, start, destination):

    visited = []

    stack = [(start, [start])]

    while stack:

        city, path = stack.pop()
        if city == destination:
            return path

        if city not in visited:

            visited.append(city)

            for next_city in graph.get(city, []):
                if next_city not in visited:
                    stack.append((next_city, path + [next_city]))


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    start = "A"
    destination = "F"
    print(find_path(graph, start, destination))
