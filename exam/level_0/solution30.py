"""
짝수의 합

정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

제한사항
 - 0 < n ≤ 1000

입출력 예
n = 10
result = 30

n = 4
result = 6
"""

def solution(n):
    answer = 0

    if n > 1:
        for i in range(2, n + 1, 2):
            answer += i

    return answer

print(solution(2))