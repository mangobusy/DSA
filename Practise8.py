from collections import deque

class VertexNode():
    def __init__(self,data):
        self.data = data
        self.adj = None
class EdgeNode():
    def __init__(self, data):
        self.data = data
        self.link = None
class Graph():
    def __init__(self,e,v,lines):
        self.eNum = e
        self.vNum = v
        self.lines = lines
    def adjacencyMatrix(self):
        matrix = []
        for i in range(self.vNum):
            li = []
            for j in range(self.vNum):
                li.append(float('inf'))
            matrix.append(li)
        for col in range(self.vNum):
            for vol in range(self.vNum):
                if col == vol:
                    matrix[col][vol] = 0
        for j in self.lines:
            matrix[j[0]][j[1]] = 1
        print(matrix)

    def adjacencyLists(self):
        li = []
        for i in range(self.vNum):
            newNode = VertexNode(i)
            li.append(newNode)
        for line in self.lines:
            newNode2 = EdgeNode(line[1])
            if li[line[0]].adj == None:
                li[line[0]].adj = newNode2
            else:
                w = li[line[0]].adj
                while True:
                    if w.link == None:
                        w.link = newNode2
                        break
                    else:
                        w = w.link
        for i in li:
            print(i.data,'->',end='')
            w = i.adj
            while True:
                if w:
                    print(w.data,'->',end='')
                    w = w.link
                else:
                    break
            print('')
        return li

    def DFSTraverse(self,vertex_li,vertex):
        visited = [0]*self.vNum
        li = self.DFS(visited,vertex_li,vertex,[])
        return li
    def DFS(self, visited,vertex_li,vertex,li):
        visited[vertex] = 1
        li = self.VisitVertex(vertex,li)
        w = self.GetFirstAdjacentVertex(vertex_li,vertex)
        while w is not None:
            if visited[w] == 0:
                self.DFS(visited, vertex_li, w,li)
            w = self.GetNextAdjacentVertex(visited, vertex_li, vertex, w)
        return li


    def BFS(self,vertex_li,v):
        visited = [0] * self.vNum
        qu = deque()
        li = self.VisitVertex(v,[])
        visited[v]=1
        qu.append(v)
        while len(qu)>0:
            v = qu.popleft()
            w = self.GetFirstAdjacentVertex(vertex_li,v)
            while w is not None:
                if visited[w]==0:
                    li = self.VisitVertex(w,li)
                    visited[w]=1
                    qu.append(w)
                w = self.GetNextAdjacentVertex(visited,vertex_li,v,w)
        return li

    def VisitVertex(self,vertex,li):                 # stroe the vertex into a list
        # print(vertex,'',end='')
        li.append(vertex)
        return li
    def  GetFirstAdjacentVertex(self,vertex_li,vertex):
        return vertex_li[vertex].data
    def GetNextAdjacentVertex(self, visited, vertex_li, vertex, w):
        w = vertex_li[vertex].adj
        while w:
            if visited[w.data]==0:
                return w.data
            else:
                w = w.link

    def BFSA(self,vertex_li):
        visited = [0]*self.vNum
        li2 = []
        for i in range(self.vNum):
            if visited[i]==0:
                li = self.BFS(vertex_li,vertex_li[i].data)
                li2.append(li)       # add each traversal as a sub_list into li2
        for i in li2:
            i.sort()
        list1 = [list(j)for j in set(tuple(i)for i in li2)]   # delet the repeated sub_list
        print('{} connected component'.format(len(list1)))    # the len(li2) is the number of connected component
        dict1 = {}
        for i in range(len(list1)):
            dict1[i] = len(list1[i])

        while list1:
            min_len = 100
            for i in dict1.values():
                min_len = min(i,min_len)   # find the min connected component
            for i,j in dict1.items():
                if j==min_len:
                    print(list1[i])
                    for n in list1[i]:
                        for m in list1:
                            if n in m:
                                m.remove(n)
                    list1.pop(i)
                    del dict1[i]
                    break

if __name__=='__main__':
    # Fig1
    lines1 = [[0, 5], [0, 1], [1, 2], [1, 4], [2, 3], [3, 1], [3, 0], [4, 3], [5, 4]]
    eNum1 = 9
    vNum1 = 6

    # Fig2
    lines2 = [[0, 1], [0, 4], [1, 2], [2, 0], [2, 3], [3, 0], [3, 5], [5, 4]]
    eNum2 = 8
    vNum2 = 6

    example_num = int(input('please input the example number'))
    if example_num==1:
        test = Graph(eNum1, vNum1, lines1)
    if example_num==2:
        test = Graph(eNum2, vNum2, lines2)
    num = int(input('please input the function number: '))
    while num != 0:   # when user input 0, exit the program
        global vertex_li

        if num == 1:
            test.adjacencyMatrix()
        if num == 2:
            vertex_li = test.adjacencyLists()
        if num == 3:
            li = test.DFSTraverse(vertex_li, vertex_li[0].data)
            for i in li:
                print(i, end='')
            print('')
        if num == 4:
            li = test.BFS(vertex_li,vertex_li[0].data)
            for i in li:
                print(i,end='')
            print('')
        if num == 5:
            test.BFSA(vertex_li)
        num = int(input('please input the function number: '))













