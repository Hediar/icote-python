n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result1 = 0
result2 = 0

# 단순한 방식
while True:
    for i in range(k):
        if m == 0:
            break
        result1 += first
        m -= 1
    if m == 0:
        break
    result1 += second
    m -= 1

# 간단한 계산식을 이용한 방식
count = int(m/(k+1))*k
count += m % (k+1)

result2 += count * first
result2 += (m - count) * second

print(result1, result2)
