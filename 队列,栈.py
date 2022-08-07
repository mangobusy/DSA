# 队列 Queue(两端开口，后进前出）
# FIFO(first in first out)
# a.enqueue(object)--在结尾添加数据
# a.dequeue()--删除并返回开头数据
# a. first()--返回开头数据
# a.len()--返回int
# a.is_empty()--判断是否为空--返回布尔值--判断方法：看fear==front
# size()--返回有几个数据：(rear-front+N)%N  (N是队列的总位子数)

class ArrayQueue():
    DEFAULT_CAPACITY=10
    def __init__(self):
        self._data=[None]*ArrayQueue.DEFAULT_CAPACITY
        self._size=0
        self._front=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def first(self):
        if self.is_empty():
            raise 'Queue is empty'
        return self._data[self._front]
    def dequeue(self):
        if self.is_empty():
            raise 'Queue is empty'
        answer=self._data[self._front]
        self._data[self._front]=None
        self._front=(self._front+1)%len(self._data)
        self._size-=1
        return answer
    def enqueue(self,e):
        if self._size==len(self._data):
            self.resize(2*len(self._data))
        avail=(self._front+self._size)%len(self._data)
        self._data[avail]=e
        self._size+=1
    def resize(self,cap):
        old=self._data
        self._data=[None]*cap
        walk=self._front
        for k in range(self._size):
            self._data[k]=old[walk]
            walk=(1+walk)%len(old)
        self._front=0
# 双端队列Deque(两端开口，两端都可以进出)
# a.add_last()
# a.add_first()
# a.delete_first()--删除并返回第一一个数据；若空，报错
# a.delete_last()--删除并返回最后一个数据；若空，报错
# a.first()--返回第一个数据；若空，报错
# a.last()--返回最后一个数据；若空，报错
# a.len()
# a.is_empty()
# back = (self._front + self._size -1) % len(self._data)
# self._front = (self._front -1) % len(self._data)
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# 栈Stack (last in first out)
# space--O(n)
# time--O(1)
# push(object)--加入一个元素
# pop()--删除一个元素
# top()--返回最后一个加入的元素
# len()
# is_empty()--返回布尔值，看是否为空
class Arraystack():
    def __init__(self):
        self.data=[]
    def push(self,a):
        return self.data.append(a)
    def len(self):
        return len(self.data)
    def is_empty(self):
        return len(self.data)==0
    def pop(self):
        if len(self.data)==0:
            raise 'stack is empty'    # raise是用来抛出异常的
        else:
            return self.data.pop()
    def top(self):
        if len(self.data)==0:
            raise 'stack is empty'
        else:
            return self.data[-1]
# a=Arraystack()
# a.push(6)
# print(a.len())
# a.pop()
# a.top()

# 括号匹对问题

def is_matched(expr):
    lefty='{[('
    righty='}])'
    s=Arraystack()
    for c in expr:
        if c in lefty:
            s.push(c)
        elif c in righty:
            if s.is_empty():
                return False
            if righty.index(c)!=lefty.index(s.pop()):
                return False
    return s.is_empty()
