# 2. Given an integer n, return true if it is power of two. Otherwise, return false
# An integer n is a power of two, if there exists an integer x such that n==2x
def practice2(n):
    if n == 1:
        return True
    if  n%2==1:
        return False
    else:
        return practice2(n/2)
print('32' , practice2(32))
print('7' , practice2(7))
print('8' , practice2(8))
print('128' , practice2(128))

'''
T(n)=O(logn)
'''