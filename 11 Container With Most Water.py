from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res



if __name__ == '__main__':
    solveObj = Solution()
    print(solveObj.maxArea([1,8,6,2,5,4,8,3,7]))