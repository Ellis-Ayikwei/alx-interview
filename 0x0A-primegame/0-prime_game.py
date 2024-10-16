#!/usr/bin/python3
"""The Game theory"""


def sieve_of_eratosthenes(n):
    """Generate a list of booleans indicating whether each number 
    <= n is prime."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes


def play_game(n, primes):
    """Simulate the game for a given n and return
    the winner ('Maria' or 'Ben')."""
    primes_in_game = [i for i in range(1, n + 1) if primes[i]]
    moves = 0
    while primes_in_game:
        # Maria picks first (odd moves), Ben picks second (even moves)
        prime = primes_in_game[0]
        primes_in_game = [x for x in primes_in_game if x % prime != 0]
        moves += 1

    # Maria wins if the number of moves is odd, Ben wins if even
    if moves % 2 == 1:
        return "Maria"
    else:
        return "Ben"


def isWinner(x, nums):
    """Determine the overall winner after x rounds of the game."""
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)  
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n, primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
