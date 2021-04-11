# 1. list
list = []

list = [1, 'abc', 4.5]

list.append(3)
list[3] = 4

list[:1]
list[3:7]

# 2. dict
dict = {}

from collections import defaultdict
dict = defaultdict(int)

dict['name'] = 'Jennifer'

# 3. stack 
stack = []

# heap - priority queue
import heapq

heap = [5, 4, 2, 1]

heapq.heapify(heap)

heapq.heappush(heap, 3)

heapq.heappop(heap) # smallest element

heapq.heappushpop(heap, 0) # first push then pop, returns 0 itself, more efficient

heapq.heapreplace(heap, 0) # first pop then push, returns 1

heapq.nlargest(3, heap)
heapq.nsmallest(3, heap)

heap[0] # top