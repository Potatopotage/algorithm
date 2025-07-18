"""
n이 주어졌을 때 n번째 피보나치 수를 구하는 프로그램을 구하시오

f1 = 0
f2 = 1
fn = fn-1 + fn-2
"""
import sys
input = sys.stdin.readline

def fibonacci(n):
    # 0이나 1이면 바로 반환
    if n == 0 or n == 1:
        return n

    # 숫자를 저장할 배열 생성
    arr = [0] * (n + 1)
    
    # 초기값 입력
    arr[0] = 0
    arr[1] = 1

    # 현재 위치에 이전 값과 그 전값의 합 저장
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    # 배열의 마지막 값 반환
    return arr[-1]

N = int(input())
print(fibonacci(N))


"""
55
"""