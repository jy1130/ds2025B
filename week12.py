from collections import deque

d = deque([3, -9, 14])
d.append(77)
#d.appendleft(100) #빠져나가는 deque 방향에서 집어넣는 것 . 출력하면 100이 먼저 출력됨 .
d.append(91)
for i in range(len(d)):
    print(d.popleft())
