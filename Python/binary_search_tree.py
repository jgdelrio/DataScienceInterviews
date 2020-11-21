# Created by Jose del Rio 2020/08/30
# Copyright 2020 Jose del Rio. All rights reserved.
#

# Problem statement:
# -----------------
#   Binary search tree (BST) is a binary tree where the value of each node is larger or equal
#   to the values in all the nodes in that node's left subtree and is smaller than the values
#   in all the nodes in that node's right subtree.
#
#   Write a function that, efficiently with respect to time used,
#   checks if a given binary search tree contains a given value.
#
#   For example, for the following tree:
#      n1 (Value: 1, Left: null, Right: null)
#      n2 (Value: 2, Left: n1, Right: n3)
#      n3 (Value: 3, Left: null, Right: null)
#
#   Call to contains(n2, 3) should return True since a tree with root at n2 contains number 3.


from collections import namedtuple


Node = namedtuple('Node', ['left', 'right', 'value'])


def contains(root, value):
    if root is None:
        return False
    elif root.value == value:
        return True
    elif root.left is None and root.right is None:
        return False

    if root.value > value:
        return contains(root.left, value)
    else:
        return contains(root.right, value)


def test_contains_True():
    # Create tree
    n1 = Node(value=1, left=None, right=None)
    n3 = Node(value=3, left=None, right=None)
    n2 = Node(value=2, left=n1, right=n3)
    # Get output
    result = contains(n2, 3)

    assert result is True


def test_contains_False():
    # Create tree
    n1 = Node(value=1, left=None, right=None)
    n3 = Node(value=3, left=None, right=None)
    n2 = Node(value=2, left=n1, right=n3)
    # Get output
    result = contains(n2, 5)

    assert result is False


if __name__ == "__main__":
    test_contains_False()
