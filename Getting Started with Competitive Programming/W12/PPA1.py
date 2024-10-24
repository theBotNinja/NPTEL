MOD = 10**9 + 7

def find_paths(grid, N, M):
    # dp[i][j] will store the number of ways to reach cell (i, j)
    dp = [[0] * M for _ in range(N)]
    
    # Start at the top-left corner
    dp[0][0] = 1
    
    for i in range(N):
        for j in range(M):
            if grid[i][j] == -1:  # If the cell is a dead-end, skip it
                dp[i][j] = 0
            else:
                # Add paths from top
                if i > 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
                # Add paths from left
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD
    
    # Return the number of ways to reach the bottom-right corner
    return dp[N-1][M-1]

def solve():
    T = int(input())  # Number of test cases
    for _ in range(T):
        N, M = map(int, input().split())
        grid = []
        for i in range(N):
            grid.append(list(map(int, input().split())))
        result = find_paths(grid, N, M)
        print(result)

# Solve the problem
solve()
