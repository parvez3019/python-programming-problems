__author__ = 'parvez'
import pickle
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def createNode(self, data):
        return Node(data)

    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)

        return node

    def search(self, node, data):
        if node is None or node.data == data:
            return node

        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)

    def minValue(self, node):
        minv = node.data
        while node.left is not None:
            minv = node.left.data
            node = node.left
        return minv

    def deleteNode(self, node, data):
        if node is None:
            return None
        # searching key into BST.
        if data < node.data:
            node.left = self.deleteNode(node.left, data)
        elif data > node.data:
            node.right = self.deleteNode(node.right, data)
        elif data == node.data:
        # reach to the node that need to delete from BST.
        #     print("node reached")
            if node.left is None and node.right is None:
                del node
                return None
            elif node.left is None:
                temp = node.right
                node.data = temp.data
                del temp
                return node
            elif node.right is None:
                temp = node.left
                node.data = temp.data
                del temp
                return node
            # Smallest value of right subtree

            else :
                node.data = self.minValue(node.right)
                #deletion
                node.right = self.deleteNode(node.right, node.data)

        return node

    def update(self, node, data, updatedata):
        self.deleteNode(node, data)
        self.insert(node, updatedata)

    def Inorder(self, root):
        if root is not None:
            self.Inorder(root.left)
            print root.data
            self.Inorder(root.right)

    def save_tree(self, root):
        # Using pickle Library
        try:
            file = open('tree.p', 'w')
            pickle.dump(root, file)
        except:
            print("Exception while Dumping tree")
        file.close()

    def load_tree(self):
        try:
            file = open('tree.p', 'r')
            root = pickle.load(file)
        except:
            print("Error opening file.")
        file.close()
        return root


def main():
    root = None
    tree = Tree()
    choice = -1
    print("Choose any operation to perform:")

    while choice is not 7:
        print("1.To Insert a node.")
        print("2.To Delete a node.")
        print("3.To update a node.")
        print("4.To Inorder Tree Traversal.")
        print("5.To save tree to disk.")
        print("6.To load tree from disk.")
        print("7.To Exit.")
        choice = input("Your Choice:")
        if choice is 1:
            if root is None:
                data = input("Enter data to insert: ")
                root = tree.insert(root, data)
            else:
                data = input("Enter data to insert: ")
                tree.insert(root, data)
        elif choice is 2:
            if root is None:
                print("Tree is empty")
            else:
                data = input("Enter node to delete: ")
                tree.deleteNode(root, data)
        elif choice is 3:
            if root is None:
                print("Tree is empty")
            else:
                data = input("Enter data need to be updated : ")
                updated_data = input("Enter new data value : ")
                tree.update(root,data,updated_data)
        elif choice is 4:
            if root is None:
                print("Tree is empty")
            else:
                print("Inorder Traversal Before saving ")
                tree.Inorder(root)
        elif choice is 5:
            if root is None:
                print("Tree is empty")
            else:
                tree.save_tree(root)
        elif choice is 6:
            root = tree.load_tree()
        elif choice is 7:
            sys.exit()

    print("Bye")


if __name__ == "__main__":
    main()