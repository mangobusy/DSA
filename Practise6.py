class Node():
    def __init__(self,ele,li):
        self.ele = ele
        self.right = None
        self.left = None
        self.li = li
        self.h = 1

    def form_link(self,num):   # construct the lined representation
        if (2*num+2)<len(self.li):
            if self.li[2*num+1]!='#':
                self.left = Node(self.li[2*num+1],li)
                self.left.form_link(2 * num + 1)
            else:
                self.left = None

            if self.li[2*num+2]!='#':
                self.right = Node(self.li[2*num+2],li)
                self.right.form_link(2 * num + 2)
            else:
                self.right = None

    def set_node_height(self,h,dict):   # set the height of each node
        dict.update({self.ele:self.h})   # put node and height to the dict
        h+=1
        if self.left:
            self.left.h+=h
            self.left.set_node_height(h,dict)
        if self.right:
            self.right.h+=h
            self.right.set_node_height(h,dict)
    def tree_height(self):
        h = 1
        for i in dict.values():   # the maximum of node_height is the height of tree
            h = max(h,i)
        print('the height of the binary tree is {}'.format(h))
    def node_on_same_height(self,k):
        count = 0
        node_li = []
        for i,j in dict.items():
            if j==k:
                count+=1
                node_li.append(i)
        print('there are {} nodes on level k, they are {}'.format(count,node_li))

li = ['A','B','C','D','E','#','F','#','#','G','H','#','#','I','#','#','#','#','#','#']
test = Node(li[0],li)
test.form_link(0)
h=0
dict={}
test.set_node_height(h,dict)
test.tree_height()
k = int(input('please input the level k:'))
test.node_on_same_height(k)


