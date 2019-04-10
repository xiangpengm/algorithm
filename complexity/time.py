from datetime import datetime

# 设 每行运行时间 =1


# 统计函数平均运行时间
def clock(func):
    def wrapper(*args, **kwargs):
        loop = 10
        start = datetime.now()
        for _ in range(loop):
            r = func(*args, **kwargs)
        end = datetime.now()
        use_time = (end - start)/loop
        print('run time', func.__name__.ljust(10), str(use_time.microseconds).rjust(10), "ms")
        return r
    return wrapper


#时间复杂度 O(1)
# 与数据规模没关系
@clock
def cal_1(n):
    array = range(n)
    if n > 100:
        # 1
        return array[100]


# 时间复杂度 O(n)
# 与数据规模线性相关
@clock
def cal_n(n):
    # 1
    s = 0
    # x
    for i in range(n):
        # x
        s = s + i
    # 2n + 1
    # 去掉低位和系数
    # n
    # 得到此函数的时间复杂度为n
    return s


# 时间复杂度 O(n^2)
# 与数据规模指数相关
@clock
def cal_n2(n):
    # 1
    s = 0
    # n
    for i in range(n):
        #  n*n
        for l in range(n):
            # n*n
            s = s + i * l
    # 2n^2 + n + 1
    # n^2
    # 因此得到此函数的时间复杂度为n^2
    return s


# 时间复杂度 O(nlogn)
@clock
def cal_n_logn(n):
    # 1
    s = 0
    # n
    for i in range(n):
        # n
        l = 1
        # n * log2n
        while l < n:
            l *= 2
            s = s + i * l
    # n*log2n + 2n + 1
    # nlogn
    # 因此得到此函数的时间复杂度为nlogn
    return s


def main():
    n = 100
    cal_1(n)
    cal_n(n)
    cal_n2(n)
    cal_n_logn(n)
    n = 1000
    cal_1(n)
    cal_n(n)
    cal_n_logn(n)
    cal_n2(n)


if __name__ == "__main__":
    main()
