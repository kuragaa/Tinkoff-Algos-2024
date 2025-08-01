import sys

class MinHeap:

    def __init__(self, maxsize):

        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -sys.maxsize
        self.MIN = 1


    def parent(self, index):
        return index // 2

    def leftChild(self, index):
        return 2 * index

    def rightChild(self, index):
        return (2 * index) + 1


    def isLeaf(self, index):
        if index >= (self.size // 2) and index <= self.size:
            return True
        return False


    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos], self.Heap[fpos])


    def minHeapify(self, index):
        left = self.leftChild(index)
        right = self.rightChild(index)
        smallest = index

        if left <= self.size and self.Heap[left] < self.Heap[smallest]:
            smallest = left

        if right <= self.size and self.Heap[right] < self.Heap[smallest]:
            smallest = right

        if smallest != index:
            self.swap(index, smallest)
            self.minHeapify(smallest)


    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while (self.Heap[current] < self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)


    def extractMin(self):
        popped = self.Heap[self.MIN]
        self.Heap[self.MIN] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.MIN)
        return popped


n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
heap = MinHeap(n)
for el in arr:
    heap.insert(el)
sorted = []
for _ in range(n):
    sorted.append(heap.extractMin())

print(*sorted)