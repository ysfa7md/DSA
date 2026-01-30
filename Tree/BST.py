class Node:
    def __init__(self,value):
        self.right=None
        self.left=None
        self.val=value


class Tree():
    def __init__(self,value):
        self.root=Node(value)


    def insert(self, value):
        node=Node(value)
        if self.root is None:
            self.root=node
        else:
            ptr=self.root
            while ptr:
                if value == ptr.val:
                    return

                if value > ptr.val:
                    ptr=ptr.right

                else:   # if value < ptr.val:
                    ptr=ptr.left

            if ptr <value:
                ptr.right = node
            else:
                ptr.left = node




    def search(self, value):
        if self.root is None:
            raise ValueError("Tree is empty")

        ptr=self.root
        while ptr:
            if value == ptr.val:
                return True

            if value > ptr.val:
                ptr=ptr.right
            else:   # if value < ptr.val:
                ptr=ptr.left
        else:
            return False

    def delete(self):
        pass

    def inorderTraversal(self):
        pass

    def PreorderTraversal(self):
        pass

    def PostorderTraversal(self):
        pass

    def level_order_BFS(self):
        pass

    def find_min(self):
        ptr=self.root
        while ptr.left:
            ptr=ptr.left
        return ptr.val

    def find_max(self):
        ptr=self.root
        while ptr.right:
            ptr=ptr.right
        return ptr.val

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


