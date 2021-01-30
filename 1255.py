#두 실수 사이의 수를 0.01 간격으로 오름차순 출력하기
a, b=map(float, input().split())
while(a<=b): #for로 하니까 안됬었음 이유찾기
    print("%.2f" %a, end=" ")
    a+=0.01