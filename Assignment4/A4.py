import random
import heapq


# helper function

def print_tree(n, indent=0):
    if n is None:
        print(" " * indent, "X")
        return
    print_tree(n.right, indent + 4)
    print(" " * indent, n.val)
    print_tree(n.left, indent + 4)


# helper function
def inorder(n):
    if not n:
        return
    yield from inorder(n.left)
    yield n.val
    yield from inorder(n.right)


class BST:

    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, val):
        n = self.Node(val)
        if self.root is None:
            self.root = n
            return
        r = self.root
        while r is not None:
            if val < r.val:
                if r.left is None:
                    r.left = n
                    return
                else:
                    r = r.left
            else:
                if r.right is None:
                    r.right = n
                    return
                else:
                    r = r.right

    def __iter__(self):
        yield from inorder(self.root)

    def print(self):
        print("------- Tree -----------")
        if self.root is None:
            print("Empty tree")
        else:
            print_tree(self.root)
        print("------------------------")

    def remove(self, val):
        if self.root == None:  # base case, if root is none
            return  # not found, not removed

        self.root = self._remove(self.root, val)

    def _remove(self, node, val):
        # print(node.val, val)
        if val < node.val:
            node.left = self._remove(node.left, val)
            return node
        elif val > node.val:
            node.right = self._remove(node.right, val)
            return node
        else:  # found value
            if node.left != None and node.right != None:  # has both children
                successor = self.minimum(node.right)
                node.val = successor.val
                node.right = self._remove(node.right, node.val)
                return node
            elif node.left != None:  # has left child
                return node.left
            elif node.right != None:  # has right child
                return node.right
            else:  # has no child
                return None

    def minimum(self, node):
        current = node
        while(current.left != None):
            current = current.left
        return current


bst = BST()
bst.insert(5)
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(4.5)
bst.insert(6)
bst.remove(5)
bst.remove(4)
bst.remove(3)
bst.remove(2)
bst.remove(4.5)
bst.remove(6)
bst.print()


def _siftup(heap, index):
    while index > 0:
        parentIndex = (index - 1) // 2 # find parent index
        if heap[parentIndex] > heap[index]:
            heap[index], heap[parentIndex] = heap[parentIndex], heap[index]  # swap them
            index = parentIndex
        else:
            return



def _siftdown(heap, index, length = None):
    while True:
        left, right = index * 2 + 1, index * 2 + 2
        if length == None: length = len(heap)

        if right >= length:
            if left >= length:
                return
            elif heap[index] > heap[left]:
                heap[index], heap[left] = heap[left], heap[index]
            return
        else:
            if heap[left] < heap[right]:
                swap = left
            else:
                swap = right

            if heap[index] > heap[swap]:
                heap[index], heap[swap] = heap[swap], heap[index]
                index = swap
            else:
                return


def my_heappush(heap, value):
    heap.append(value)
    _siftup(heap, len(heap) - 1)


def my_heappop(heap):
    heap[0], heap[-1] = heap[-1], heap[0]
    pop = heap.pop()
    _siftdown(heap, 0)
    return pop


def my_heapify(heap):
    for parent in reversed(range(len(heap) // 2)):
        _siftdown(heap, parent)



def my_heapsort(heap):
    my_heapify(heap)
    
    for each in range(len(heap) - 1, -1, -1):
        heap[each], heap[0] = heap[0], heap[each]
        _siftdown(heap, 0, each)

    heap.reverse()


#
# you can use the tests below to verify your implementations are correct
# but do not modify the tests below


def is_heap(heap):
    def parent(i): return (i-1) // 2
    def left(i): return 2 * i + 1
    def right(i): return 2 * i + 2
    for i in range(0, parent(len(heap)-1)):
        if left(i) < len(heap) and heap[i] > heap[left(i)]:
            return False
        if right(i) < len(heap) and heap[i] > heap[right(i)]:
            return False
    return True


def test_my_heappush(n):
    print("Testing my_heappush:")
    a = [random.randint(0, 100) for x in range(n)]
    print("  [I] inserting:", a)
    heap = []
    for i in a:
        my_heappush(heap, i)
    print("  [I] heap:", heap)
    if sorted(heap) != sorted(a):
        print("  [E] incorrect elements in heap after inserting:")
    if not is_heap(heap):
        print("  [E] not a heap after inserting")


def test_my_heappop(n):
    print("Testing my_heappop:")
    a = [random.randint(0, 100) for x in range(n)]
    heapq.heapify(a)
    print("  [I] testing pop on heap:", a)
    heapcopy = a[:]
    true_min = heapq.heappop(heapcopy)
    my_min = my_heappop(a)
    print("  [I] popped item:", my_min)
    print("  [I] resulting heap:", a)
    if true_min != my_min:
        print("  [I] my_heappop returned", my_min)
        print("  [I] but real min is", true_min)
    if sorted(heapcopy) != sorted(a):
        print("  [E] incorrect elements in heap after popping")
    if not is_heap(a):
        print("  [E] not a heap after popping")


def test_my_heapify(n):
    print("Testing my_heapify:")
    a = [random.randint(0, 100) for x in range(n)]
    print("  [I] input array:", a)
    heapcopy = a[:]
    heapq.heapify(heapcopy)
    my_heapify(a)
    print("  [I] heap:", a)
    if sorted(heapcopy) != sorted(a):
        print("  [E] incorrect elements in heap after heapify")
    if not is_heap(a):
        print("  [E] not a heap after heapify")


def test_my_heapsort(n):
    print("Testing my_heapsort")
    a = [random.randint(0, 100) for x in range(n)]
    copy = a[:]
    my_heapsort(a)
    print("  [I] input array:", copy)
    print("  [I] sorted output:", a)
    if sorted(a) != sorted(copy):
        print("  [E] incorrect elements in sorted array")
    if a != sorted(a):
        print("  [E] not sorted")


def test_all(n):
    test_my_heappush(n)
    test_my_heappop(n)
    test_my_heapify(n)
    test_my_heapsort(n)


test_all(9)
