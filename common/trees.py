from collections import deque
from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None


class BinaryTree:
    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None

    # -------------------------
    # Insertion
    # -------------------------
    def insert_left(self, parent: Node, value):
        parent.left = Node(value)
        return parent.left

    def insert_right(self, parent: Node, value):
        parent.right = Node(value)
        return parent.right

    # -------------------------
    # Search
    # -------------------------
    def find(self, value):
        """DFS search for a node with the given value."""
        return self._find(self.root, value)

    def _find(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        return self._find(node.left, value) or self._find(node.right, value)

    # -------------------------
    # Traversals
    # -------------------------
    def preorder(self):
        res = []
        self._preorder(self.root, res)
        return res

    def _preorder(self, node, res):
        if not node:
            return
        res.append(node.value)
        self._preorder(node.left, res)
        self._preorder(node.right, res)

    def inorder(self):
        res = []
        self._inorder(self.root, res)
        return res

    def _inorder(self, node, res):
        if not node:
            return
        self._inorder(node.left, res)
        res.append(node.value)
        self._inorder(node.right, res)

    def postorder(self):
        res = []
        self._postorder(self.root, res)
        return res

    def _postorder(self, node, res):
        if not node:
            return
        self._postorder(node.left, res)
        self._postorder(node.right, res)
        res.append(node.value)

    def level_order(self):
        if not self.root:
            return []
        q = deque([self.root])
        res = []

        while q:
            node = q.popleft()
            res.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return res

    # -------------------------
    # Utility methods
    # -------------------------
    def count_leaves(self):
        return self._count_leaves(self.root)

    def _count_leaves(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return self._count_leaves(node.left) + self._count_leaves(node.right)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if not node:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def is_balanced(self):
        """Returns True if the tree is height-balanced."""
        return self._check_balanced(self.root)[0]

    def _check_balanced(self, node):
        if not node:
            return True, 0
        left_bal, left_h = self._check_balanced(node.left)
        right_bal, right_h = self._check_balanced(node.right)
        balanced = left_bal and right_bal and abs(left_h, right_h) <= 1
        return balanced, 1 + max(left_h, right_h)

    def to_list(self):
        """Return tree as a list using level-order."""
        return self.level_order()

    # -------------------------
    # Pretty print (for debugging)
    # -------------------------
    def print_tree(self):
        if not self.root:
            print("<empty>")
            return

        q = deque([(self.root, 0)])
        current_level = 0
        line = []

        while q:
            node, level = q.popleft()
            if level != current_level:
                print(" ".join(line))
                line = []
                current_level = level
            line.append(str(node.value))
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        print(" ".join(line))


class TernaryNode:
    def __init__(self, value, left=None, middle=None, right=None):
        self.value = value
        self.left = left
        self.middle = middle
        self.right = right

    def __repr__(self):
        return f"TernaryNode({self.value})"


class TernaryTree:
    def __init__(self, root=None):
        self.root = root

    # --------------------------------------------------
    # Traversals
    # --------------------------------------------------

    def preorder(self, node=None, visit=lambda x: print(x.value)):
        """Root → Left → Middle → Right"""
        if node is None:
            node = self.root
        if node is None:
            return

        visit(node)
        if node.left:
            self.preorder(node.left, visit)
        if node.middle:
            self.preorder(node.middle, visit)
        if node.right:
            self.preorder(node.right, visit)

    def postorder(self, node=None, visit=lambda x: print(x.value)):
        """Left → Middle → Right → Root"""
        if node is None:
            node = self.root
        if node is None:
            return

        if node.left:
            self.postorder(node.left, visit)
        if node.middle:
            self.postorder(node.middle, visit)
        if node.right:
            self.postorder(node.right, visit)
        visit(node)

    def inorder(self, node=None, visit=lambda x: print(x.value)):
        """
        A reasonable inorder definition for ternary tree:
        Left → Root → Middle → Right
        """
        if node is None:
            node = self.root
        if node is None:
            return

        if node.left:
            self.inorder(node.left, visit)
        visit(node)
        if node.middle:
            self.inorder(node.middle, visit)
        if node.right:
            self.inorder(node.right, visit)

    def level_order(self, visit=lambda x: print(x.value)):
        """Breadth-First (Level Order)"""
        if self.root is None:
            return

        q = deque([self.root])
        while q:
            node = q.popleft()
            visit(node)
            for child in (node.left, node.middle, node.right):
                if child:
                    q.append(child)

    # --------------------------------------------------
    # Utility Methods
    # --------------------------------------------------

    def height(self, node=None):
        """Return height of the tree (max depth)."""
        if node is None:
            node = self.root
        if node is None:
            return -1

        return 1 + max(
            self.height(node.left),
            self.height(node.middle),
            self.height(node.right)
        )

    def search(self, value, node=None):
        """Depth-first search for a value."""
        if node is None:
            node = self.root
        if node is None:
            return None

        if node.value == value:
            return node

        for child in (node.left, node.middle, node.right):
            if child:
                found = self.search(value, child)
                if found:
                    return found

        return None

    # --------------------------------------------------
    # Insertion (manual positioning)
    # --------------------------------------------------

    def insert_children(self, node, left=None, middle=None, right=None):
        """Attach up to three children."""
        node.left = left
        node.middle = middle
        node.right = right

    # --------------------------------------------------
    # Pretty Printing
    # --------------------------------------------------

    def pretty_print(self):
        """Print tree sideways."""
        def _print(node, prefix="", is_left=True):
            if node is None:
                return

            _print(node.right, prefix + ("│   " if is_left else "    "), False)
            print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
            _print(node.left, prefix + ("    " if is_left else "│   "), True)
            _print(node.middle, prefix + ("    " if is_left else "│   "), True)

        _print(self.root)
