def max_points(nums):
    if not nums:
        return 0
    
    # Step 1: Count occurrences of each number
    max_num = max(nums)
    count = [0] * (max_num + 1)
    
    for num in nums:
        count[num] += 1
    
    # Step 2: Use dynamic programming to calculate the maximum points
    dp = [0] * (max_num + 1)
    
    dp[1] = count[1] * 1  # Base case
    
    for i in range(2, max_num + 1):
        dp[i] = max(dp[i-1], dp[i-2] + i * count[i])
    
    return dp[max_num]

# Input reading and output
n = int(input())  # Number of elements in the sequence
nums = list(map(int, input().split()))  # The sequence of integers

# Output the maximum points that can be earned
print(max_points(nums))
