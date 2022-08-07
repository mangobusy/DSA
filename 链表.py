# 链表： 是一组数据项的集合，其中每个数据项都是一个节点的一部分，每个节点还包括指向下一个节点的链接
# 链表的结构: +-----+------+
#            data | next |
#           +-----+------+
#  data为自定义数据，next为下一个节点的地址
# 基本元素：1、节点: 每个节点有两个部分，左边称为值域，存放用户数据；右边部分成为指针域，用来存放指向下一个元素的指针
#         2、head: head节点永远指向第一个节点
#         3、tail: tail永远指向最后一个节点
#         4、None: 链表中最后一个节点的指针域为None值
# 线性表的链式储存结构：线性表中的数据元素（结点）在存储器中的位置是任意的，即逻辑上相邻的数据元素在物理位置上不一定相邻
# 当进行插入和删除操作时，\\链表操作的时间复杂度仅为O(1),空间复杂度为O(n)\\

# 单链表--从 头指针 开始
class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        while (temp):
            print(temp.data)
            temp=temp.next

llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
llist.head.next = second  # 把第一个节点与第二个节点链接起来
second.next = third
# +-----+------+      +-----+------+      +-----+------+
# |  1  |   o-------->|  2  |   o-------->|  3  | null |
# +-----+------+      +-----+------+      +-----+------+

class LinkedList_1():
    def add_first(self,L, e):  # 在开头新插入一个Node
        newest = Node(e)      # 创造一个新Node
        newest.next = L.head    # 将新Node的指针指向原本的第一个Node
        L.head = newest    # 将head指向新Node
        L.size = L.size + 1
    def remove_first(self,L):  # 删除开头的一个Node
        if L.head==None:
            raise "the list is empty"
        L.head=L.head.next   # 将head指向（要删除的）下一个Node
        L.size=L.size-1
    def add_last(self,L,e):
        newest = Node(e)
        newest.next=None
        L.tail.next=newest
        L.tail=newest
        L.size=L.size+1
    # remove_tail is not efficient: we need to know the element before the end, which is not easy

# 链表栈--linked-list stack
# 空间复杂度O(n)
class LinkedStack():
    class _Node():  # 嵌套类
        __slots__='_element','_next'   # 定义一个特殊的__slots__变量，来限制该class实例所能添加的属性
        def __init__(self,element,next):
            self._element=element
            self._next=next
    def __init__(self):
        self._head=None
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def push(self,e):   # add element to the top of the stack
        self._head=self._Node(e,self._head)
        self._size+=1
    def top(self):  # return the top element of the stack
        if self.is_empty():
            raise ('Stack is empty')
        return self._head._element
    def pop(self):  # remove and return the element from the top of the stack
        if self.is_empty():     # The top element is stored at the first node of the list
            raise ('Stack is empty')
        answer=self._head._element
        self._head=self._head._next
        self._size-=1
        return answer

# 链表队列Linked-List Queue
# 空间复杂度O(n), 时间复杂度O(1)
class LinkedQueue:
    class _Node():  # 嵌套类
        __slots__='_element','_next'   # 定义一个特殊的__slots__变量，来限制该class实例所能添加的属性
        def __init__(self,element,next):
            self._element=element
            self._next=next
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def first(self):  # return the element at the front of the queue
        if self.is_empty():
            raise ('Queue is empty')
        return self._head._element
    def dequeue(self):   # remove and return the first element of the queue
        if self.is_empty():
            raise ('Queue is empty')
        answer=self._head
        self._head=self._head._next
        self._size-=1
        if self.is_empty():
            self._tail=None
        return answer
    def enqueuue(self,e):  # add an element to the back of queue
        newest=self._Node(e,None)
        if self.is_empty():
            self._head=newest
        else:
            self._tail._next=newest
            self._tail=newest
            self._size+=1
# ================================================================================
# 双向链表doubly linked list
# 空间复杂度O(n), 时间复杂度O(1)
class _DoublyLinkedBase():
    class _Node():
        __slots__ = '_element', '_prev', '_next'
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
    def __init__(self):
        self._header=self._Node(None,None,None)
        self._trailer=self._Node(None,None,None)
        self._header._next=self._trailer
        self._trailer._prev=self._header
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def _insert_between(self,e,predecessor,successor):
        newest=self._Node(e,predecessor,successor)
        predecessor._next=newest
        successor._prev=newest
        self._size+=1
        return newest
    def _delete_node(self,node):
        predecessor=node._prev
        successor=node._next
        predecessor._next=successor
        successor._prev=predecessor
        self._size-=1
        answer=node._element
        node._prev=node._next=node._element=None
        return answer

# 双向链表双端队列(implement deque with a doubly linked list)
class LinkedDeque(_DoublyLinkedBase):
    def first(self):  # return the element at the front of the deque
        if self.is_empty():
            raise ('Deque is empty')
        return self._header._next._element
    def last(self):
        if self.is_empty():
            raise ('Deque is empty')
        return self._trailer._prev._element
    def insert_first(self,e):
        self._insert_between(e,self._header,self._header._next)
    def insert_last(self,e):
        self._insert_between(e,self._trailer._prev,self._trailer)
    def delete_first(self):
        if self.is_empty():
            raise ('Deque is empty')
        return self._delete_node(self._header._next)
    def delete_last(self):
        if self.is_empty():
            raise ('Deque is empty')
        return self._delete_node(self._trailer._prev)

# 位置列表(基于双向链表)
class PositionalList(_DoublyLinkedBase):
    class Position():   # 嵌套position类
        def __init__(self,container,node):
            self._container=container
            self._node=node
        def element(self):
            return self._node._element
        def __eq__(self, other):    # return True if other is a position representing the same location
            return type(other) is type(self) and other._node is self._node
        def __ne__(self, other):   # return True if other dose not represent the same location
            return not(self==other)
    def _validate(self,p):#------ utility method------------------------------
        if not isinstance(p,self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise TypeError('p dose not belong to this container')
        if p._node._next is None:
            raise TypeError('p is no longer valid')
        return p._node
    def _make_position(self,node):  # utility method
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self,node)
    def first(self):#-----accessors-------------------------------------
        return self._make_position(self._header._next)
    def last(self):
        return self._make_position(self._trailer._prev)
    def before(self,p):
        node=self._validate(p)
        return self._make_position(node._prev)
    def after(self,p):
        node=self._validate(p)
        return self._make_position(node._next)
    def __iter__(self):
        cursor=self.first()
        while cursor is not None:
            yield cursor.element()
            cursor=self.after(cursor)
    def _insert_between(self,e,predecessor,successor):#---mutators-----------
        node=super()._insert_between(e,predecessor,successor)
        return self._make_position(node)
    def add_first(self,e):
        return self._insert_between(e,self._header,self._header._next)
    def add_last(self,e):
        return self._insert_between(e, self.trailer._prev, self.trailer)
    def add_before(self,p,e):
        original=self._validate(p)
        return self._insert_between(e, original._prev, original)
    def add_after(self,p,e):
        original=self._validate(p)
        return self._insert_between(e, original, original._next)
    def delete(self,p):
        original=self._validate(p)
        return self._delete_node(original)
    def replace(self,p,e):
        original=self._validate(p)
        old_value=original._element
        original._element=e
        return old_value
