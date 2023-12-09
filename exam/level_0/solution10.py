"""
정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

제한사항
 - -10,000 <= numbers의 원소 <= 10,000
 - 1 <= numbers의 길이 <= 1,000

입출력 예
numbers = [1, 2, 3, 4, 5]
result = [2, 4, 6, 8, 10]

numbers = [1, 2, 100, -99, 1, 2, 3]
result = [2, 4, 200, -198, 2, 4, 6]
"""

def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i * 2)
    return answer
    # [num * 2 for num in numbers] 리스트 컴프리헨션