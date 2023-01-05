# 打开abc1_in文件，将数据加载到列表中
f = open('abc1_in')
func1 = f.readlines()
li1 = []
for i in func1:
    a=i.split()
    b=[]
    for j in a:
        j=int(j)
        b.append(j)
    li1.append(b)
print(li1)

# 打开abc2_in文件，将数据加载到列表中
f = open('abc2_in')
func1 = f.readlines()
li2 = []
for i in func1:
    a=i.split()
    b=[]
    for j in a:
        j=int(j)
        b.append(j)
    li2.append(b)
print(li2)

# 计算乘法时列表的长度
maxlen=li1[-1][1]+li2[-1][1]+1

class Node():
    def __init__(self,li):
        self.data=li
        self.next=None

class Polynomial():
    def __init__(self):
        self.head=Node([])
        self.head.next=None
        self.curr=self.head
    def polynomial(self,li):
        for i in li:
            new=Node(i)
            self.curr.next=new
            self.curr = self.curr.next
    def traversal(self):
        curr=self.head.next
        while curr:
            print(curr.data)
            curr=curr.next

    def po_add(self):
        # new=Polynomial()
        # new.polynomial([])
        test1.curr = test1.head.next
        test2.curr = test2.head.next
        # print(test1.curr.data)
        # print(test2.curr.data)
        while test1.curr and test2.curr:
            if test1.curr.data[1] == test2.curr.data[1]:
                test3.curr.next.data = [test1.curr.data[0] + test2.curr.data[0], test1.curr.data[1]]
                # new.curr=new.curr.next
                test1.curr = test1.curr.next
                test2.curr = test2.curr.next
                test3.curr = test3.curr.next
            elif test1.curr.data[1] > test2.curr.data[1]:
                test3.curr.next = test2.curr
                test2.curr = test2.curr.next
                test3.curr = test3.curr.next
            elif test1.curr.data[1] < test2.curr.data[1]:
                p = test1.curr.next
                test3.curr.next = test1.curr
                test1.curr = p
                test3.curr = test3.curr.next
        curr = test3.head.next

        with open("addre_out", "w") as f:
            while curr:
                for i in curr.data:
                    f.write(str(i)+' ')
                f.write('\n')
                curr = curr.next

    def po_multiply(self):
        li = []
        for i in range(maxlen):
            li.append(0)
        test11.curr = test11.head.next

        while test11.curr:
            # print('test11:----------------------------')
            # print(test11.curr.data)
            test22.curr = test22.head.next
            while test22.curr:
                # print(test22.curr.data)
                li[test11.curr.data[1] + test22.curr.data[1]] += (test11.curr.data[0] * test22.curr.data[0])
                # print(li[test11.curr.data[1] + test22.curr.data[1]])
                test22.curr = test22.curr.next
            test11.curr = test11.curr.next
        print(li)

        with open('addmul_out','w') as f:
            j = 0
            for i in li:
                if i!=0:
                    f.write(str(i)+' '+str(j)+'\n')
                j+=1

test1=Polynomial()
test2=Polynomial()
test3=Polynomial()

test1.polynomial(li1)
test2.polynomial(li2)
test1.po_add()

test11=Polynomial()
test22=Polynomial()
test11.polynomial(li1)
test22.polynomial(li2)
test11.po_multiply()


