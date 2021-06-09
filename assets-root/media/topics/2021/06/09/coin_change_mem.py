coins = [1, 3, 4]
n_of_coins = len(coins)
INF = coins[n_of_coins-1]
values = {}


def solve(x):
    if (x < 0):
        return INF

    if (x == 0):
        return 0

    if(values.get(x) != None):
        return values.get(x)

    best = INF
    for i in range(n_of_coins):
        best = min(best, solve(x - coins[i]) + 1)

    values[x] = best
    return best


print(solve(6))