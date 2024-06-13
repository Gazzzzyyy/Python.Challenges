"""
Given a set of nodes N on an undirected, positive weighted graph G and a query node n,
what is the fastest algorithm for finding the node in N that is closest to n?
"""

import heapq


def dijkstra(graph, start):
    """
    Implementation of Dijkstra's algorithm.

    Parameters:
    - graph: A dictionary where keys are node identifiers and values are lists of tuples (neighbor, weight).
    - start: The starting node identifier.

    Returns:
    - distances: A dictionary where keys are node identifiers and values are the shortest distances from start node.
    """
    # Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def find_closest_node(graph, N, query_node):
    """
    Find the closest node in set N from the query node using Dijkstra's algorithm.

    Parameters:
    - graph: A dictionary where keys are node identifiers and values are lists of tuples (neighbor, weight).
    - N: A set of target nodes.
    - query_node: The starting node identifier.

    Returns:
    - closest_node: The node in N that is closest to the query_node.
    """
    # Run Dijkstra's algorithm from the query node
    distances = dijkstra(graph, query_node)

    # Find the closest node in N
    closest_node = None
    min_distance = float('inf')
    for node in N:
        if distances[node] < min_distance:
            min_distance = distances[node]
            closest_node = node

    return closest_node


if __name__ == "__main__":

    # Example usage:
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    N = {'B', 'D'}
    query_node = 'A'

    closest_node = find_closest_node(graph, N, query_node)
    print(f"The closest node in N to {query_node} is {closest_node}.")
