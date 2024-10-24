def longest_common_subsequence(s1, s2):
    n, m = len(s1), len(s2)
    
    # Create a 2D array to store lengths of longest common subsequence
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Build the dp array
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:  # Characters match
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # Characters do not match
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[n][m]  # The length of LCS is found in dp[n][m]

def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])  # Number of test cases
    results = []
    
    for i in range(1, t + 1):
        s1, s2 = data[i].split()
        lcs_length = longest_common_subsequence(s1, s2)
        results.append(lcs_length)
    
    for result in results:
        print(result)

# Read input and solve the problem
solve()
