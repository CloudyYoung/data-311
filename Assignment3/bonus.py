
from A3 import DoublyLinkedList


class ModifiedDoublyLinkedList(DoublyLinkedList): # Inherite from DLL
    
    class ModifiedNode(DoublyLinkedList.Node): # Inherite from DLL.Node
        def __init__(self, value = None, predecessor = [], successor = []):
            super().__init__(value)
            self.predecessor = predecessor.copy()
            self.successor = successor.copy()

        def printPredecessor(self):
            ret = "";
            for each in self.predecessor:
                ret += str(each.value) + " "
            return ret

        def printSuccessor(self):
            ret = "";
            for each in self.successor:
                ret += str(each.value) + " "
            return ret



    def addFront(self, value):
        add = self.ModifiedNode(value)
        
        if self.head != None:
            # trace back to change predecessor/successor for every ModifiedNode
            for each in self:
                add.successor.append(each)
                each.predecessor.insert(0, add)

        self.head = add
        print(self)

    def removeFront(self):
        if self.head == None or len(self.head.successor) == 0:
            self.head = None
        else:
            self.head = self.head.successor[0]
            for each in self:
                    each.predecessor.pop(0)

        print(self)
            

    def __iter__(self):
        current = self.head
        while current != None:
            yield current
            if len(current.successor) > 0:
                current = current.successor[0]
            else:
                current = None

    def importFromArray(self, arr):
        for each in arr[::-1]: # reversed to keep the order same with the original array
            self.addFront(each)

    def binarysearch(self, value):
        middle = (len(self) - 1) // 2 - 1 # middle index, length of array itself divided by 2 with floor, and exclude self.head itself by minus 1
        rangeN = len(self) // 2 # range number for predecessor/successor for each node
        return self._binarysearch(value, self.head.successor[middle], rangeN, middle + 1) # search
    

    def _binarysearch(self, value, node, rangeN, index):

        print('goal-value', value, 'current-node-value', node, 'node-range', rangeN, 'current-node-index', index)
        
        if node.value == value:
            return index

        if node.value == None or index < 0 or rangeN < 0:
            return -1

        if value < node.value:
            middle = len(node.predecessor) - 1 - ((rangeN - 1) // 2) # middle index of predecessor
            index = index - (len(node.predecessor) - middle) # index in the list
            return self._binarysearch(value, node.predecessor[middle], rangeN // 2, index) # select middle Node from predecessor
        else:
            middle = (rangeN - 1) // 2
            index = index + (middle + 1)
            return self._binarysearch(value, node.successor[middle], rangeN // 2, index) # select middle Node from successor

    

print("-----Modified Doubly Linked List------")

mdll = ModifiedDoublyLinkedList()
mdll.removeFront()
mdll.addFront(1.2)
mdll.addFront(4.28)
mdll.addFront(410.2)
mdll.removeFront()
mdll.removeFront()
mdll.removeFront()



print("-----Binary Search------")

## Random Number Array - for testing
arr10 = [2, 3, 23, 36, 53, 70, 77, 79, 79, 99]
arr20 = [2, 2, 3, 5, 13, 14, 16, 23, 28, 34, 37, 38, 39, 40, 52, 54, 67, 89, 92, 98]
arr100 = [11, 11, 22, 25, 35, 37, 46, 75, 82, 85, 91, 109, 118, 121, 121, 125, 125, 127, 128, 138, 153, 163, 177, 188, 190, 202, 206, 206, 230, 239, 242, 245, 245, 261, 261, 278, 303, 303, 349, 354, 356, 363, 376, 379, 402, 427, 433, 460, 470, 471, 477, 484, 484, 500, 505, 519, 519, 551, 561, 573, 581, 595, 610, 611, 613, 613, 616, 620, 625, 627, 631, 633, 660, 662, 683, 707, 714, 742, 744, 765, 767, 781, 808, 810, 810, 812, 817, 825, 851, 851, 880, 887, 888, 899, 905, 922, 941, 968, 970, 984]

mdll = ModifiedDoublyLinkedList()
mdll.importFromArray(arr10)
index = mdll.binarysearch(99)
print('Value at Index (of Array):', index)
