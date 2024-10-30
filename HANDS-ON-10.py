class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None


class SimpleBST:
    def __init__(self):
        self.root_node = None

    def add(self, val):
        if not self.root_node:
            self.root_node = Node(val)
        else:
            self._add_rec(self.root_node, val)

    def _add_rec(self, current, val):
        if val < current.val:
            if current.left_child is None:
                current.left_child = Node(val)
            else:
                self._add_rec(current.left_child, val)
        else:
            if current.right_child is None:
                current.right_child = Node(val)
            else:
                self._add_rec(current.right_child, val)

    def locate(self, val):
        return self._locate_rec(self.root_node, val)

    def _locate_rec(self, current, val):
        if current is None:
            return False
        if current.val == val:
            return True
        elif val < current.val:
            return self._locate_rec(current.left_child, val)
        else:
            return self._locate_rec(current.right_child, val)


class FlexibleRBTree:
    RED = True
    BLACK = False

    class SubNode:
        def __init__(self, val, col=True):  # Default to RED
            self.val = val
            self.color = col
            self.left_child = None
            self.right_child = None

    def __init__(self):
        self.base_node = None

    def add(self, val):
        self.base_node = self._add_node(self.base_node, val)
        self.base_node.color = self.BLACK

    def _add_node(self, current, val):
        if not current:
            return self.SubNode(val, self.RED)

        if val < current.val:
            current.left_child = self._add_node(current.left_child, val)
        elif val > current.val:
            current.right_child = self._add_node(current.right_child, val)

        if self._is_red(current.right_child) and not self._is_red(current.left_child):
            current = self._left_spin(current)
        if self._is_red(current.left_child) and self._is_red(current.left_child.left_child):
            current = self._right_spin(current)
        if self._is_red(current.left_child) and self._is_red(current.right_child):
            self._flip_colors(current)

        return current

    def _is_red(self, node):
        return node is not None and node.color == self.RED

    def _left_spin(self, node):
        right_child = node.right_child
        node.right_child = right_child.left_child
        right_child.left_child = node
        right_child.color = node.color
        node.color = self.RED
        return right_child

    def _right_spin(self, node):
        left_child = node.left_child
        node.left_child = left_child.right_child
        left_child.right_child = node
        left_child.color = node.color
        node.color = self.RED
        return left_child

    def _flip_colors(self, node):
        node.color = not node.color
        node.left_child.color = not node.left_child.color
        node.right_child.color = not node.right_child.color

    def locate(self, val):
        return self._locate(self.base_node, val)

    def _locate(self, node, val):
        if node is None:
            return False
        if val == node.val:
            return True
        elif val < node.val:
            return self._locate(node.left_child, val)
        else:
            return self._locate(node.right_child, val)


class BalancedAVLTree:
    class AVLNode:
        def __init__(self, val):
            self.val = val
            self.left_child = None
            self.right_child = None
            self.height = 1

    def __init__(self):
        self.main_node = None

    def add(self, val):
        self.main_node = self._add_node(self.main_node, val)

    def _add_node(self, current, val):
        if not current:
            return self.AVLNode(val)
        if val < current.val:
            current.left_child = self._add_node(current.left_child, val)
        else:
            current.right_child = self._add_node(current.right_child, val)

        current.height = 1 + max(self._height(current.left_child), self._height(current.right_child))

        balance = self._balance(current)

        if balance > 1 and val < current.left_child.val:
            return self._rotate_right(current)
        if balance < -1 and val > current.right_child.val:
            return self._rotate_left(current)
        if balance > 1 and val > current.left_child.val:
            current.left_child = self._rotate_left(current.left_child)
            return self._rotate_right(current)
        if balance < -1 and val < current.right_child.val:
            current.right_child = self._rotate_right(current.right_child)
            return self._rotate_left(current)

        return current

    def _height(self, node):
        return 0 if not node else node.height

    def _balance(self, node):
        return 0 if not node else self._height(node.left_child) - self._height(node.right_child)

    def _rotate_left(self, z):
        y = z.right_child
        T2 = y.left_child

        y.left_child = z
        z.right_child = T2

        z.height = 1 + max(self._height(z.left_child), self._height(z.right_child))
        y.height = 1 + max(self._height(y.left_child), self._height(y.right_child))

        return y

    def _rotate_right(self, y):
        x = y.left_child
        T2 = x.right_child

        x.right_child = y
        y.left_child = T2

        y.height = 1 + max(self._height(y.left_child), self._height(y.right_child))
        x.height = 1 + max(self._height(x.left_child), self._height(x.right_child))

        return x

    def locate(self, val):
        return self._locate_node(self.main_node, val)

    def _locate_node(self, node, val):
        if not node:
            return False
        if node.val == val:
            return True
        elif val < node.val:
            return self._locate_node(node.left_child, val)
        else:
            return self._locate_node(node.right_child, val)
bst = SimpleBST()
for n in [5, 3, 7, 2, 4, 6, 8]:
    bst.add(n)
print("BST Search:", bst.locate(5), bst.locate(10))


rbt = FlexibleRBTree()
for n in [5, 3, 7, 2, 4, 6, 8]:
    rbt.add(n)
print("Red-Black Tree Search:", rbt.locate(5), rbt.locate(10))


avl = BalancedAVLTree()
for n in [5, 3, 7, 2, 4, 6, 8]:
    avl.add(n)
print("AVL Tree Search:", avl.locate(5), avl.locate(10))
