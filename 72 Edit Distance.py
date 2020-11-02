
def minDistance(word1: str, word2: str) -> int:
    n1,n2 = len(word1),len(word2)
    dp = [[0x3f3f3f] * (n2+1) for _ in range(n1+1)]
    for i in range(n1+1):
        dp[i][0] = i
    for i in range(n2+1):
        dp[0][i] = i
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = min(dp[i][j],dp[i-1][j-1])
            dp[i][j] = min(dp[i][j],dp[i-1][j-1]+1,dp[i][j-1]+1,dp[i-1][j]+1)
    return dp[n1][n2]

print(minDistance("intention","execution"))