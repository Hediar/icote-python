"""
N이 1이 될 때 까지
1. N - 1
2. (N % K == 0) N / K

최소 횟수만 실행하려면 최대한 많이 나누기
"""

n, k = map(int, input().split())
result1 = 0
result2 = 0
# 단순히 생각한걸 나열했을 때
while n >= k:
    while n % k != 0:
        n -= 1
        result1 += 1
    n //= k
    result1 += 1
while n > 1:
    n -= 1
    result1 += 1

# 한번에 빼버리기
while True:
    target = (n//k) * k
    result2 += (n - target)
    n = target
    if n < k:
        break
    result2 += 1
    n //= k
result2 += (n - 1)

print(result1, result2)