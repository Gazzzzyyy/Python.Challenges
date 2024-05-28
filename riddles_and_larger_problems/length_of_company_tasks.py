"""
You are working as a project manager for a tech company. Your team is planning a complex software development project,
and you need to determine the longest path of dependent tasks to understand the critical path that will determine
the project duration. The project tasks and their dependencies are represented as a directed graph
where each node is a task and each edge indicates a dependency.

Implement a function find_longest_paths(tasks) that finds all the longest possible trajectories (critical paths)
in the project. If multiple trajectories have the same length, return all of them.

The tasks and dependencies are represented as follows:

tasks = {
    'Start': ['Design', 'Documentation'],
    'Design': ['Development'],
    'Development': ['Testing'],
    'Documentation': ['Review'],
    'Review': ['Testing'],
    'Testing': ['Deployment'],
    'Deployment': ['End'],
    'End': []
}
"""


def find_longest_paths(tasks):
    """
    Find the longest possible trajectories in the project. If multiple trajectories have the same length, return all of them.

    Args:
    tasks (dict): The adjacency list of tasks and their dependencies.

    Returns:
    list: A list of lists, where each sublist represents a longest trajectory (critical path).
    """

    if "Start" not in tasks:
        raise KeyError("Expected a start point for projects")

    stack = [("Start", ["Start"])]

    max_length = 0
    longest_path = []

    while stack:

        vertex, current_path = stack.pop()

        if tasks[vertex]:

            for neighbour in tasks[vertex]:
                stack.append((neighbour, current_path + [neighbour]))

        else:

            # nothing else to add. Find the length of path

            current_length = len(current_path)

            if current_length > max_length:
                max_length = current_length
                longest_path = [current_path]

            else:
                # handle multiple paths of the same length
                longest_path.append(current_path)

    return longest_path


if __name__ == "__main__":

    # Test cases
    test_cases = [
        {
            "tasks": {
                "Start": ["Design", "Documentation"],
                "Design": ["Development"],
                "Development": ["Testing"],
                "Documentation": ["Review"],
                "Review": ["Testing"],
                "Testing": ["Deployment"],
                "Deployment": ["End"],
                "End": [],
            },
            "expected": [
                [
                    "Start",
                    "Design",
                    "Development",
                    "Testing",
                    "Deployment",
                    "End",
                ],
                [
                    "Start",
                    "Documentation",
                    "Review",
                    "Testing",
                    "Deployment",
                    "End",
                ],
            ],
        },
        {
            "tasks": {
                "Start": ["A"],
                "A": ["B"],
                "B": ["C"],
                "C": ["D"],
                "D": ["End"],
                "End": [],
            },
            "expected": [["Start", "A", "B", "C", "D", "End"]],
        },
        {
            "tasks": {
                "Start": ["A", "B"],
                "A": ["C"],
                "B": ["C"],
                "C": ["D"],
                "D": [],
            },
            "expected": [["Start", "A", "C", "D"], ["Start", "B", "C", "D"]],
        },
        {
            "tasks": {
                "Start": ["A", "B"],
                "A": ["C"],
                "B": ["D"],
                "C": ["End"],
                "D": ["End"],
                "End": [],
            },
            "expected": [
                ["Start", "A", "C", "End"],
                ["Start", "B", "D", "End"],
            ],
        },
        {
            "tasks": {
                "Start": ["A", "B", "C"],
                "A": ["D", "E"],
                "B": ["E"],
                "C": ["F"],
                "D": ["G"],
                "E": ["G", "H"],
                "F": ["H"],
                "G": ["End"],
                "H": ["End"],
                "End": [],
            },
            "expected": [
                ["Start", "A", "D", "G", "End"],
                ["Start", "A", "E", "G", "End"],
                ["Start", "A", "E", "H", "End"],
                ["Start", "B", "E", "G", "End"],
                ["Start", "B", "E", "H", "End"],
                ["Start", "C", "F", "H", "End"],
            ],
        },
        {
            "tasks": {"Start": ["End"], "End": []},
            "expected": [["Start", "End"]],
        },
        {
            "tasks": {
                "Start": ["A"],
                "A": ["B"],
                "B": [],
                "C": ["D"],
                "D": ["End"],
                "End": [],
            },
            "expected": [
                ["Start", "A", "B"]
            ],  # Note: The path 'C' -> 'D' -> 'End' is not reachable from 'Start'
        },
    ]

    def sorted_paths(paths):
        """Helper function to sort paths and elements within paths for comparison."""
        return sorted([sorted(path) for path in paths])

    for i, test_case in enumerate(test_cases):
        result = find_longest_paths(test_case["tasks"])
        assert sorted_paths(result) == sorted_paths(
            test_case["expected"]
        ), f"Test case {i + 1} failed: {result} != {test_case['expected']}"
        print(f"Test case {i + 1} passed")

    print("All test cases passed")
