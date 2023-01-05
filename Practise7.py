import heapq

class HuffmanCode():
    def __init__(self,data,weight):
        self.val = data
        self.parent = None
        self.left = None
        self.right = None
        self.weight = weight
        self.flag = True
class Huffman():
    def __init__(self,fre):
        self.fre0 = []
        self.fre1 = []
        for i in fre:
            self.fre0.append(i)
        for i in fre:
            self.fre1.append(i)
        self.fre0.sort()

    def initialization(self,chara,fre):
        rn = None
        heap = []
        a = [None] * (2*len(fre)-1)
        for i in range(len(fre)):
            heapq.heappush(heap, [fre[i], i])
            a[i] = HuffmanCode(chara[i], fre[i])    # new a Huffmancode with self.val=letter, self.weight=frequency

        for i in range(len(fre),2*len(fre)-1):
            p1 = heapq.heappop(heap)
            p2 = heapq.heappop(heap)
            r = p1[0] + p2[0]
            a[i] = HuffmanCode('Null',r)
            a[p1[1]].parent = a[p2[1]].parent = a[i]
            a[i].left,a[i].right = a[p1[1]],a[p2[1]]
            a[p1[1]].flag, a[p2[1]].flag = True, False
            heapq.heappush(heap, [a[i].weight,i])
        return a[-1]

    def Encoding(self,root,chara):
        def encode(root,i,code):
            if root:
                if root.val == i: # if match the letter, store its code
                    with open("CodeFile", "a") as f:
                        # print(code,end='')
                        # f.write(i+': '+code+'\n')
                        f.write(code)
                if root.val!=i:
                    encode(root.left,i,code+'0')  # if the letter is in the left tree, code add 0
                    encode(root.right,i,code+'1')  # if the letter is in the right tree, code add 1

        for i in chara:
            encode(root,i,'')


    def Decoding(self,root,codeli):
        r = root
        def decode(root,codeli,r):
            if root and codeli!=[]:
                if root.val!='Null':  # if self.val==letter, store the letter in the file
                    # print(root.val,end='')
                    with open('TextFile','a') as f:
                        f.write(root.val)
                    root = r
                if root.val=='Null':
                    if codeli[0]=='0':  # if code number=0, find it in left tree
                        decode(root.left,codeli[1::],r)
                    if codeli[0]=='1':  # if code number=1, find it in right tree
                        decode(root.right,codeli[1::],r)
        decode(root,codeli,r)

    def Print(self):
        with open("CodeFile", 'r') as f:
            code = f.read()
            code_li = []
            for i in code:
                code_li.append(i)
            a = len(code_li)//50
            j = 0
            print('the code of sentence "THIS PROGRAM IS MY FAVORITE" is :')
            while j<=a:
                for i in code_li[j*50:(j+1)*50:]:   # print 50 number each line
                    print(i,end='')
                print('')
                j+=1
        print('')
    def TreePrint(self,root):    # preorder traversal to print the tree out
        deque_li = []
        deque_li.append(root)
        while len(deque_li)>0:
            p = deque_li[0]
            with open('TreePrint','a') as f:
                f.write(p.val)
                f.write('\n')
            print(p.val,p.weight)
            del deque_li[0]
            if p.left!=None:
                deque_li.append(p.left)
            if p.right!=None:
                deque_li.append(p.right)

if __name__=='__main__':
    chara = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    fre = [64,13,22,32,103,21,15,47,57,1,5,32,20,57,63,15,1,48,51,80,23,8,18,1,16,1]

    testWord='THIS PROGRAM IS MY FAVORITE'
    testli = []
    for i in testWord:
        testli.append(i)
    test = Huffman(fre)
    while True:
        choose = input('please select function: ')
        a = test.initialization(chara,fre)
        if choose == 'E':
            print('Encoding: Finish encoding')
            test.Encoding(a,testli)
        if choose == 'D':
            print('Decoding: Finish decoding')
            with open('CodeFile', 'r') as f:
                code = f.read()
            li = []
            for i in code:
                li.append(i)
            test.Decoding(a,li)
        if choose == 'P':
            print('Print: ')
            test.Print()
        if choose == 'T':
            print('TreePrint: ')
            test.TreePrint(a)

