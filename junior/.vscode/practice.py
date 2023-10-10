print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*10)

# 참 / 거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

# 애완동물을 소개해 주세요~
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult =  age >= 3
# 변수: 값이 저장되는 공간

print("우리집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

print("우리집 " + animal + "의 이름은 " + name + "에요")
#print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요") # 정수형은 str로 감싸 결합해야 한다.
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요") # + 연산자 대신 , 연산자로 결합할 수 있으며, 이 경우 정수형을 str 없이 결합할 수 있다. 단 , 연산자는 한 칸을 띄우고 결합한다.
print(name + "는 어른일까요? " + str(is_adult)) # 불리안형도 str로 감싸 결합해야 한다.

# 주석: 프로그램에 포함되어 있지만, 실제로 실행되지 않는 코드
# #: 한 줄 주석
# '''주석''': 여러 줄 주석

'''
Quiz) 변수를 이용하여 다음 문장을 출력하시오
변수명: station
변수값: "사당", "신도림", "인천공항" 순서대로 입력
출력 문장: XX 행 열차가 들어오고 있습니다.
'''
sentence = "행 열차가 들어오고 있습니다."
station = "사당"
print(station, sentence)
station = "신도림"
print(station, sentence)
station = "인천공항"
print(station, sentence)

print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기 = 2
print(5//3) # 몫 구하기 = 1

print(10 > 3) # 비교 연산자
print(3 == 3)
print(3 + 4 == 7) # True
print(1 != 3)
print(not(1 != 3))
print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True
print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True
print(5 > 4 > 3) # 연속 비교(순차 비교로 결과 도출) = True
print(5 > 4 > 7) # False

print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
print(number)
number += 2 # 18
print(number)
number *= 2 # 36
print(number)
number /= 2 # 18
print(number)
number -= 2 # 16
print(number)
#number %= 2 # 0
number %= 5 # 1
print(number)

print(abs(-5)) # 절대값 5
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import * # math 라이브러리 안의 모든 것 이용
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

from random import *
print(random()) # 0.0 ~ 1.0 미만 범위의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만
print(int(random() * 10)) # 0 ~ 10 미만
print(int(random() * 10) + 1) # 1 ~ 10 이하
print(int(random() * 45) + 1) # 1 ~ 45 이하
print(randrange(1, 46)) # 1 ~ 46 미만 범위의 임의의 값
print(randint(1, 45)) # 1 ~ 45 이하 범위의 임의의 값

'''
Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1: 랜덤으로 날짜를 뽑아야 함
조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건3: 매월 1~3일은 스터디 준비를 해야하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.
'''
print("오프라인 스터디 모임 날짜는 매월", str(randint(4, 28)) + "일로 선정되었습니다.")

sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
""" # 여러 줄의 문자열
print(sentence3)

jumin = "990120-1234567"
print("성별: " + jumin[7])
print("년생: " + jumin[0:2]) # 인덱스 0 부터 2 전까지(0, 1)
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])
# print("생년월일: " + jumin[0:6])
print("생년월일: " + jumin[:6]) # 인덱스 처음부터 6 전까지
# print("뒤 7자리: " + jumin[7:14])
print("뒤 7자리: " + jumin[7:]) # 인덱스 7 부터 끝까지
print("뒤 7자리(뒤에서부터): " + jumin[-7:]) # 인덱스 맨 뒤에서 7번째부터 끝까지