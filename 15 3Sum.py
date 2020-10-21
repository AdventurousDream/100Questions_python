from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k = n - 1
            target = -nums[i]
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                while j < k and nums[j] + nums[k] > target:
                    k -= 1
                if j >= k:
                    break
                if nums[j] + nums[k] == target:
                    ans.append([nums[i], nums[j], nums[k]])
        
        return ans


if __name__ == '__main__':
    solveObj = Solution()
    print(solveObj.threeSum([-1, 0, 1, 2, -1, -4]))