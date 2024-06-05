def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for target in range(1, amount + 1):
        for coin in coins:
            if coin <= target:
                dp[target] = min(dp[target], dp[target - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
inp = open('input4.txt', 'r')
out = open('output4.txt', 'w')
N, X = map(int, inp.readline().split())
coins = list(map(int, inp.readline().split()))
result = min_coins(coins, X)
out.write(str(result))
inp.close()
out.close()
