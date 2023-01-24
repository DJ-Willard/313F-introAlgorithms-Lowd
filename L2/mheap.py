class max_heap(object):
    """Binary max-heap

    Supports most standard heap operations (insert, peek, extract_max).
    Can be used for building a priority queue or heapsort. Since Python
    doesn't have built-in arrays, the underlying implementation uses a
    Python list instead. When initialized, max_heap creates a new list of
    fixed size or uses an existing list.

    Attributes
    ----------
    __str__(self):
        print array with the parent child structure
    leaf(self,p):
        return true if node is leaf else return false
    insert(self, data):
        inserts value into array at the tail to recursiving swaps nodes till the inserted node is in the correct placement.
    peek(self):
        return current max value of heap at heap[0]
    extract_max(self):
        Returns max value which is the parent and decement lenght heap array
    __heapify(self, curr_index, list_length = None):
        recusive fuction the swaps if child is larger the parent and apples to the correct Right left placement to keep properties of heap
        update the values in the "array" to the correct postion based off size
    build_heap(self):
        builds a max heap form a list input. done by calling heapify on list l.
        get_heap(self):
            returns current heap

    Helper Methods
    --------------
    __get_parent(self, loc):
        returns parent of node
    __get_left(self, loc):
        returns the right child for current node
    __get_right(self, loc):
        returns the left child for the current node
    __swap(self, a, b):
        swaps node a and node b in heap.
    ort_insert(self, data):
        put the current max into the last value

    Outside of class
    ----------------
    heap_sort(l):
        calls build_heap(self) to sort an input list and formats the list into a max heap.
        then extacts maxium for inplace swaping to put list in asending order.

    """

    def __init__(self, size = 20, data = None):
        """Initialize a binary max-heap.

        size: Total capacity of the heap.
        data: List containing the desired heap contents. 
              The list is used in-place, not copied, so its contents 
              will be modified by heap operations.
              If data is specified, then the size field is ignored."""

        # Add to this constructor as needed
        if data is not None:
            self.max_size = len(data)
            self.length = len(data)
            self.heap = data
        else:
            self.max_size = size
            self.length = 0
            self.heap = [None] * size

    def __str__(self):
    #print the heap sperate root and children in printing
        p = self.heap
        n = self.max_size
        result = "["
        for i in range(n):
            result += str(p[i]) +"|"
        return result[:-1] + "]"
    def get_heap(self):
        return self.heap

    # bool that returns true if postion p is a leaf false otherwise.
    def leaf(self, p):
        if p >= self.length//2 and p <= self.length:
            return True
        return False

    def insert(self, data):
        """Insert an element into the heap.
         Raises IndexError if the heap is full."""
        # Tips : insert 'data' at the end of the list initially
        #      : swap with its parent until the parent is larger or you 
        #      : reach the root
        # error here
        if self.length >= self.max_size:
            raise IndexError('Heap is full')

        #first element input
        if(self.length == 0):
            self.heap[0] = data
            self.length += 1
        else:
            self.heap[self.length] = data
            self.length += 1

        current = self.length - 1
        parent = self.__get_parent(current)
        while (self.heap[current] and self.heap[parent] and current != 0 and self.heap[current] > self.heap[parent]):
            self.__swap(current, parent)
            current = parent
            parent = self.__get_parent(current)

    def peek(self):
        """Return the maximum value in the heap."""
        value = self.heap[0]
        return value


    def extract_max(self):
        """Remove and return the maximum value in the heap.
         Raises KeyError if the heap is empty."""
        # Tips: Maximum element is first element of the list
        #     : swap first element with the last element of the list.
        #     : Remove that last element from the list and return it.
        #     : call __heapify to fix the heap
        #error if empty
        if self.length == 0:
            raise KeyError("Cannot extract max form emtpy Heap")

        value = self.heap[0]
        #first last swap
        self.heap[0] = self.heap[self.length -1]
        #remove value
        self.heap[self.length - 1] = None
        #remove last value
        self.length -= 1
        #call heapify
        self.__heapify(0, self.length)
        return value

    def __heapify(self, curr_index, list_length = None):
        # helper function for moving elements down in the heap
        # Page 157 of CLRS book // actully 162
        #recusive fuction the swaps if child is larger the parent and apples to the coreect Right left placement to keep properties of heap
        #form book
        left = self.__get_left(curr_index)
        right = self.__get_right(curr_index)

        size = list_length
        if left <= size -1 and self.heap[left] > self.heap[curr_index]:
            largest = left
        else:
            largest = curr_index

        if right <= size -1 and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != curr_index:
            self.__swap(curr_index, largest)
            self.__heapify(largest, self.length)

    def build_heap(self):
        # builds max heap from the list l. done by calling heapify
        # Tip: call __heapify() to build to the list
        #    : Page 157 of CLRS book // 164 actully
        for i in range(self.length//2, -1, -1):
            self.__heapify(i, self.length)

    ''' Optional helper methods may be used if required '''
    ''' You may create your own helper methods as required.'''
    ''' But do not modify the function definitions of any of the above methods'''

    def __get_parent(self, loc):
        # left child has odd location index
        # right child has even location index
        if loc % 2 == 0:
            parent = int((loc - 2) / 2)
        else:
            parent = int((loc - 1) / 2)
        return parent

    def __get_left(self, loc):
        return 2*loc + 1

    def __get_right(self, loc):
        return 2*loc + 2

    def __swap(self, a, b):
        # swap elements located at indexes a and b of the heap
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp


def heap_sort(l):
    """Sort a list in place using heapsort."""
    # Note: the heap sort function is outside the class
    #     : The sorted list should be in ascending order
    # Tips: Initialize a heap using the provided list
    #     : Use build_heap() to turn the list into a valid heap
    #     : Repeatedly extract the maximum and place it at the end of the list
    #     : Refer page 161 acutlly (167) in the CLRS textbook for the exact procedure
    n = len(l)
    heap_sorted = max_heap(n,l)
    heap_sorted.build_heap()
    while heap_sorted.length > 0:
        l[heap_sorted.length] = heap_sorted.extract_max()
    return l

"""
Helpers for debuging code:
        Sequoia
        Sam
        Bella
        Lynette
The book was unhelpful internet was more helpful. The plus one errors killed me.
The key vs value was main isssue I wish the book was more clear on the key vs value.
worked for 73 hours now needed people to help debugg. very tired i hope this is satifactory.
        
"""