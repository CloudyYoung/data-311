## DATA 311


class DoublyLinkedList:

    class Node:
        def __init__(self, value, predecessor = None, successor = None):
            self.value = value
            self.predecessor = predecessor
            self.successor = successor

        def __str__(self):
            return str(self.value)

        def __repr__(self):
            return str(self.value)

    def __init__(self): # It has the same functionality as "createDLL"
        self.head = None
        print(self)

    def isEmpty(self):
        if self.head == None:
            return -1
        else:
            return 1

    def addFront(self, value):
        add = self.Node(value, None, self.head)
        
        if self.head != None:
            self.head.predecessor = add
        self.head = add
        print(self)


    def removeFront(self):
        if self.head != None:
            self.head = self.head.successor
        print(self)

    def __iter__(self):
        current = self.head
        while current != None:
            yield current
            current = current.successor

    def __len__(self):
        length = 0
        for each in self:
            length += 1
        return length
        
    def __str__(self):
        string = "";
        for each in self:
            string += str(each.value) + " ⇆ "
        return string + "*"



print("------Doubly Linked List-----")

dll = DoublyLinkedList()

dll.removeFront()

dll.addFront("a")
dll.addFront("b")
dll.addFront("c")

dll.removeFront()
dll.removeFront()
dll.removeFront()

dll.removeFront()



class Stack:

    def __init__(self):  # It has the same functionality as "createStack"
        self.stack = DoublyLinkedList()
        print(self)

    def push(self, val):
        self.stack.addFront(val)

    def pop(self, val = None):
        self.stack.removeFront()
        
    def peek(self):
        if self.stack.head == None:
            return None
        return self.stack.head.value
        
    def __len__(self):
        return len(self.stack)

    def __iter__(self):
        self.stack.__iter__()

    def __str__(self):
        return self.stack.__str__()

print("------Stack-----")

stack = Stack()
stack.pop()
stack.push(111)
stack.push(222)
stack.push(333)
stack.pop()
stack.pop()
stack.pop()
stack.pop()




def _postfixExpression(exp):
    stack = Stack()
    
    for each in exp.split(" "):
        if each == "+" or each == "-" or each == "*" or each == "/": # if it is operator
            value1 = stack.peek()
            stack.pop()
            value2 = stack.peek()
            stack.pop()
            if value1 == None or value2 == None:
                return False
            result = eval(str(value2) + each + str(value1)) # calculate the expression
            stack.push(result)
        elif each != "" and each.isnumeric(): # if it is a number
            stack.push(each)
        else: # invalid character
            return False


    if len(stack) != 1: # if there are more than one value left at the stack as final result
        return False
    return stack.peek()

def postfixExpression(exp):
    result = _postfixExpression(exp)
    if result == False:
        print("User input is not a valid postfix expression")
    else :
        print(result)
            
            

print("------Postfix Expression-----")
    
postfixExpression("1 2 3 4 - * +")
postfixExpression("3 2 * -")


