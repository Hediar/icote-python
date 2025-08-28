#  abcde
# 1
# 2
# ...

# 나이트가 이동 가능한 경우의 수

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

movement = [(-2,-1), (-1, -2), (1, -2), (-2, 1), (2, 1), (1, 2), (-1, 2), (2, -1)]
result = 0

for move in movement:
    next_row = row + move[0]
    next_column = column + move[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)