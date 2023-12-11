"""
최빈값 구하기

최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array 가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1 을 return 합니다.

제한사항
 - 0 < array 의 길이 < 100
 - 0 <= array 의 원소 < 1,000

입출력 예
array = [1, 2, 3, 3, 3, 4]
result = 3

array = [1, 1, 2, 2]
result = -1

array = [1]
result = 1
"""

def solution(array):
    answer = 0

    array_range = [0] * (max(array) + 1)

    for num in array:
        array_range[num] += 1

    array_range_sort = []
    array_range_sort.extend(array_range)
    array_range_sort.sort(reverse=True)
    array_range_sort.sort(reverse=True)
    if len(array_range_sort) > 1 and array_range_sort[0] == array_range_sort[1]:
        answer = -1
    else:
        answer = array_range.index(max(array_range))

    return answer

print(solution([1, 1, 2, 2]))