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