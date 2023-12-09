"""
정수 num1, num2가 매개변수로 주어집니다. 두 수가 같으면 1 다르면 -1을 return하도록 solution 함수를 완성해주세요.

제한사항
 - 0 <= num1 <= 10,000
 - 0 <= num2 <= 10,000

입출력 예
num1 = 2
num2 = 3
result = -1

num1 = 11
num2 = 11
result = 1

num1 = 7
num2 = 99
result = -1
"""

def solution(num1, num2):
    answer = 0
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer