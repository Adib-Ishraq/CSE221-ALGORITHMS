def count_ways(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

inp = open('input3.txt', 'r')
out = open('output3.txt', 'w')
n = int(inp.readline().strip())
result = count_ways(n)
out.write(str(result))
inp.close()
out.close()
