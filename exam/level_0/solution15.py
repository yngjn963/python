"""
짝수는 싫어요

정수 n 이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return 하도록 solution 함수를 완성해주세요.

제한사항
 - 1 <= n <= 100

입출력 예
n = 10
result = [1, 3, 5, 7, 9]

n = 15
result = [1, 3, 5, 7, 9, 11, 13, 15]
"""

def solution(n):
    answer = []
    for i in range(1, n + 1, 2):
        answer.append(i)

    print(answer)
    return answer

solution(15)