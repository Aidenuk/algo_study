# recursive solution -> time complexity: O(n*m)
def change(amount, coins):
    cache = {}
    def dfs(i, a):
        if a == amount:
            return 1
        if a > amount:
            return 0
        if i == len(coins):
            return 0
        if (i, a) in cache:
            return cache[(i, a)]

        cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
        return cache[(i, a)]

    return dfs(0,0)


print(change(5,[1,2,5]))


