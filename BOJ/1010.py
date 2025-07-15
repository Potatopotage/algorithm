"""
재원이는 한 도시의 시장이 되었다

서쪽에는 N개의 사이트, 동쪽에는 M개의 사이트(N <= M)
서쪽의 사이트 개수만큼 다리를 짓는다
다리끼리는 서로 겹쳐질 수 없다고 할 때, 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 구하라
"""
import sys
input = sys.stdin.readline

# M개 중에서 N개를 고르는 경우의 수를 구하는 함수
def comb(N, M):
    # 경우의 수 초기값
    result = 1

    for i in range(1, N + 1):
        # M을 거꾸로 곱하기
        result *= M - i + 1
        # 곱하는 즉시 N을 1부터 증가시키면서 나눠주기(overflow 방지)
        result //= i
    return result

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    print(comb(N, M))

"""
1
5
67863915
"""