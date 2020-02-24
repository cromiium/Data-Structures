class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None 
#TODO: Add balancing
    def __insert_node(self, root, data):
        if self.root == None:
            self.root = Node(data)
        elif root == None:
            root = Node(data)
        else:
            if data <= root.data: 
                root.left = self.__insert_node(root.left, data)
            elif data > root.data:
                root.right = self.__insert_node(root.right, data)
        return root
    def insert(self, data): # Wrapper function for __insert_node
        self.__insert_node(self.root, data)

#TODO: Add remove
#TODO: Number of Leaves
#TODO: Find min/max
#TODO: Print out all root-> leaf paths per line
#TODO: Add preorder and postorder
    def __inorder_tree(self, root): 
        if root == None:
            return
        self.__inorder_tree(root.left)
        print(root.data)
        self.__inorder_tree(root.right)
    def inorder(self): # Wrapper functino for __inorder_tree
        self.__inorder_tree(self.root)

def main():
    tree1 = Tree()
    tree1.insert(1)
    tree1.insert(2)
    tree1.insert(3)
    tree1.insert(4)
    tree1.insert(5)
    tree1.inorder()
main()