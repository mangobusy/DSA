# [列表查找--可以用index()]
# 顺序查找（线性查找）：从列表第一个元素开始，顺序进行搜索，直到找到或到列表最后一个元素为止
def linear_search(l,val):
    for ind,n in enumerate(l):
        if n==val:
            return ind
    else:
        return None
print(linear_search([1,2,3,4,5],4))
print('-'*50)
# 二分查找：只能有序数列查找
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
# 用迭代
def binary_search(data,target,low,high):
    if low>high:
        return False
    else:
        mid=(low+high)//2
        if target==data[mid]:
            return True
        elif target<data[mid]:
            return binary_search(data,target,low,mid-1)
        else:
            return binary_search(data,target,mid+1,high)
# ***************************************************************
# ---------------------------------------------------------------
# 常见排序算法：
# lowB三人组：冒泡排序、选择排序、插入排序---O(n**2)
# NB三人组：快速排序、堆排序、归并排序   ---O(nlogn)---运行时间：快速排序<归并排序<堆排序
# 其他排序：希尔排序、计数排序、基数排序
# -------------------------------------------------
# 冒泡排序  O(n**2)
def bubble_sort(l):
    for i in range(len(l)-1):   # 每一趟
        for j in range(len(l)-i-1):    # 每一趟指针的挪动
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]   # 交换顺序
    return (l)
print(bubble_sort([5,2,7,4,8,9,3]))
# -------------------------------------------------
# 选择排序:先找到最小的数，放在最前面。。。。
def select_sort_simple(l2):    # 不推荐
    l_new=[]
    for i in range(len(l2)):
        min_val=min(l2)
        l_new.append(min_val)
        l2.remove(min_val)
    return l_new
print('-'*50)
def select_sort(l):
    for i in range(len(l)-1):  # 这里减一还是不减一都可以，只不过减一就多重复一次
        min_location=i
        for j in range (i,len(l)):
            if l[j]<l[min_location]:
                min_location=j
        l[i],l[min_location]=l[min_location],l[i]
    return l
print(select_sort([9,5,3,7,4,8,6,1]))
print('-'*50)
# ---------------------------------------------------
# 插入排序
def insert_sort(l):
    for i in range(1,len(l)):  # i表示下一个数
        tem=l[i]     # 把l[i]存在一个变量中
        j=i-1    # j表示最新的已排好序的数
        while j>=0 and l[j]>tem:
            l[j+1]=l[j]
            j-=1
        l[j+1]=tem    # 这里是j+1不是j
    return l
print(insert_sort([3,5,8,2,7,1,9,4]))
print('*'*50)
# --------------------------------------------------
# 快速排序  O( n*log(n) )
# 取一个元素P(第一个元素),使P归=归位；列表被P分为两部分，左边都比P小，右边都比P大；递归
def partition(li,left,right):    # O(n)
    tmp=li[left]
    while left<right:
        while left<right and li[right]>=tmp:  # 从右边找比tmp小的数
            right-=1
        li[left]=li[right]    # 把右边的值写道左边空位
        while left<right and li[left]<=tmp:
            left+=1
        li[right]=li[left]   # 把左边的值写道右边空位
    li[left]=tmp  # 把第一个数归位 (也可以写成 li[right]=tmp,因为此时 li[left]=li[right])
    return left
def quick_sort(li,left,right):
    if left<right:   # 表示至少两个元素
        mid=partition(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)

li=[5,7,4,6,3,1,2,8]
quick_sort(li,0,len(li)-1)
print(li)
# ---------------------------------------------------
# 堆排序  O(n*logn)
# 顺序存储方式：
#       父节点和左子节点的编号有什么关系：i->2i+1
#       父节点和右子节点的编号有什么关系：i->2i+2
# 大根堆：一棵完全二叉树，满足任一节点都比其孩子节点大
# 小根堆：一棵完全二叉树，满足任一节点都比其孩子节点小
def sift(li,low,high):   # low指的是堆顶,high指的是堆的最后一个元素
    i=low
    j=2*i+1
    tmp=li[low]  #把堆顶存起来
    while j<=high:
        if j+1<=high and li[j+1]>li[j]:
            j=j+1
        if li[j]>tmp:
            li[i]=li[j]
            i=j     # 往下看一层
            j=2*i+1
        else:
            li[i]=tmp
            break
    else:
        li[i]=tmp
def heap_sort(li):
    n=len(li)
    for i in range((n-2)//2,-1,-1):  # 建堆
        sift(li,i,n-1)
    for i in range(n-1,-1,-1):   # i指向当前堆的最后一个元素
        li[0],li[i]=li[i],li[0]
        sift(li,0,i-1)
# -------------------------------------------------------
# 归并排序  O(nlogn)
# 归并
def merge(li,low,mid,high):
    i=low
    j=mid+1
    l_tmp=[]
    while i<=mid and j<=high:
        if li[i]<li[j]:
            l_tmp.append(li[i])
            i+=1
        else:
            l_tmp.append(li[j])
            j+=1
    while i<=mid:
        l_tmp.append(li[i])
        i+=1
    while j<=high:
        l_tmp.append(li[j])
        j+=1
    li[low:high+1]=l_tmp
def merge_sort(li,low,high):
    if low<high:  # 至少有两个元素
        mid=(low+high)//2
        merge_sort(li,low,mid)
        merge_sort(li, mid+1, high)
        merge(li,low,mid,high)
# ----------------------------------------------------
# 希尔排序
def insert_sort_gap(li,gap):   # 把插入排序的代码中的1改成
    for i in range(gap,len(li)):
        tmp=li[i]
        j=i-gap
        while j>=0 and li[j]>tmp:
            li[j+gap]=li[j]
            j-=gap
        li[j+gap]=tmp
def shell_sort(li):
    d=len(li)//2
    while d>=1:
        insert_sort_gap(li,d)
        d//=2

























# 列表排序--升序、降序
# sort()
