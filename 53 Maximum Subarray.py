
def maxSubArray(nums: List[int]) -> int:
    ans = nums[0];
    tmpans = 0;
    for n in nums:
        if tmpans > 0:
            tmpans += n
        else:
            tmpans = n
        ans = max(ans,tmpans)
    return ans
