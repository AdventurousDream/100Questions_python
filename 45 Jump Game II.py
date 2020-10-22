from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        arr_len = len(nums)
        if arr_len == 1:
            return 0
        ans = 0
        
        curIdx = 0
        maxPos = -1
        nextIdx = -1
        while True:
            if curIdx + nums[curIdx] >= arr_len - 1:
                return ans+1
            curMaxPos = -1
            for step in range(1,nums[curIdx]+1):
                j = curIdx + step
                if j >= arr_len:
                    break
                if nums[j] + j > curMaxPos:
                    curMaxPos = nums[j] + j
                    nextIdx = j
            curIdx = nextIdx
            ans += 1
            if curIdx >= arr_len - 1:
                return ans



if __name__ == '__main__':
    solveObj = Solution()
    print(solveObj.jump([2,3,1,2,4,2,3]))