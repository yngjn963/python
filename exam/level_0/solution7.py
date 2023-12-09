"""
정수 num1, num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return하도록 solution 함수를 완성해주세요.

제한사항
 - 0 <= num1 <= 100
 - 0 <= num2 <= 100

입출력 예
num1 = 3
num2 = 2
result = 1500

num1 = 7
num2 = 3
result = 2333

num1 = 1
num2 = 16
result = 62
"""

def solution(num1, num2):
    answer = int(num1 / num2 * 1000)
    return answer