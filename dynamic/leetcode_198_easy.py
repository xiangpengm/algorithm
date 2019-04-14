"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的
现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防
盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报
装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i-1], dp[i-2] + i)
        # 存上两个状态和当前状态
        dp = [0, 0, 0]
        if nums == []:
            return 0
        elif len(nums)<= 2:
            return max(nums)
        else:
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in nums[2:]:
                # print(dp)
                dp[2] = max(dp[1], dp[0]+i)
                dp[0] = dp[1]
                dp[1] = dp[2]
            return max(dp)


if __name__ == "__main__":
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
