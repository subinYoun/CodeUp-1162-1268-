#사주보기 (년-월+일)의 마지막 숫자가 0이면 "대박" 아니면 "그럭저럭"출력
a, b, c=map(int, input().split())
r=a-b+c
if int(r)%10==0:#int(r)%10은 정수 r의 마지막 숫자
    print("대박")
else:
    print("그럭저럭")