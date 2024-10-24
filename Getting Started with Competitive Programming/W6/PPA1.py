import sys
from collections import deque

# Fast input
input = sys.stdin.read
data = input().splitlines()

# Initialize variables for input
idx = 0
T = int(data[idx])
idx += 1

results = []

for _ in range(T):
    n, m = map(int, data[idx].split())
    idx += 1
    
    matrix = []
    empty_seats = []
    
    # Collect matrix and empty seat positions
    for i in range(n):
        row = list(map(int, data[idx].split()))
        matrix.append(row)
        for j in range(m):
            if row[j] == 0:
                empty_seats.append((i, j))
        idx += 1
    
    # If there are fewer than two empty seats, the result is -1
    if len(empty_seats) < 2:
        results.append(-1)
        continue

    # BFS to calculate the minimum distance
    min_distance = sys.maxsize
    for i in range(len(empty_seats)):
        for j in range(i+1, len(empty_seats)):
            r1, c1 = empty_seats[i]
            r2, c2 = empty_seats[j]
            distance = abs(r1 - r2) + abs(c1 - c2)
            min_distance = min(min_distance, distance)
    
    results.append(min_distance)

# Output all results
sys.stdout.write("\n".join(map(str, results)) + "\n")
