from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        arr_len = len(height)
        l, r = 0, arr_len - 1    
        ans = 0
        lm, rm = 0, 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= lm:
                    lm = height[l]
                else:
                    ans += lm - height[l]
                l += 1
            else:
                if height[r] >= rm:
                    rm = height[r]
                else:
                    ans += rm - height[r]
                r -= 1
        return ans

if __name__ == '__main__':
    solveObj = Solution()
    print(solveObj.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
