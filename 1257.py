#두 수 사이의 홀수 출력하기
a, b=map(int,input().split())
while a<=b:
    if a==b: #두 수가 같을 경우에도 생각해줘야함
        if (a%2)==0:
            print()
            break #break해주지 않으면 무한루프 발생
        else:
            print(a)
            break
    else:
        if (a%2)==0:
            print(a+1, end=" ")
            a+=2
        else:
            print(a, end=" ")
            a+=2
