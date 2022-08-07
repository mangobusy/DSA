# Tree树
# Root根: node without parent
# Internal node内节点: node with at least one child
# Siblings: Child nodes at the same depth
# External node外节点: node without children

class Position():
    def __init__(self, container, node):
        self._container = container
        self._node = node

    def element(self):
        return self._node._element

    def __eq__(self, other):  # return True if other is a position representing the same location
        return type(other) is type(self) and other._node is self._node

    def __ne__(self, other):  # return True if other dose not represent the same location
        return not (self == other)

class Tree():
    class Position():   # 嵌套position类
        def element(self):    # return the element stored at this position
            raise NotImplementedError('must be implemented by subclass')
        def __eq__(self, other):
            raise  NotImplementedError('must be implemented by subclass')
        def __ne__(self, other):
            return not(self==other)
    def root(self):   # return position representing the tree's root (or None if empty)
        raise NotImplementedError('must be implemented by subclass')
    def parent(self,p):   # return position representing p's parent (or None if empty)
        raise NotImplementedError('must be implemented by subclass')
    def num_children(self,p):   # return the number of children that Position p has
        raise NotImplementedError('must be implemented by subclass')
    def childred(self,p):    # Generate an iteration of Positions representing p's children
        raise NotImplementedError('must be implemented by subclass')
    def __len__(self):    # return the total number of elements in the tree
        raise NotImplementedError('must be implemented by subclass')
    def is_root(self,p):
        return self.root()==p
    def is_leaf(self,p):
        return self.num_children(p)==0
    def is_empty(self):
        return len(self)==0

# preorder traversal先序遍历: 按照根->左->右的顺序沿一定路径经过路径上所有节点。在二叉树中，先根后左再右
class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
    def PreorderTraversal(self,root):
        res=[]
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

# Postorder Traversal后序遍历: 按照左->右->根的顺序遍历
#            A
#          /   \
#         B     C
#        / \   /
#       D   E  F      # 遍历顺序： DEBFCA
class Postorder_Traversal(Node):
    def postordertraversal(self,root):
        res = []
        if root:
            res = self.postordertraversal(root.left)
            res = res + self.postordertraversal(root.right)
            res.append(root.data)
        return res
# root=Postorder_Traversal(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)
# print(root.PostorderTraversal(root))

# Breadth-first Traversal宽度优先遍历: 以离初状态的状态距离为顺序进行遍历
#            A
#          /   \
#         B     C
#        / \   /
#       D   E  F      # 遍历顺序： ABCDEF
class Node_3():
    def __init__(self,val:int):
        self.left = None
        self.right = None
        self.val = val
    def __repr__(self):  # 调用该方法将对象转化为字符串，再将字符串连接在一起
        return str(self.val)
    def insert_node(self,val):
        if self.val is not None:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert_node(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert_node(val)
    @staticmethod
    def insert_nodes(vals:list,root):
        for i in vals:
            root.insert_node(i)
    def bfs(self,root = None):
        if root is None:
            return
        queue=[root]
        while len(queue) > 0:
            cur_node = queue.pop(0)
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)
            print(queue)
# def run():
#     root = Node_3(4)
#     root.insert_nodes([2,1,3,6,5,7],root)
#     root.bfs(root = root)
# if __name__ == '__main__':
#     run()

# Binary Tree二叉树===================================================================
# n : number of nodes
# e : number of external nodes
# i : number of internal nodes
# h : height
# 一些性质: e = i + 1 \\ n = 2e - 1 \\ h <= i \\ h <= (n - 1)/2 \\ e <= 2h
class BinaryTree(Tree):
    def left(self,p):   # 返回p的左子节点
        raise NotImplementedError('must be implemented by subclass')
    def right(self,p):
        raise NotImplementedError('must be implemented by subclass')
    def sibling(self,p):
        parent=self.parent(p)
        if parent is None:
            return None
        else:
            if p==self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    def children(self,p):
        if self.left(p) is not None:
            yield self.left(p)   # yield相当于return，但是会记住本次结束执行的位置，下次迭代就从这个位置后开始
        if self.right(p) is not None:
            yield self.right(p)

# Inorder traversal中序遍历 : 左->根->右
class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
    def Inorder_Traversal(self,root):
        res = []
        if root:
            res = self.Inorder_Traversal(root.left)
            res.append(root.data)
            res = res + self.Inorder_Traversal(root.right)
        return res

# root = Node(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)
# print(root.Inorder_Traversal(root))

# 中序遍历完成算数运算
class Node1():
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value
def evaluateExpressionTree(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return int(root.data)
    left_sum = evaluateExpressionTree(root.left)
    right_sum = evaluateExpressionTree(root.roght)
    if root.data == '+':
        return left_sum + right_sum
    if root.data == '-':
        return left_sum - right_sum
    if root.data == '*':
        return left_sum * right_sum
    else:
        return left_sum // right_sum

# Euler Tour Traversal欧拉遍历
class Node2():
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
def eulerTree(root,euler):
    euler.append(root.data)
    if root.left:
        euler = eulerTree(root.left,euler)
        euler.append(root.data)
    if root.right:
        euler = eulerTree(root.right,euler)
        euler.append(root.data)
    return euler
def printEulerTour(root):
    euler = []
    euler = eulerTree(root,euler)
    for i in range(len(euler)):
        print(euler[i],end=' ')