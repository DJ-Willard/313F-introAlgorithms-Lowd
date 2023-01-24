import copy
class IsEmptyError(Exception):
    pass

class Node(object):
    """
    A class to represent a node.

    ...

    Attributes
    ----------
    #data : int or float
        An individual character or number to be stored in a node
    #next_node : object of class Node
        A pointer to the next node in a stack or queue

    Methods
    -------
    setData(data):
        Updates the value of data attribute of Node
    setNext(next_node):
        Updates the value of next_node attribute of Node
    getData():
        Returns the value of data attribute
    getNext():
        Returns the value of next_node attribute
    """
    def __init__(self, data = None, next_node = None):
        """
        Constructs (or initializes) the attributes for an object of the class

        ...

        Parameters
        ----------
        data : int or float
            An individual character or number to be stored in a node
        next_node : object of class Node
            A pointer to the next node in a stack or queue

        """
        self.__data = data
        self.__next_node = next_node

    def setData(self, data):
        '''Set the "data" data field to the corresponding input.'''
        self.__data = data
        return

    def setNext(self, next_node):
        '''Set the "next_node" data field to the corresponding input.'''
        self.__next_node = next_node
        return

    def getData(self):
        '''Return the "data" data field.'''
        return self.__data

    def getNext(self):
        '''Return the "next_node" data field.'''
        return self.__next_node

class Queue(object):
    """Provide class dosctring"""
    def __init__(self):
        self.__head = None
        self.__tail = None

    def __str__(self):
        '''Loop through your queue and print each Node's data.'''
        head = self.__head
        if head == None:
            return None
        result = "["
        while head != None:
            result += str(head.getData()) + ", "
            head = head.getNext()
        return result[:-2] + "]"



    def enqueue(self, newData):
        '''Create a new node whose data is newData and whose next node is null
        Update head and tail.'''
        # Hint: Think about what's different for the first node added to the Queue
        #if first, set head and tail to the new node.
        nxtnode = Node(newData, None)
        if self.isEmpty():
            self.__head = nxtnode
        else:
            self.__tail.setNext(nxtnode)
        #if not set current node tail to nxtnode and self tail to nxtnode
        self.__tail = nxtnode

    def dequeue(self):
        '''Return the head of the Queue
        Update head.'''
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue
        # Hint: Return the element(data) that is dequeued.
        if self.isEmpty():
            raise IsEmptyError('Empty queue cannot DeQueue')
        DQnode = self.__head.getData()
        #if the tail and  head are the same after dequeue set to empty
        if self.isEmpty():
            self.__tail = None
            self.__head = None
        else:
            self.__head = self.__head.getNext()
        return DQnode

    def isEmpty(self):
        '''Check if the Queue is empty.'''
        if self.__head == None:
            return True
        else:
            return False


class Stack(object):
    """Provide class dosctring"""
    def __init__(self):
        ''' We want to initialize our Stack to be empty.
        (ie) Set top as null'''
        self.__head = None
        self.__tail = None

    def __str__(self):
        '''Loop through your stack and print each Node's data.'''
        head = self.__head
        if head == None:
            return None
        result = "["
        while head != None:
            result += str(head.getData()) + ", "
            head = head.getNext()
        return result[:-2] + "]"

    def push(self, newData):
        '''We want to create a node whose data is newData and next node is top.
        Push this new node onto the stack
        Update top'''
        # if first head gets node else set cureent node to next head is newnode
        self.__head = Node(newData, self.__head)

    def pop(self):
        ''' Return the Node that currently represents the top of the stack.
        Update top'''
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #         to hold important information
        # Hint: Return null on a empty stack
        # Hint: Return the element(data) that is popped
        if self.isEmpty():
            #auto grader said no raise AttributeError("AttributeError: Cannot pop stack with no pop")
            #and to raise IsEmptyError(stack is empty)
            return None
        #removes head and makes next head
        #store current in tmp set next return tmp
        removed = self.__head
        self.__head = self.__head.getNext()
        return removed.getData()

    def isEmpty(self):
        '''Check if the Stack is empty.'''
        if self.__head == None:
            return True
        else:
            return False

def isPalindrome(s):
    '''Use your Queue and Stack class to test wheather an input is a palindrome.'''
    myStack = Stack()
    myQueue = Queue()
    status = True
    #strip spaces
    s = s.replace(" ","")
    print(s)
    for c in s:
        myStack.push(c)
        myQueue.enqueue(c)
    ## Helper function ## just call str
    print("Stack data: : " + myStack.__str__())
    print("Queue data: " + myQueue.__str__())
    while not myStack.isEmpty():
        p = str.lower(myStack.pop())
        q = str.lower(myQueue.dequeue())
        print("Dequeue: " + q)
        print("StackPop: " + p)
        if p != q:
            status = False
    # Return appropriate value
    print(s+": Palindrome? " + str(status))
    return status

class TwoStackQueue(object):
    """Provide class dosctring"""
    def __init__(self):
        self.stk1 = Stack()
        self.stk2 = Stack()

    def __str__(self):
        '''Loop through your queue and print each Node's data.'''
        # this can mutate so copy so i can loop though stack without distroy stucture and keep speed
        p = copy.copy(self.stk1)
        if p.isEmpty():
            return None
        result = "["
        while not p.isEmpty():
            result += str(p.pop()) + ", "
        return result[:-2] + "]"

    def enqueue(self, newData):
        '''while stk1 not emtpy pop stack1  to push to stack2
        then push  newdata to stack one then push everthing back '''
        while not self.stk1.isEmpty():
            self.stk2.push(self.stk1.pop())
        self.stk1.push((newData))

        while not self.stk2.isEmpty():
            self.stk1.push(self.stk2.pop())

    def dequeue(self):
        '''if stack1 isemtpy IsEmpty error, otherwise
        pop form stk1  and return it to dequeue'''
        if self.stk1.isEmpty():
            #raise IsEmptyError("TwoStackQueue is emtpy!!!") auto grader said no
            None
        dq = self.stk1.pop()
        return dq

    def isEmpty(self):
        '''Check if the Queue is empty.'''
        if self.stk1.isEmpty() and self.stk2.isEmpty():
            return True
        else:
            return False

def isPalindromeEC(s):
    '''Implement if you wish to do the extra credit.'''
    ms = Stack()
    tsq = TwoStackQueue()
    status = True
    # strip spaces
    s = s.replace(" ", "")
    print(s)
    for c in s:
        ms.push(c)
        tsq.enqueue(c)
    ## Helper function ## just call str
    print("Stack data: : " + ms.__str__())
    print("TSQueue data: " + tsq.__str__())
    while not ms.isEmpty():
        p = str.lower(ms.pop())
        q = str.lower(tsq.dequeue())
        print("TSDequeue: " + q)
        print("StackPop: " + p)
        if p != q:
            status = False
    # Return appropriate value
    print(s + ": Palindrome? " + str(status))
    return status





if __name__ == '__main__':
    """q = Queue()
    print("Queue : " + str(q.__str__()))
    q.enqueue(10)
    print("Queue : " + str(q.__str__()))
    q.enqueue(20)
    print("Queue : " + str(q.__str__()))
    q.dequeue()
    print("Queue : " + str(q.__str__()))
    q.dequeue()
    print("Queue : " + str(q.__str__()))
    s = Stack()
    print("Stack : " + str(s.__str__()))
    s.push(10)
    print("Stack : " + str(s.__str__()))
    s.push(20)
    print("Stack : " + str(s.__str__()))
    s = Stack()
    s.pop()
    print("Stack : " + str(s.__str__()))
    s.pop()
    print("Stack : " + str(s.__str__()))"""
    print(isPalindromeEC("TaCo CaT"))




