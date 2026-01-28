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
        if self.root:
            ptr=self.root
            if value < ptr.val:
                if ptr.left:
                    ...


    def search(self, value):
        pass

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

    def findMin(self):
        pass

    def findMax(self):
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

    def depth(self):
        pass

    def clear(self):
        pass

    def destroy_tree(self):
        pass


