n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1] # U, D
dy = [-1, 1, 0, 0] # L, R
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny # 범위를 벗어나지 않으면, 반영

print(x, y)