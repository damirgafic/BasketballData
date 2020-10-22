'''
Things to be done:
-scrape all salaries and PER stats

'''


class newNode:

    # Constructor to create a new node
    def __init__(self, data, name):
        self.key = data
        self.name = name
        self.count = 1
        self.left = None
        self.right = None


# A utility function to do inorder
# traversal of BST
def inorder(root):
    if root != None:
        inorder(root.left)
        print(str(root.key) + ' ' + root.name + ' ' + str(root.count))
        inorder(root.right)

    # A utility function to insert a new node


# with given key in BST
def insert(node, key, name):
    # If the tree is empty, return a new node
    if node == None:
        k = newNode(key, name)
        return k

        # If key already exists in BST, increment
    # count and return
    if key == node.key:
        root.count += 1
        node.left = insert(node.left, key, name)

        # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key, name)
    else:
        node.right = insert(node.right, key, name)

        # return the (unchanged) node pointer
    return node


# Given a non-empty binary search tree, return
# the node with minimum key value found in that
# tree. Note that the entire tree does not need
# to be searched.
def minValueNode(node):
    current = node

    # loop down to find the leftmost leaf
    while current.left != None:
        current = current.left

    return current


# Given a binary search tree and a key,
# this function deletes a given key and
# returns root of modified tree
def deleteNode(root, key):
    # base case
    if root == None:
        return root

        # If the key to be deleted is smaller than the
    # root's key, then it lies in left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)

        # If the key to be deleted is greater than
    # the root's key, then it lies in right subtree
    elif key > root.key:
        root.right = deleteNode(root.right, key)

        # if key is same as root's key
    else:

        # If key is present more than once,
        # simply decrement count and return
        if root.count > 1:
            root.count -= 1
            return root

            # ElSE, delete the node node with
        # only one child or no child
        if root.left == None:
            temp = root.right
            return temp
        elif root.right == None:
            temp = root.left
            return temp

            # node with two children: Get the inorder
        # successor (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's content
        # to this node
        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)
    return root


# Driver Code
if __name__ == '__main__':
    # Let us create following BST
    # 12(3)
    # / \
    # 10(2) 20(1)
    # / \
    # 9(1) 11(1)
    root = None

    root = insert(root, 15, 'gg5')
    root = insert(root, 1, 'gg4')
    root = insert(root, 12, 'gg3')
    root = insert(root, 150, 'gg2')
    root = insert(root, 50, 'gg1')
    root = insert(root, 12, 'gg56')


    print("Inorder traversal of the given tree")
    inorder(root)
    print()

