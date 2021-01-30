#두 알파벳 사이의 모든 알파벳 출력
a, b=input().split()
for i in range(ord(a), ord(b)+1): #ord(문자):문자의 아스키코드(숫자) 변환
    print(chr(i), end=" ") # chr(숫자):숫자의 아스키 코드(문자로) 변환