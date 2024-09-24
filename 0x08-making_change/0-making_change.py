#!/usr/bin/python3
"""Difines a module making a change"""


def makeChange(coins, total):
    """Return the minimum number of coins needed to make change
    for `total` using
    the given `coins` denominations. If no combination of coins sums
    up to `total`,
    return -1.
    """
    if total <= 0:
        return 0

    # Initialize an array of size `total + 1` with all elements
    # set to infinity,
    # except for the first element which is 0.
    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    # Iterate over each coin denomination.
    for coin in coins:
        # Iterate over each amount from `coin` to `total`.
        for amount in range(coin, total + 1):
            # Update `dp[amount]` to be the minimum of its current value and
            # `dp[amount - coin] + 1`.
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If `dp[total]` is still infinity, then no combination
    # of coins sums up to
    # `total`, so return -1. Otherwise, return `dp[total]`.
    return dp[total] if dp[total] != float("inf") else -1
