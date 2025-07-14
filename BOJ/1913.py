"""
홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N ** 2 까지의 자연수를 달팽이 모양으로 N * N의 표에 채울 수 있다

위 오른쪽 아래 왼쪽

"""
import sys
sys.stdin = open('1913.txt', 'r')

N = int(input())
target = int(input())

arr = [[0] * N for _ in range(N)]

# 거꾸로 맨 뒤에서부터
direction = {
    0: [1, 0],
    1: [0, 1],
    2: [-1, 0],
    3: [0, -1],
}

num = N * N
dr = 0
r, c = 0, 0
target_r, target_c = 0, 0

while num > 0:
    arr[r][c] = num
    nr, nc = r + direction[dr][0], c + direction[dr][1]

    if num == target:
        target_r, target_c = r, c

    if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] != 0:
        dr = (dr + 1) % 4

    r += direction[dr][0]
    c += direction[dr][1]
    num -= 1


for row in arr:
    print(*row)
print(target_r + 1, target_c + 1)





"""
49 26 27 28 29 30 31
48 25 10 11 12 13 32
47 24 9 2 3 14 33
46 23 8 1 4 15 34
45 22 7 6 5 16 35
44 21 20 19 18 17 36
43 42 41 40 39 38 37
5 7
"""