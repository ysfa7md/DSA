class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.val = value


class Tree:
    def __init__(self, value):
        self.root = Node(value)
        self.size=0

    def insert(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
            return

        ptr = self.root
        while ptr:
            if value == ptr.val:
                return

            if value > ptr.val:
                ptr = ptr.right
            else:
                ptr = ptr.left

        if ptr < value:
            ptr.right = node
        else:
            ptr.left = node

        self.size+=1

    def _search(self, node, target):
        if not node:
            return

        if node.val == target:
            return node

        elif node.val < target:
            self._search(node.right, target)
        else:
            self._search(node.left, target)

    def search(self, value):
        if self.root is None:
            raise ValueError("Tree is empty")

        return self._search(self.root, value)
        # ptr = self.root
        # while ptr:
        #     if value == ptr.val:
        #         return True

        #     if value > ptr.val:
        #         ptr = ptr.right
        #     else:  # if value < ptr.val:
        #         ptr = ptr.left

        # return False
    # TODo :-
    def delete(self,value):
        root=self.root
        if not root:
            return ValueError("Tree is empty")

        # case 1 val is the root
        if not (root.left or root.right):
            del root

        if not

    # ====================
    # helper functions
    # ====================
    values = list()

    def _in_order(self, node):
        if not node:
            return

        self._in_order(node.left)
        self.values.append(node.val)
        self._in_order(node.right)

    def _pre_order(self, node):
        if not node:
            return

        self.values.append(node.val)
        self._pre_order(node.left)
        self._pre_order(node.right)

    def _post_order(self, node):
        if not node:
            return

        self._post_order(node.left)
        self._post_order(node.right)
        self.values.append(node.val)
    # ====================

    def in_order_traversal(self):
        values = []
        root = self.root
        self._in_order(root)
        return self.values

    def pre_order_traversal(self):
        values = []
        root = self.root
        self._pre_order(root)
        return self.values

    def post_order_traversal(self):
        values = []
        root = self.root
        self._post_order(root)
        return self.values
    # ====================

    def find_min(self):
        ptr = self.root
        while ptr.left:
            ptr = ptr.left
        return ptr.val

    def find_max(self):
        ptr = self.root
        while ptr.right:
            ptr = ptr.right
        return ptr.val

    def level_order_BFS(self):
        pass

    def successor(self):
        pass

    def predecessor(self):
        pass

    def count_nodes(self):
        pass

    def is_BST(self):
        pass

    def is_balanced(self):
        pass

    def height(self):
        pass

    def clear(self):
        pass

    def destroy_tree(self):
        pass

    def __repr__(self):
        return f'BST({self.in_order_traversal()})'

    def __str__(self):
        return f'{self.in_order_traversal()}'
