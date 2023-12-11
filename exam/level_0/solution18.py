"""
배열의 평균값

정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

제한사항
 - 0 <= numbers 의 원소 <= 1,000
 - 1 <= numbers 의 길이 <= 100

입출력 예
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = 5.5

numbers = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
result = 94.0
"""

def solution(numbers):
    answer = 0

    sum = 0
    for i in numbers:
        sum += i
    
    return sum / len(numbers)
    # return sum(numbers) / len(numbers)