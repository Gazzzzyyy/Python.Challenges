"""
Implement a depth-first search (DFS) algorithm to traverse a graph.
Given the following adjacency list representation of a graph, perform DFS starting from vertex 'A':

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

    A
   / \
  B   C
 / \   \
D   E   \
     \ /
      F
"""


def dfs(graph, start):

    visited = []

    stack = [start]

    while stack:

        vertex = stack.pop()

        if vertex not in visited:
            visited.append(vertex)

            stack.extend(graph[vertex][::-1])

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
    result = dfs(graph, "A")
    print(result)  # Output: ['A', 'B', 'D', 'E', 'F', 'C']
