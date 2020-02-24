class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

class Tree:
    def __init__(self,):
        self.root = None 
    

    def insert_node(self, data):
        new_node = Node(data)

        if self.root == None:
            self.root = new_node
            return

        temp_root = self.root

        if data <= temp_root.data:
            while temp_root.left != None:
                temp_root = temp_root.left
            temp_root.left = new_node
        
        if data > temp_root.data:
            while temp_root.right != None:
                temp_root = temp_root.right
            temp_root.right = new_node
    
    def inorder_tree(self, root):
        if root == None:
            return
        self.inorder_tree(root.left)
        print(root.data)
        self.inorder_tree(root.right)

def main():
    tree1 = Tree()
    tree1.insert_node(10)
    tree1.insert_node(5)
    tree1.insert_node(20)
    tree1.insert_node(9)
    tree1.insert_node(15)
    tree1.inorder_tree(tree1.root)
main()