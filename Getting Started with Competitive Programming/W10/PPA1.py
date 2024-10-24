def max_prefix_sum(arr):
    max_sum = 0
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read n and the red sequence
    n = int(input())
    r = list(map(int, input().split()))
    
    # Read m and the blue sequence
    m = int(input())
    b = list(map(int, input().split()))
    
    # Compute the maximum prefix sums for both sequences
    max_r = max_prefix_sum(r)
    max_b = max_prefix_sum(b)
    
    # The result is the sum of the two maximum prefix sums
    result = max_r + max_b
    
    # Print the result
    print(result)
