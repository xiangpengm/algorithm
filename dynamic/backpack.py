from collections import defaultdict


def log_matrix(matrix):
    for line in matrix:
        print(line)
    print()


# 递归
def jie(weight_list, weight_threshold):
    l = len(weight_list)
    mem = set()
    def f(index, current_weight):
        if index == l:
            print(index * '    ', index, current_weight)
            return 
        # 不装
        # 检查是否计算过
        if (index+1, current_weight) not in mem:
            f(index+1, current_weight)
            mem.add((index+1, current_weight))
        print( index * '    ' , index, current_weight)
        # 小于 阈值 的 装入
        if (current_weight + weight_list[index] <= weight_threshold):
            # 检查是否计算过
            if (index+1, current_weight + weight_list[index]) not in mem:
                f(index+1, current_weight+weight_list[index])
                mem.add((index+1, current_weight+weight_list[index]))
    # 调用
    f(0, 0)

    

# 经典问题
def dynamic_weight():
    weight = [2, 2, 4, 6, 3]
    back_thr = 9
    #  初始化一个矩阵
    matrix = [[0] * 9 for _ in range(len(weight))]
    log_matrix(matrix)
    for index, weight_value in enumerate(weight):
        # 放入
        if index == 0:
            # 不放入
            matrix[index][0] = 1
            # 放入
            matrix[index][weight_value] = 1
        else:
            # 不放入
            matrix[index] = matrix[index-1].copy()
            # 放入
            # 合并同类项
            for current_weight, have in enumerate(matrix[index-1]):
                # 是否存在
                if have == 1:
                    # 判断是否超过背包重量
                    if current_weight + weight_value < back_thr:
                        # 小于重量
                        print('set index:{} weight: {} = True'.format(index, current_weight + weight_value))
                        # 防止重复设置
                        if matrix[index][current_weight + weight_value] != 1:
                            matrix[index][current_weight + weight_value] = 1
        log_matrix(matrix)
    return


# 
def test():
    name = ['吉他', '音箱', '笔记本']
    value = [1500, 3000, 2000]
    weight = [1, 4, 3]
    pack_size = 4
    data = list(zip(name, value, weight))
    matrix = [[[0, 0] for i in range(pack_size)] for _ in data]
    # 状态转移方程
    # cell[i][j] = max(cell[i-1][j], i + cell[i-1][j - 当前商品重量]
    cell = matrix
    for i, line in enumerate(matrix):
        current_goods = data[i]
        print("out current goods: ",current_goods)
        value = current_goods[1]
        weight = current_goods[2]
        for j, _ in enumerate(line):
            child_backpack_size = j + 1
            if i == 0:
                if weight <= child_backpack_size:
                    cell[i][j][0] = value
                    cell[i][j][1] = weight
            else:
                a = cell[i-1][j]
                # b = value + cell
                if weight > child_backpack_size:
                    b = [0, 0]
                elif weight == child_backpack_size:
                    b = [value, weight]
                else:
                    mod = cell[i-1][j - weight]
                    value = mod[0] + value
                    weight = mod[1] + weight
                    b = [value, weight]
                cell[i][j] = max(a, b, key=lambda x: x[0])
        log_matrix(cell)


# 杨辉三角
def tringle(triangle):
    # triangle = [
    #   [2],
    #  [3,4],
    #  [6,5,7],
    # [4,1,8,3]
    # ]
    """
               tringle[i][j]
    tringle[i+1][j]   tringle[i+1][j+1]
    状态转移方程
    dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
    """
    length = len(triangle)
    dp = [0] * (length + 1)
    i = length - 1
    while i >= 0:
        line = triangle[i]
        for j, _ in enumerate(line):
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        i -= 1
    return dp[0]


if __name__ == "__main__":
    # dynamic_weight()
    # weight_list = [2, 2, 4, 6, 3]
    # weight_threshold = 9
    # print(jie(weight_list, weight_threshold))
    # test()
    triangle = [
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
    ]
    print(tringle(triangle))
