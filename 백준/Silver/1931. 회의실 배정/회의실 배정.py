import sys
import heapq
N=int(sys.stdin.readline())

heap=[]

for _ in range(0,N):
    start,end=map(int,sys.stdin.readline().split())
    heap.append([end,start])
heapq.heapify(heap)


count=0

last_meeting=0

while heap:
    poped=heapq.heappop(heap)
    start_time,end_time=poped[1],poped[0]
    if start_time>=last_meeting:
        count=count+1
        last_meeting=end_time
    

print(count)