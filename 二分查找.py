# 二分查找：只能有序数列查找
# 时间复杂度O(logn)
def binary_search(l,val):
    left=0
    right=len(l) -1
    mid=(left+right)//2
    while left<=right:
        if val==l[mid]:
            return mid
        elif val>l[mid]:
            left=mid+1
            mid=(left+right)//2
        else:
            right=mid-1
            mid=(left+right)//2
    else:
        return None
print(binary_search([4,5,6,7,8,9],6))
print('-'*50)

class Node():
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def search(root,key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right,key)
    if root.val > key:
        return search(root.left,key)
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left, key)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def insert2(root,key):
    if root is None:
        return Node(key)
    prev = None
    temp = root
    while temp:
        if temp.val > key:
            prev = temp
            temp = temp.left
        elif temp.val < key:
            prev = temp
            temp = temp.right
    if prev.val > key:
        prev.left = Node(key)
    else:
        prev.right = Node(key)
    return root
def inorder2(root):
    temp = root
    stack = []
    while temp or stack:
        if temp:
            stack.append(temp)
            temp = temp.left
        else:
            temp = stack.pop()
            print(temp.val)
            temp = temp.right

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current
def deleteNode(root,key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left,key)
    elif key > root.key:
        root.right = deleteNode(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right,temp.key)
    return root




# r= Node(50)
# r=insert(r,30)
# r=insert(r,20)
# r=insert(r,40)
# r=insert(r,70)
# r=insert(r,60)
# r=insert(r,80)
# r=insert(r,90)
# inorder(r)