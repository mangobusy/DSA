# Tower of Hanoi Problem
disk_num = int(input('please input the number of disks:'))
name = []
for i in range(1,disk_num+1):
    n = input('please input the name of disk {}:'.format(i))
    name.append(n)
print('the followings are the moving process:')

def hanoi(n,A,B,C,disk):
    if n==1:
        print('moving {} from {} to {}'.format(disk[0],A,C))
    else:
        hanoi(n-1,A,C,B,disk[:n-1:])
        print('moving {} from {} to {}'.format(disk[n-1],A,C))
        hanoi(n-1,B,A,C,disk[:n-1:])

hanoi(disk_num,'A','B','C',name)

# t(1)=1
# t(n)
# =t(n-1)+t(n-1)=2t(n-1)=2^1 t(n-1)
# =t(n-2)+t(n-2)+t(n-2)+t(n-2) = 2[2t(n-2)]=4t(n-2) = 2^2 t(n-2)
# =2^n t(1)
