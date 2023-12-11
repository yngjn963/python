"""
문자열 뒤집기

문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.

제한사항
 - 1 ≤ my_string의 길이 ≤ 1,000

입출력 예
my_string = "jaron"
result = "noraj"

my_string = "bread"
result = "daerb"
"""

def solution(my_string):
    answer = list(my_string)
    answer.reverse()
    return "".join(answer)