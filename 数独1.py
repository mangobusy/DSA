import random
import numpy as np

def set_board():
    # def print_sudo(sudo):
    #     for row_index, row in enumerate(sudo):
    #         if row_index % 3 == 0 and row_index != 0:
    #             print('-' * (9 + 8 + 4))
    #         row = list(map(str, row.tolist()))
    #         row.insert(6, '|')
    #         row.insert(3, '|')
    #         print(' '.join(row))

    # def get_row(sudo, row):
    #     return sudo[row, :]
    #
    # def get_col(sudo, col):
    #     return sudo[:, col]
    #
    # def get_block(sudo, row, col):
    #
    #     row_start = row // n ** n
    #     col_start = col // n ** n
    #     return sudo[row_start: row_start + n , col_start: col_start + n]
    #
    # def create_base_sudo():
    #     sudo = np.zeros((n ** 2, n ** 2), dtype=int)
    #     num = random.randrange(n ** 2) + 1
    #     # 遍历从左到右，从上到下逐个遍历
    #     for row_index in range(n ** 2):
    #         for col_index in range(n ** 2):
    #             # 获取该格子对应的行、列、九宫格
    #             sudo_row = get_row(sudo, row_index)
    #             sudo_col = get_col(sudo, col_index)
    #             sudo_block = get_block(sudo, row_index, col_index)
    #             # 如果该数字已经存在于对应的行、列、九宫格
    #             # 则继续判断下一个候选数字，直到没有重复
    #             while num in sudo_row or num in sudo_col or num in sudo_block:
    #                 num = num % (n ** 2) + 1
    #             # 赋值
    #             sudo[row_index, col_index] = num
    #             num = num % n ** 2 + 1
    #     return sudo
    #
    # def random_sudo(sudo, times):
    #     for _ in range(times):
    #         # 随机交换两行
    #         rand_row_base = random.randrange(3) * 3  # 从0，3，6 随机取一个
    #         rand_rows = random.sample(range(3), 2)  # 从 0，1，2中随机取两个数
    #         row_1 = rand_row_base + rand_rows[0]
    #         row_2 = rand_row_base + rand_rows[1]
    #         sudo[[row_1, row_2], :] = sudo[[row_2, row_1], :]
    #         # 随机交换两列
    #         rand_col_base = random.randrange(3) * 3
    #         rand_cols = random.sample(range(3), 2)
    #         col_1 = rand_col_base + rand_cols[0]
    #         col_2 = rand_col_base + rand_cols[1]
    #         sudo[:, [col_1, col_2]] = sudo[:, [col_2, col_1]]
    #     return sudo
    #
    # def get_sudo_subject(sudo, del_nums):
    #     # 最少要保留17个数字，题目才可解。一共81个数字，则最多可以擦除81-17 = 64。
    #     max_clear_count = (n - 1) ** 2
    #     # 最少也要擦除14个
    #     min_clear_count = (n ** 2) - (n - 1) ** 2
    #
    #     if del_nums < min_clear_count:
    #         del_nums = min_clear_count
    #     if del_nums > max_clear_count:
    #         del_nums = max_clear_count
    #
    #     # 随机擦除（从0到80，随机取要删除的个数）
    #     clears = random.sample(range(n ** 4), del_nums)
    #     for clear_index in clears:
    #         # 把0到80的坐标转化成行和列索引
    #         # 这样就不会重复删除同一个格子的数字
    #         row_index = clear_index // n ** 2
    #         col_index = clear_index % n ** 2
    #         sudo[row_index, col_index] = 0
    #     return sudo
    #
    # n = int(input('please input a number'))
    # sudo = create_base_sudo()
    # random_sudo(sudo, 30)
    # get_sudo_subject(30)
    n = int(input('please input a number'))
    max_num=n**2
    min
#------------------------------------------------------

def start_pos(set_board):
    for x in range(9):
        for y in range(9):
            if set_board[x][y]==0:
                return (x,y)
    return False,False

def get_next(set_board,x,y):
    for next_y in range(y+1,9):
        if set_board[x][next_y]==0:
            return (x,next_y)
    for next_x in range(x+1,9):
        for next_y in range(0,9):
            if set_board[next_x][next_y]==0:
                return (next_x,next_y)
    return -1,-1

def value(set_board,x,y):
    i,j=x//3,y//3
    grid=[set_board[i*3+r][j*3+c] for r in range(3) for c in range(3)]
    v=set([x for x in range(1,10)])-set(grid)-set(set_board[x])-\
      set(list(zip(*set_board))[y])
    return list(v)

def solve(set_board,x,y):
    for v in value(set_board,x,y):
        set_board[x][y]=v
        next_x,next_y=get_next(set_board,x,y)
        if next_y==-1:
            return True
        else:
            end=solve(set_board,next_x,next_y)
            if end:
                return True
            set_board[x][y]=0

def sudoku(board):
    x,y=start_pos(board)
    solve(board,x,y)
    print(board)

sudoku(set_board())

