"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""


class Solution:
    
    def climbStairs(self, n: int) -> int:
        # 状态转移方程
        # dp(n) = dp(n-1) + dp(n-2)
        dp = n * [0]
        for i in range(0, n):
            if i in (0, 1):
                dp[i] = i + 1
            else:
                dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

    def climbStairs2(self, n: int) -> int:
        # 状态转移方程
        # dp(n) = dp(n-1) + dp(n-2)
        prev = 1
        current = 2
        if n == 1:
            return prev
        elif n == 2:
            return current
        else:
            for _ in range(2, n):
                next, prev=  prev + current, current
                current = next
        return current

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs2(1))
    print(s.climbStairs2(2))
    print(s.climbStairs2(3))
    print(s.climbStairs2(4))
    print(s.climbStairs2(5))
    print(s.climbStairs2(1000))
