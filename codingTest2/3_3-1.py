n, m = map(int, input().split())
result = 0

for i in range(n):
    arr = list(map(int, input().split()))
    min_val = 10001
    for j in arr:
        min_val = min(j, min_val)
    result = max(result, min_val)

print(result)