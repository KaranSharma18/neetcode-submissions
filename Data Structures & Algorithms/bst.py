from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # ── INSERT ────────────────────────────────────────────────────────────────
    # Time: O(h)  Space: O(h) call stack  |  h = log n balanced, n worst case

    def insert(self, val: int) -> None:
        self.root = self._insert(self.root, val)

    def _insert(self, node: Optional[TreeNode], val: int) -> TreeNode:
        if not node:
            return TreeNode(val)           # found the right empty spot
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        # val == node.val: duplicate → ignore
        return node

    # ── SEARCH ────────────────────────────────────────────────────────────────
    # Time: O(h)  Space: O(h) call stack

    def search(self, val: int) -> bool:
        return self._search(self.root, val)

    def _search(self, node: Optional[TreeNode], val: int) -> bool:
        if not node:
            return False
        if val == node.val:
            return True
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)

    # ── DELETE ────────────────────────────────────────────────────────────────
    # Time: O(h)  Space: O(h) call stack
    #
    # Three cases:
    #   1. Leaf node (no children)  → just remove it
    #   2. One child                → replace node with that child
    #   3. Two children             → replace value with inorder successor
    #                                 (smallest in right subtree), then delete successor

    def delete(self, val: int) -> None:
        self.root = self._delete(self.root, val)

    def _delete(self, node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not node:
            return None                    # val not found, nothing to delete

        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Case 1: leaf
            if not node.left and not node.right:
                return None

            # Case 2: one child
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            # Case 3: two children
            successor = self._min_node(node.right)   # smallest in right subtree
            node.val = successor.val                  # overwrite with successor's value
            node.right = self._delete(node.right, successor.val)  # remove successor

        return node

    # ── MIN / MAX ─────────────────────────────────────────────────────────────
    # Time: O(h)  Space: O(1)

    def find_min(self) -> Optional[int]:
        if not self.root:
            return None
        return self._min_node(self.root).val

    def _min_node(self, node: TreeNode) -> TreeNode:
        while node.left:               # keep going left until no more left child
            node = node.left
        return node

    def find_max(self) -> Optional[int]:
        if not self.root:
            return None
        node = self.root
        while node.right:              # keep going right until no more right child
            node = node.right
        return node.val

    # ── HEIGHT ────────────────────────────────────────────────────────────────
    # Time: O(n)  Space: O(h) call stack

    def height(self) -> int:
        return self._height(self.root)

    def _height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    # ── INORDER TRAVERSAL: Left → Root → Right ────────────────────────────────
    # Produces sorted output for a valid BST
    # Time: O(n)  Space: O(n)

    def inorder(self) -> list:
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: Optional[TreeNode], result: list) -> None:
        if not node:
            return
        self._inorder(node.left, result)
        result.append(node.val)
        self._inorder(node.right, result)

    # ── PREORDER TRAVERSAL: Root → Left → Right ───────────────────────────────
    # Useful for copying or serializing a tree
    # Time: O(n)  Space: O(n)

    def preorder(self) -> list:
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node: Optional[TreeNode], result: list) -> None:
        if not node:
            return
        result.append(node.val)
        self._preorder(node.left, result)
        self._preorder(node.right, result)

    # ── POSTORDER TRAVERSAL: Left → Right → Root ─────────────────────────────
    # Useful for deletion (children deleted before parent)
    # Time: O(n)  Space: O(n)

    def postorder(self) -> list:
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node: Optional[TreeNode], result: list) -> None:
        if not node:
            return
        self._postorder(node.left, result)
        self._postorder(node.right, result)
        result.append(node.val)

    # ── LEVEL ORDER TRAVERSAL (BFS) ───────────────────────────────────────────
    # Returns nodes level by level, left to right
    # Time: O(n)  Space: O(n)

    def level_order(self) -> list:
        if not self.root:
            return []
        result = []
        queue = deque([self.root])
        while queue:
            level = []
            for _ in range(len(queue)):        # process all nodes at current level
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

    # ── BST VALIDATION ────────────────────────────────────────────────────────
    # Verifies every node satisfies: min_val < node.val < max_val
    # Time: O(n)  Space: O(h) call stack

    def is_valid_bst(self) -> bool:
        return self._is_valid(self.root, float("-inf"), float("inf"))

    def _is_valid(self, node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
        if not node:
            return True
        if not (min_val < node.val < max_val):
            return False
        return (self._is_valid(node.left, min_val, node.val) and
                self._is_valid(node.right, node.val, max_val))

    # ── PRETTY PRINT ──────────────────────────────────────────────────────────

    def __repr__(self) -> str:
        if not self.root:
            return "Empty BST"
        lines = []
        self._print_tree(self.root, "", False, lines)
        return "\n".join(lines)

    def _print_tree(self, node, prefix, is_left, lines):
        if not node:
            return
        connector = "├── " if is_left else "└── "
        lines.append(prefix + connector + str(node.val))
        child_prefix = prefix + ("│   " if is_left else "    ")
        self._print_tree(node.left, child_prefix, True, lines)
        self._print_tree(node.right, child_prefix, False, lines)


# ── COMPLEXITY SUMMARY ────────────────────────────────────────────────────────
#
# Operation      Time (avg)   Time (worst)   Space
# ─────────────────────────────────────────────────────────────────────────────
# insert         O(log n)     O(n)           O(log n) call stack
# search         O(log n)     O(n)           O(log n) call stack
# delete         O(log n)     O(n)           O(log n) call stack
# find_min/max   O(log n)     O(n)           O(1)
# height         O(n)         O(n)           O(log n) call stack
# inorder        O(n)         O(n)           O(n)
# preorder       O(n)         O(n)           O(n)
# postorder      O(n)         O(n)           O(n)
# level_order    O(n)         O(n)           O(n)
# is_valid_bst   O(n)         O(n)           O(log n) call stack
#
# Worst case (all O(n)) happens when the tree degenerates into a linked list
# — e.g. inserting already-sorted values: insert(1,2,3,4,5) gives a right-skewed chain.
# A self-balancing BST (AVL / Red-Black tree) guarantees O(log n) always.


# ── DEMO ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    bst = BST()

    for val in [10, 5, 15, 3, 7, 12, 20]:
        bst.insert(val)

    print("Tree structure:")
    print(bst)
    #      10
    #    /    \
    #   5      15
    #  / \    /  \
    # 3   7  12   20

    print("\nInorder  (sorted):", bst.inorder())    # [3, 5, 7, 10, 12, 15, 20]
    print("Preorder          :", bst.preorder())    # [10, 5, 3, 7, 15, 12, 20]
    print("Postorder         :", bst.postorder())   # [3, 7, 5, 12, 20, 15, 10]
    print("Level order       :", bst.level_order()) # [[10], [5, 15], [3, 7, 12, 20]]

    print("\nSearch 7  :", bst.search(7))    # True
    print("Search 99 :", bst.search(99))    # False

    print("\nMin:", bst.find_min())    # 3
    print("Max:", bst.find_max())     # 20
    print("Height:", bst.height())    # 3

    print("\nValid BST:", bst.is_valid_bst())    # True

    print("\n--- Delete leaf (3) ---")
    bst.delete(3)
    print("Inorder:", bst.inorder())    # [5, 7, 10, 12, 15, 20]

    print("\n--- Delete node with one child (5) ---")
    bst.delete(5)
    print("Inorder:", bst.inorder())    # [7, 10, 12, 15, 20]

    print("\n--- Delete node with two children (15) ---")
    bst.delete(15)
    print("Inorder:", bst.inorder())    # [7, 10, 12, 20]

    print("\nFinal tree:")
    print(bst)
