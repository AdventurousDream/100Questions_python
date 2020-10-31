
def canJump(nums: List[int]) -> bool:
    n = len(nums)
    cur = 0
    while True:
        if cur == -1:
            return False
        nxt = -1
        maxdist = -1
        for i in range(1, nums[cur] + 1):
            j = cur + i
            if (j + nums[j]) >= n:
                return True
            if (j+nums[j]) > maxdist:
                maxdist = j+nums[j]
                nxt = j
        cur = nxt