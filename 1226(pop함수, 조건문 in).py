#로또 당첨 결과
a = list(map(int, input().split()))
h = list(map(int, input().split()))
bonus = a.pop() #pop함수는 인자가 없을 경우 마지막 인덱스의 값을 리턴하고 삭제한다. 따라서 a.pop()은 마지막 인자를 뜻한다.
count = 0

for i in a:
    if i in h:#조건문에서 i in h는 i가 h에 있을 경우를 뜻한다.
        count += 1

if count == 6:
    print(1)
elif count == 5 and bonus in h:
    print(2)
elif count == 5:
    print(3)
elif count == 4:
    print(4)
elif count == 3:
    print(5)
else:
    print(0)
