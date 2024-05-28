"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
The LCA is defined as the lowest node in the tree that has both nodes as descendants
(where we allow a node to be a descendant of itself).
"""


class TreeNode:

    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    """
    Function to find the lowest common ancestor of two nodes in a binary tree.

    :param root: TreeNode, the root of the binary tree
    :param p: TreeNode, one of the target nodes
    :param q: TreeNode, the other target node
    :return: TreeNode, the lowest common ancestor of the two nodes
    """

    if root == None or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left is not None and right is not None:
        return root

    return left if left is not None else right


if __name__ == "__main__":

    def test_lowest_common_ancestor():
        """
        Function to test the lowest_common_ancestor function with various test cases.
        """

        # Helper function to build a binary tree from a list of values
        def build_tree(nodes):
            val, left, right = nodes
            root = TreeNode(val)
            root.left = build_tree(left) if left else None
            root.right = build_tree(right) if right else None
            return root

        # Test case 1: General case with common ancestor in the middle of the tree
        # Tree Structure:
        #        3
        #       / \
        #      5   1
        #     / \ / \
        #    6  2 0  8
        #      / \
        #     7   4
        root1 = build_tree(
            (
                3,
                (5, (6, None, None), (2, (7, None, None), (4, None, None))),
                (1, (0, None, None), (8, None, None)),
            )
        )
        p1 = root1.left  # Node 5
        q1 = root1.left.right.right  # Node 4
        assert (
            lowest_common_ancestor(root1, p1, q1).val == 5
        ), "Test Case 1 Failed"

        # Test case 2: Both nodes are direct children of root
        # Tree Structure:
        #       3
        #      / \
        #     5   1
        root2 = build_tree((3, (5, None, None), (1, None, None)))
        p2 = root2.left  # Node 5
        q2 = root2.right  # Node 1
        assert (
            lowest_common_ancestor(root2, p2, q2).val == 3
        ), "Test Case 2 Failed"

        # Test case 3: LCA is root itself
        # Tree Structure:
        #       3
        #      /
        #     5
        #    / \
        #   6   2
        root3 = build_tree((3, (5, (6, None, None), (2, None, None)), None))
        p3 = root3.left  # Node 5
        q3 = root3.left.left  # Node 6
        assert (
            lowest_common_ancestor(root3, p3, q3).val == 5
        ), "Test Case 3 Failed"

        # Test case 4: Both nodes are on the same subtree
        # Tree Structure:
        #       3
        #      / \
        #     5   1
        #        / \
        #       0   8
        root4 = build_tree(
            (3, (5, None, None), (1, (0, None, None), (8, None, None)))
        )
        p4 = root4.right.left  # Node 0
        q4 = root4.right.right  # Node 8
        assert (
            lowest_common_ancestor(root4, p4, q4).val == 1
        ), "Test Case 4 Failed"

        # Test case 5: Nodes are the same
        # Tree Structure:
        #       3
        #      / \
        #     5   1
        root5 = build_tree((3, (5, None, None), (1, None, None)))
        p5 = root5.left  # Node 5
        q5 = root5.left  # Node 5 (same as p5)
        assert (
            lowest_common_ancestor(root5, p5, q5).val == 5
        ), "Test Case 5 Failed"

        print("All test cases passed!")

    if __name__ == "__main__":
        test_lowest_common_ancestor()

    test_lowest_common_ancestor()
