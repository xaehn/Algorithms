# Circular path
def tsp(n, cost, k):
    dp = [n * [float("INF")] for _ in range(1 << n)]
    dp[1 << k][k] = 0

    for visited in range(1 << n):
        for current in range(n):
            if visited & (1 << current):
                for next in range(n):
                    if not (visited & (1 << next)):
                        next_visited = visited | (1 << next)
                        dp[next_visited][next] = min(
                            dp[next_visited][next],
                            dp[visited][current] + cost[current][next]
                        )

    min_cost = float("INF")
    for i in range(n):
        if not i == k:
            min_cost = min(min_cost, dp[(1 << n) - 1][i] + cost[i][k])

    return min_cost

# Simple path
def tsp(n, cost, k):
    dp = [n * [float("INF")] for _ in range(1 << n)]
    dp[1 << k][k] = 0

    for visited in range(1 << n):
        for current in range(n):
            if visited & (1 << current):
                for next in range(n):
                    if not (visited & (1 << next)):
                        next_visited = visited | (1 << next)
                        dp[next_visited][next] = min(
                            dp[next_visited][next],
                            dp[visited][current] + cost[current][next]
                        )

    min_cost = float("INF")
    for i in range(n):
        if not i == k:
            min_cost = min(min_cost, dp[(1 << n) - 1][i])

    return min_cost