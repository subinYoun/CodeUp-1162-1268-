#만능 휴지통(10의 자릿수 1의 자릿수 서로 바꿔서 2를 곱해준 값이 50넘으면 OH MY GOD
a=int(input())
r=(((a%10)*10)+(a//10))*2
if r>=100:#10의 자릿수 1의 자릿수 서로 바꿔서 2를 곱해준 값이 100을 넘게되면 100을 뺀 값으로 판단
    print("%d" %(r-100))
    if r-100 <= 50:
        print("GOOD")
    else:
        print("OH MY GOD")
else:
    print("%d" %r)
    if r <= 50:
        print("GOOD")
    else:
        print("OH MY GOD")
