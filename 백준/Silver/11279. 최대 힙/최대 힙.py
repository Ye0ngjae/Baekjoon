import heapq
import sys

heap = []

N = int(sys.stdin.readline().strip())

for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-x, x))

