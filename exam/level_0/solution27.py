"""
문자 반복 출력하기

문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.

제한사항
 - 2 ≤ my_string 길이 ≤ 5
 - 2 ≤ n ≤ 10
 - "my_string"은 영어 대소문자로 이루어져 있습니다.

입출력 예
my_string = "hello"
n = 3
result = "hhheeellllllooo"
"""

def solution(my_string, n):
    answer = ''

    for i in range(0, len(my_string)):
        answer += my_string[i:i + 1] * 3

    return answer