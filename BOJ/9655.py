"""
탁자에 돌 N개가 있다
상근이와 창영이는 턴을 번갈아가며 돌을 가져가며, 돌은 1개 혹은 3개를 가져갈 수 있다
마지막 돌을 가져가는 사람이 게임을 이기게 된다

두 사람이 완벽하게 게임을 했을 때, 이기는 사람을 구하는 프로그램을 구하시오
게임은 상근이가 먼저 시작한다

상근이가 이기면 SK, 창영이가 이기면 CY를 출력한다
"""
import sys
input = sys.stdin.readline

N = int(input())

# 그냥 풀기
if N % 2 == 0:
    print('CY')
else:
    print('SK')

# DP로 풀기
arr = [False] * (N + 1)

# False면 SK True면 CY가 이기는 경우로 설정

# 초기값 설정
if N >= 1:
    arr[1] = False
if N >= 2:
    arr[2] = True
if N >= 3:
    arr[3] = False

# 현재의 첫번째 혹은 세 번째 돌을 가져간 적이 있다면 현재는 이길 수 있다
for i in range(4, N + 1):
    # arr[i-1]이 false이거나 arr[i-3]이 false인 경우
    arr[i] = (not arr[i-1]) or (not arr[i-3])

# 배열의 마지막 인덱스에 따라 값 출력
if arr[N] == False:
    print('SK')
else:
    print('CY')

"""
SK
"""