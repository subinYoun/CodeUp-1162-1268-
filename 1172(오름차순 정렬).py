#세 정수 오름차순 출력
a=list(map(int, input().split()))
a.sort()#a를 오름차순 정렬
for i in range(0, 3):
    print(a[i], end=' ')