#최소힙
import heapq
heap=list()

while True:
    n=int(input())
    if n==-1:
        break
    else:
        if n==0:
            if heap:
                print(heapq.heappop(heap))
                #가장 작은 수를 뽑고 자동으로 오름 차순 정렬됨
            else:
                print(-1)
        else: 
            heapq.heappush(heap,n)
            

# 최대힙
heap=list()

while True:
    n=int(input())
    if n==-1:
        break
    else:
        if n==0:
            if heap:
                print(heapq.heappop(heap)*-1)
                #-를 붙여서 가장 큰수를 구해낸다
            else:
                print(-1)
        else: 
            heapq.heappush(heap,-n)
            