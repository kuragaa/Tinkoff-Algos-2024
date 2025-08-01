import sys

class MaxHeap:

    def __init__(self, maxsize):

        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.MAX = 1


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


    def maxHeapify(self, index):
        left = self.leftChild(index)
        right = self.rightChild(index)
        largest = index

        if left <= self.size and self.Heap[left] > self.Heap[largest]:
            largest = left

        if right <= self.size and self.Heap[right] > self.Heap[largest]:
            largest = right

        if largest != index:
            self.swap(index, largest)
            self.maxHeapify(largest)


    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while (self.Heap[current] > self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)


    def extractMax(self):
        popped = self.Heap[self.MAX]
        self.Heap[self.MAX] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.MAX)
        return popped


n = int(sys.stdin.readline().strip())
heap = MaxHeap(n)
for _ in range(n):
    op = list(map(int, sys.stdin.readline().split()))
    if op[0] == 0:
        heap.insert(op[1])
    else:
        print(heap.extractMax())