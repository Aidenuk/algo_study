# min heap where the root is the minimum
# max heap where the root is the maximum


def _siftup(self, i):
    parent = (i - 1) // 2
    while i != 0 and self.heap[i] < self.heap[parent]:
        self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
        i = parent
        parent = (i - 1) // 2

def _siftdown(self, i):
    left = 2 * i + 1
    right = 2 * i + 2
    while (left < len(self.heap) and self.heap[i] > self.heap[left]) or (right < len(self.heap) and self.heap[i] > self.heap[right]): 
        smallest = left if (right >= len(self.heap) or self.heap[left] < self.heap[right]) else right
        self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
        i = smallest
        left = 2 * i + 1
        left = 2 * i + 2
        
def extract_min(self):
    if len(self.heap) == 0:
        return None
    minval = self.heap[0]
    self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
    self.heap.pop()
    self._siftdown(0)
    return minval


# update
def update(self, old, new):
    if old in self.heap:
        self.update_by_index(self.heap.index(old), new)


# heapify aka building priority queue
self.heap = arr.copy
for i in range(len(self.heap))[::-1]:
    self._siftdown(i)