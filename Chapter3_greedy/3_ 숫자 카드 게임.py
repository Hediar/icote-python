n, m = map(int, input().split())

result1 = 0 
result2 = 0
# min과 max를 이용한 방식
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result1 = max(result1, min_value)

# 2중 반북문을 이용한 방식
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result2 = max(result2, min_value)

print(result1, result2)