# 1. Given an integer num, repeatedly add all its digits until the result has
# only on digit, and return it
def practice1(num):
    li = list(str(num))
    li2=[]
    for i in li:
        li2.append(int(i))  # O(n)
    print(li2)
    if sum(li2)<10:
        return sum(li2)
    else:
        return practice1(sum(li2))
print('the resultof 338:  ')
print(practice1(338))

print('the resultof 12345:  ')
print(practice1(12345))


'''
T(n) = O(n^2)
S(n) = O(n)

'''