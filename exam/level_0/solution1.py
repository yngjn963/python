"""
중복된 숫자 개수

정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는지를 return 하도록 solution 함수를 완성해보세요.

제한사항
 - 1 <= array의 길이 <= 100
 - 0 <= array의 원소 <= 1000
 - 0 <= n <= 1000

입출력 예
array = [1, 1, 2, 3, 4, 5]
n = 1
result = 2

array = [0, 2, 3, 4]
n = 1
result = 0
"""

def solution(array, n):
    answer = array.count(n)
    return answer