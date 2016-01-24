__author__ = 'parvez'
import pickle


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

    def deleteNode(self,node,data):
        if node is None:
            return None
        # searching key into BST.
        if data < node.data:
            node.left = self.deleteNode(node.left, data)
        elif data > node.data:
            node.right = self.deleteNode(node.right, data)
        else: # reach to the node that need to delete from BST.
            if node.left is None and node.right is None:
                del node
            if node.left is None:
                temp = node.right
                del node
                return temp
            elif node.right is None:
                temp = node.left
                del node
                return temp
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
        file = open('tree.p', 'r')
        root = pickle.load(file)
        file.close()
        return root


def main():
    root = None
    tree = Tree()
    root = tree.insert(root, 10)
    tree.insert(root, 20)
    tree.insert(root, 30)
    tree.insert(root, 40)
    tree.insert(root, 70)
    tree.insert(root, 1)
    tree.insert(root, 80)
    tree.update(root, 70, 5)
    print("Inorder Traversal Before saving ")
    tree.Inorder(root)
    tree.save_tree(root)
    root = tree.load_tree()
    print("After loading from disk")
    tree.Inorder(root)


if __name__ == "__main__":
    main()