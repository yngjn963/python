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

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) # 시작위치 지정
print(python.find("Python"))
print(python.find("Java")) # -1
# print(python.index("Python")) # ValueError. 이후 프로그램을 실행하지 않고 종료.
print(python.count("n")) # n 개수

print("a" + "b")
print("a", "b")
# 방법 1
print("나는 %d살입니다." % 20) # d: 정수
print("나는 %s을 좋아해요." % "파이썬") # s: 문자열
print("Apple은 %c로 시작해요." % "A") # c: 문자
print("나는 %s살입니다." % 20) # s: 정수, 문자열, 문자 모두 가능
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

# 방법 4(파이썬 버전 3.6 이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출문자
# \n: 줄바꿈
# print("백문이 불여일견
#        백견이 불여일타")
print("백문이 불여일견\n백견이 불여일타")

# \", \': 문장 내에서 따옴표
# print("저는 "나도코딩"입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")

# \\: 문장 내에서 \
# print("C:\Python311\python.exe")
print("C:\\Python311\\python.exe")

# \r: 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple

# \b: 백 스페이스
print("Redd\bApple") # RedApple

# \t: 탭
print("Red\tApple") # Red     Apple

'''
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙1: http:// 부분은 제외 => naver.com
규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3: 남은 글자 중 처음 세자리(nav) + 글자 개수(5) + 글자 내 'e' 개수 + "!"로 구성

(출력문 예제)
생성된 비밀번호: nav51!
'''
site = "http://naver.com"
# print(site.index("/"))
# print(site.index("/") + 1)
# print(site.index("/", site.index("/") + 1))
# print(site[site.index("/", site.index("/") + 1) + 1:])
# print(site.index("http://") + 7)
# print(site[site.index("http://") + 7:site.index(".com")])
# print(site[site.index("http://") + 7:site.index(".com")][0:3])
pw = site[site.index("http://") + 7:site.index(".com")] # .com이 아닌 다른 사이트 경우를 생각하면 수정 필요
print(f"생성된 비밀번호: {pw[0:3]}{len(pw)}{pw.count('e')}!")

# 리스트: 순서를 가지는 집합 객체
# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)
# 조세호는 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 다음 정류장에서 하하가 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈이 유재석과 조세호 사이 칸에 탐
subway.insert(1, "정형돈")
print(subway)

# 마지막 칸부터 내림
print(subway.pop()) # 내린 사람
print(subway) # 내리고 지하철에 남은 사람
# print(subway.pop()) # 내린 사람
# print(subway) # 내리고 지하철에 남은 사람
# print(subway.pop()) # 내린 사람
# print(subway) # 내리고 지하철에 남은 사람

# 같은 이름의 사람이 몇 명 있는지 확인하기
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬하기
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 역으로 정렬하기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 서로 다른 자료형을 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장(리스트 합치기)
num_list = [5,2,4,3,1]
num_list.extend(mix_list)
print(num_list)

# 사전
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
# print(cabinet[5]) # 오류로 프로그램 종료
print(cabinet.get(5)) # 오류가 아닌 None 으로 출력
print(cabinet.get(5, "사용 가능")) # 해당 Key가 없을 경우 None 값 대신 사용 가능이라는 값을 반환
print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국" # A-3에 대한 값 변경
cabinet["C-20"] = "조세호"
print(cabinet)

# 떠난 손님(손님 지우기)
del cabinet["A-3"]
print(cabinet)

# 사용 중인 Key
print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])

# 사용 중인 Value
print(cabinet.values()) # dict_values(['김태호', '조세호'])

# 사용 중인 Key, Value 쌍
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 캐비넷 모두 비우기
cabinet.clear()
print(cabinet) # {}


# 튜플: 변경할 수 없지만 성능이 좋다.
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # 오류

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩") # 서로 다른 변수를 한 번에 선언
print(name, age, hobby)


# 집합(Set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) # {1,2,3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합(java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합(java를 할 수 있거나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python)) # {'김태호', '양세형', '유재석', '박명수'} - 순서 상관없음

# 차집합(java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python을 할 줄 아는 개발자가 늘어남
python.add("김태호")
print(python)

# java를 까먹음
java.remove("김태호")
print(java)


# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # {'우유', '주스', '커피'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) # ['우유', '주스', '커피'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # ('우유', '주스', '커피') <class 'tuple'>

menu = set(menu)
print(menu, type(menu)) # {'우유', '주스', '커피'} <class 'set'>

'''
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
첨석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
조건2: 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
조건3: random 모듈의 shuffle과 sample을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자: 1
커피 당첨자: [2, 3, 4]
-- 축하합니다 --

(활용 예제)
from random import *
1st = [1,2,3,4,5]
print(1st)
shuffle(1st)
print(1st)
print(sample(1st, 1))
'''

from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))

users = range(1, 21) # 1부터 20까지 숫자 생성
# print(type(users)) # <class 'set'>
users = list(users)
# print(type(users)) # <class 'list'>

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 1명은 치킨, 3명은 커피

print("-- 당첨자 발표 --")
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))
print("-- 축하합니다 --")

# weather = input("오늘 날씨는 어때요? ")
# # if 조건:
# #     실행 명령문
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

temp = int(input("기온은 어때요? "))
if temp >= 30:
    print("너무 더워요. 나가지 마세요")
elif temp < 30 and temp >= 10:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")