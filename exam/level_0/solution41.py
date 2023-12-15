"""
공 던지기

머쓱이는 친구들과 동그랗게 서서 공 던지기 게임을 하고 있습니다. 공은 1번부터 던지며 오른쪽으로 한 명을 건너뛰고 그다음 사람에게만 던질 수 있습니다. 친구들의 번호가 들어있는 정수 배열 numbers와 정수 K가 주어질 때, k번째로 공을 던지는 사람의 번호는 무엇인지 return 하도록 solution 함수를 완성해보세요.

제한사항
 - 2 < numbers의 길이 < 100
 - 0 < k < 1,000
 - numbers의 첫 번째와 마지막 번호는 실제로 바로 옆에 있습니다.
 - numbers는 1부터 시작하며 번호는 순서대로 올라갑니다.

입출력 예
numbers = [1, 2, 3, 4]
k = 2
result = 3

numbers = [1, 2, 3, 4, 5, 6]
k = 5
result = 3

numbers = [1, 2, 3]
k = 3
result = 2

1 > 1 = 1 * 2 - 1 > 0
2 > 3 = 2 * 2 - 1 > 2
3 > 5 = 3 * 2 - 1 > 4 > i * 2 - 2

if len(numbers) = 4
    3번째 > 1번째 = 5 - 4 - 1
    4번째 > 3번째 = 7 - 4

if len(numbers) = 3
    3번째 > 2번째
    4번째 > 1번째
answer = numbers[i * 2 - 2]
"""

def solution(numbers, k):
    answer = 0

    length = 0
    for i in range(k):
        if i * 2 - 2 - length > length - 1:
            length += len(numbers)

        if i * 2 - 2 <= len(numbers) - 1:
            answer = numbers[i * 2 - 2]
        else:
            answer = numbers[i * 2 - 1 - length - 1]
        
        print(answer)
        
    return answer

print(solution([1, 2, 3, 4], 2))