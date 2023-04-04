def knapsack(weights, values, max_weight):
    n = len(weights)
    dp = [0] * (max_weight + 1)

    for i in range(n):
        for j in range(max_weight, weights[i]-1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp[max_weight]


costs = [5,3,9]
weigths = [10,20,30]
weight_of_inventory = 50

print(knapsack(weigths, costs, weight_of_inventory))