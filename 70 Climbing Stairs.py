
def climbStairs(n: int) -> int:
        if n == 1:
            return 1
        pre1 = 1
        pre2 = 1
        cur = 1
        for i in range(2,n+1):
            cur = pre1 + pre2
            pre1 = pre2
            pre2 = cur
        
        return cur