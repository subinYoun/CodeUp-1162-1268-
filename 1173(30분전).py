#30분 전 시간 출력하기(if 사용)
a, b=map(int,input().split())
if b<30:
    if a==0:#시간이 0일 경우도 생각
        print("%d %d" %(23, 60-(30-b)))
    else:
        print("%d %d" %(a-1, 60-(30-b)))
else:
    if a==0:
        print("%d %d" %(a, b-30))
    else:
        print("%d %d" %(a, b-30))
