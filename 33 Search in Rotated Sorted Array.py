from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        arr_len = len(nums)
        if arr_len == 0:
            return -1
        l, r = 0, arr_len - 1
        while True:
            if l > r:
                return -1
            if l == r:
                if nums[l] == target:
                    return l
                else:
                    return -1
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[l]:
                if target > nums[mid]:
                    l = mid + 1
                else:
                    if target >= nums[l]:
                        r = mid - 1
                    else:
                        l = mid + 1
            else:
                if target > nums[mid]:
                    if target > nums[r]:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    r = mid - 1
        return -1

if __name__ == "__main__":
    solveObj = Solution()
    print(solveObj.search([4,5,6,7,0,1,2], 0))