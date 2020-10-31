from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx = 0):
            if idx == n:  
                ans.append(nums[:])
            for i in range(idx, n):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]
            
        n = len(nums)
        ans = []
        backtrack()
        return ans

if __name__ == '__main__':
    obj = Solution()
    print(obj.permute([1,2,3]))