#계산기
m = input()
m = list(m)
for i in range(0, len(m)): #len(m)은 m의 길이
    if m[i] == '+':
        a = int("".join(m[:i])) #"".join(리스트)는 리스트에서 문자열으로 바꾸는것을 의미한다.
#연산식 자체를 입력으로 받으므로 문자열로 한글자씩 배열에 바다 저장하여 연산자를 기준으로 앞뒤로 슬라이싱하여 계산하는 것이 키포인트!!
#m[:i]는 i이전의 값들을 의미한다.
        b = int("".join(m[i + 1:])) #m[i + 1:]는 i+1이후의 값들을 의미
        print(a + b)
    elif m[i] == '-':
        a = int("".join(m[:i]))
        b = int("".join(m[i + 1:]))
        print(a - b)
    elif m[i] == '*':
        a = int("".join(m[:i]))
        b = int("".join(m[i + 1:]))
        print(a * b)
    elif m[i] == '/':
        a = int("".join(m[:i]))
        b = int("".join(m[i + 1:]))
        print("%.2f" % (a / b))
