class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class Circular_linked_list():
    def __init__(self,li):
        self.tail = Node(None)
        fir_node = Node(li[0])
        self.tail.next = fir_node
        fir_node.next=self.tail
        self.tail = fir_node

        print('the initial circular linked list is:')
        print('{}->'.format(li[0]),end='')
        for i in li[1::]:
            newNode = Node(i)
            newNode.next = self.tail.next
            self.tail.next = newNode
            self.tail = self.tail.next
            print('{}->'.format(i),end='')
        print('')
# calculate the length of this linked list
        self.len_=1
        curr = self.tail.next.next
        while curr.next.data != None:
            self.len_+=1
            curr=curr.next
        print('the length of this linked list is {}'.format(self.len_))
        print('\n')
    def CreatF(self):
        new = input('please input a new data:')
        newNode=Node(new)
        newNode.next=self.tail.next.next
        self.tail.next.next=newNode
    def CreatR(self):
        new = input('please input a new data:')
        newNode = Node(new)
        newNode.next=self.tail.next
        self.tail.next=newNode
        self.tail=newNode
    def insert_afterSpe_ele(self):
        new = input('please input a new data:')
        newNode = Node(new)
        ele=int(input('which element do you want to insert after:'))
        curr=self.tail
        while curr.data!=ele:
            curr=curr.next
        else:
            newNode.next=curr.next
            curr.next=newNode
    def insert_spe_index(self):
        new = input('please input a new data:')
        newNode = Node(new)
        index_ = int(input('where do you want to insert:'))
        j=-1
        curr=self.tail
        while j<index_:
            j+=1
            curr=curr.next
        else:
            newNode.next = curr.next
            curr.next = newNode
    def del_spe_ele(self):
        ele = int(input('which element do you want to delete:'))
        curr = self.tail
        while curr.next.data!=ele:
            curr=curr.next
        else:
            curr.next=curr.next.next
    def del_index(self):
        index_ = int(input('the index of the element that you want to delete:'))
        if index_>self.len_-1:
            print('!!!!!!!the index is out of range!!!!!!!')
        else:
            j=-1
            curr = self.tail
            while j<index_:
                j+=1
                curr=curr.next
            else:
                curr.next=curr.next.next
    def locate_spe_ele(self):
        ele = int(input('which element do you want to seach:'))
        curr = self.tail
        j=-2
        while curr.data!=ele:
            curr=curr.next
            j+=1
        else:
            return 'the index of this element is {}'.format(j)
    def get_spePosition_ele(self):
        index_ = int(input('the index of the element that you want to search:'))
        if index_>self.len_-1:
            print('!!!!!!!the index is out of range!!!!!!!')
        else:
            j = -2
            curr = self.tail
            while j != index_:
                j += 1
                curr = curr.next
            else:
                return 'the element is {}'.format(curr.data)


    def Reverse(self):
        curr=self.tail.next.next
        li=[]
        while curr.data!=None:
            li.append(curr.data)
            curr=curr.next
        tail = Node(None)
        fir_node = Node(li[-1])
        tail.next = fir_node
        fir_node.next = tail
        tail = fir_node
        print('the current circular linked list is:')
        print('{}->'.format(li[-1]), end='')
        for i in li[len(li)-2::-1]:
            newNode=Node(i)
            newNode.next=tail.next
            tail.next=newNode
            tail=tail.next
            print('{}->'.format(i), end='')
        print('')

    def Remove_duplicate_ele(self):
        curr = self.tail.next.next
        while curr.next.data!=None:
            if curr.data!=curr.next.data:
                curr=curr.next
            elif curr.data==curr.next.data:
                curr.next = curr.next.next
        else:
            return ''

    def Traverse(self):
        curr=self.tail.next.next
        print('the current linked list is :')
        while curr.next.data!=None:
            print("{}->".format(curr.data),end='')
            curr=curr.next
        print('{}->'.format(curr.data))
        print('Traverse is over')

# 1 test.CreatF()
# 2 test.CreatR()
# 3 test.insert_afterSpe_ele()
# 4 test.insert_spe_index()
# 5 test.del_spe_ele()
# 6 test.del_index()
# 7 print(test.locate_spe_ele())
# 8 print(test.get_spePosition_ele())
# 9 test.Reverse()
# 10 test.Traverse()
# 11 print(test.Remove_duplicate_ele())

if __name__=='__main__':
    test = Circular_linked_list([1, 2, 3, 4, 5, 5, 6, 7, 8])
    choose_num=int(input('please input the number of the function you want to choose:'))
    if choose_num==1:
        print('--------you choose: insert new node at head of the list---------')
        test.CreatF()
        test.Traverse()
    if choose_num == 2:
        print('--------you choose: insert new node at tail of the list--------')
        test.CreatR()
        test.Traverse()
    if choose_num == 3:
        print('--------you choose: insert new node after a specified node--------')
        test.insert_afterSpe_ele()
        test.Traverse()
    if choose_num == 4:
        print('--------you choose: insert new node at a specified index in the list--------')
        test.insert_spe_index()
        test.Traverse()
    if choose_num == 5:
        print('--------you choose: delete a specified element--------')
        test.del_spe_ele()
        test.Traverse()
    if choose_num == 6:
        print('--------you choose: delete an element from a specified position--------')
        test.del_index()
        test.Traverse()
    if choose_num == 7:
        print('--------you choose: search a specified element and return its index--------' )
        print(test.locate_spe_ele())
        test.Traverse()
    if choose_num == 8:
        print('--------you choose: find and return the element at specified position--------')
        print(test.get_spePosition_ele())
        test.Traverse()
    if choose_num == 9:
        print('--------you choose: Reverse--------')
        test.Reverse()
    if choose_num == 10:
        print('--------you choose: Traverse--------')
        test.Traverse()
    if choose_num == 11:
        print('--------you choose: Remove duplicate elements--------')
        print(test.Remove_duplicate_ele())
        test.Traverse()



