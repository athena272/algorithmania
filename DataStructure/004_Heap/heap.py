import heapq

def line():
    print("=*=" * 20)

heap = [1, 2, 65, 78, 98, 3, 6, 7, 99]

# make a array in a heap
heapq.heapify(heap)
# [1, 2, 3, 7, 98, 65, 6, 78, 99]
print(heap)
line()

# biggest number of heap
biggest = heapq.nlargest(3, heap)
print(biggest)
line()

# smallest number of heap
smallest = heapq.nsmallest(3, heap)
print(smallest)
line()

# push a number int the heap
heapq.heappush(heap, -9)
print(heap)
line()

# small number of heap  
print(heap[0])
line()

# large number of heap
print(heap[-1])
