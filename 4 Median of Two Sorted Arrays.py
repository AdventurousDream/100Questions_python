from typing import List

# O(log(m+n))

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findK(k):
            i1 = 0
            i2 = 0
            while True:
                # 特殊情况
                if i1 == len1:
                    return nums2[i2 + k - 1]
                if i2 == len2:
                    return nums1[i1 + k - 1]
                if k == 1:
                    return min(nums1[i1], nums2[i2])

                # 正常情况
                newI1 = min(i1 + k // 2 - 1, len1 - 1)
                newI2 = min(i2 + k // 2 - 1, len2 - 1)
                
                if nums1[newI1] <= nums2[newI2]:
                    k = k - (newI1 - i1 + 1)
                    i1 = newI1 + 1
                else:
                    k = k - (newI2 - i2 + 1)
                    i2 = newI2 + 1
        
        len1 = len(nums1)
        len2 = len(nums2)
        totlen = len1 + len2
        if totlen % 2 == 1:
            return findK((totlen + 1) // 2)
        else:
            return (findK(totlen // 2) + findK(totlen // 2 + 1)) / 2


     
if __name__ == '__main__':
    solveObj = Solution()
    print("%d" % (solveObj.findMedianSortedArrays([1,3,4,9], [1,2,3,4,5,6,7,8,9])))