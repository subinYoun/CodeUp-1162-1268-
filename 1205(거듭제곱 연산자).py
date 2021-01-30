#두수를 더하거나 빼거나 곱하거나 나누거나 제곱을 해서 가장 큰 수를 출력
a, b=map(int, input().split())
c=a+b
d=a-b
i=b-a
e=a*b
g=a/b
j=b/a
h=a**b #파이썬에서의 거듭제곱 표현:a^b를 의미
k=b**a
print("%.6f" %(max(c, d, e, g, h, i, j, k)))