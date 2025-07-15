"""
홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N ** 2 까지의 자연수를 달팽이 모양으로 N * N의 표에 채울 수 있다

위 오른쪽 아래 왼쪽

"""
import sys
input = sys.stdin.readline

# N 배열 크기 target 목표
N = int(input())
target = int(input())

# 숫자를 저장할 배열
arr = [[0] * N for _ in range(N)]

# 이동 순서를 저장한 딕셔너리
# 아래>>오른쪽>>위>>왼쪽
direction = {
    0: [1, 0],
    1: [0, 1],
    2: [-1, 0],
    3: [0, -1],
}

# 왼쪽 위부터 거꾸로 숫자를 채워넣을 것이기 때문에 N * N 부터 시작
num = N * N

# 시작 이동방향
dr = 0
# 시작 위치
r, c = 0, 0
# 목표 지점 위치 초기값 설정
target_r, target_c = 0, 0

# num이 1이 될 때까지 반복
while num > 0:
    # 숫자 넣기
    arr[r][c] = num

    # 목표 지점에 도착하면 좌표 저장
    if num == target:
        target_r, target_c = r, c

    # 현재 방향으로 다음 좌표 지정
    nr, nc = r + direction[dr][0], c + direction[dr][1]

    # 다음 좌표가 배열을 벗어나거나 이미 숫자가 채워져 있는 경우 방향 전환
    if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] != 0:
        dr = (dr + 1) % 4

    # 다음 좌표 설정
    # nr, nc로 설정하면 안됨!! >> 방향을 전환한 경우 전환한 방향으로 다음 좌표를 계산해야 하기 때문
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