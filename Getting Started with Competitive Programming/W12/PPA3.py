def max_pieces(n, a, b, c):
    # Create a dp array to store the maximum number of pieces for each length
    dp = [-1] * (n + 1)  # Initialize with -1 (impossible)
    dp[0] = 0  # Base case: 0 length can be achieved with 0 pieces

    # Iterate through all lengths from 1 to n
    for length in range(1, n + 1):
        # Check each piece length (a, b, c)
        for piece_length in (a, b, c):
            if length >= piece_length and dp[length - piece_length] != -1:
                dp[length] = max(dp[length], dp[length - piece_length] + 1)

    return dp[n]  # The answer will be the maximum number of pieces for length n

# Read input
n, a, b, c = map(int, input().split())
result = max_pieces(n, a, b, c)
print(result)
