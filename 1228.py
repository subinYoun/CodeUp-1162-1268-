#비만도 측정
a, b=map(float, input().split()) #실제 키, 몸무게 #실수 형태로 바꿔주지 않으면 출력되지 않음
c=(a-100)*0.9 #표준 몸무게
d=(b-c)*100/c #비만도
if d <=10:
    print("정상")
elif 10 < d <= 20:
    print("과체중")
else:
    print("비만")