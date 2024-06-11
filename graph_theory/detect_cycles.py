"""
You are given an undirected graph represented as an adjacency list. Your task is to detect all the cycles in the graph.
A cycle is defined as a path of edges and vertices wherein a vertex is reachable from itself.

Write a function find_cycles(graph) that takes in a graph and returns a list of lists, where each list represents a
cycle detected in the graph. Each cycle should be represented as a list of vertices in the order they are visited,
starting and ending with the same vertex. Each cycle should be listed only once, regardless of its starting point.
"""


def find_cycles(graph):
    """
    Finds all cycles in an undirected graph using Depth-First Search.

    Parameters:
    graph (dict): A dictionary representing the graph as an adjacency list.

    Returns:
    list: A list of lists, where each list represents a cycle detected in the graph.
    """

    def dfs(v, parent):
        visited.add(v)
        stack.append(v)

        for neighbor in graph.get(v, []):
            if neighbor == parent:
                continue
            if neighbor in stack:
                cycle_start_index = stack.index(neighbor)
                cycle = stack[cycle_start_index:] + [neighbor]
                cycle.sort()  # Sort to avoid duplicates due to order
                if cycle not in cycles:
                    cycles.append(cycle)
            elif neighbor not in visited:
                dfs(neighbor, v)

        stack.pop()

    visited = set()
    stack = []
    cycles = []

    for node in graph:
        if node not in visited:
            dfs(node, None)

    # Check for single edge cycles
    for node in graph:
        for neighbor in graph[node]:
            if node < neighbor:  # Ensure each edge is considered once
                cycles.append([node, neighbor, node])

    return cycles


# Example usage:
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print(find_cycles(graph))
