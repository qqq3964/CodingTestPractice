from collections import deque

N,W,L = map(int,input().split())
truck = deque(list(map(int,input().split())))
road = [0]*W
time = 0

while truck:
    trucks_weight = sum(road)
    now_truck = truck[0]
    if (trucks_weight + now_truck) <= L:
        road[-1] = truck.popleft()
    # 왼쪽으로 싀프팅
    road = road[1:] + [0]
    # 시간 증가
    time += 1

print(time + W)