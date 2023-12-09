"""
첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 답은 배열을 return 하도록 solution 함수를 완성해보세요.

제한사항
 - 0 < numer1, denom1, numer2, denom2 < 1,000

입출력 예
numer1 = 1
denom1 = 2
numer2 = 3
denom2 = 4
result = [5, 4]

numer1 = 9
denom1 = 2
numer2 = 1
denom2 = 3
result = [29, 6]
"""

def solution(numer1, denom1, numer2, denom2):
    answer = [numer1 * denom2 + numer2 * denom1, denom1 * denom2]
    for i in range(min(answer[0], answer[1]), 0, -1):
        if answer[0] % i == 0 and answer[1] % i == 0:
            answer[0] = answer[0] / i
            answer[1] = answer[1] / i
            break;
    return answer