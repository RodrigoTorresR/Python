class LinkedStack:
    """LIFO Stack implementation usign a singly linked list for storage"""
    #---------- nested _Node class-----------
    class _Node:
        """Lightweight nonpublic class for storing a singly linked node"""
        __slots__='_element','_next'    #streamline memory usage
        def __init__(self, element, next):  #initializa node's fields
            slef.__element = element    #reference to user's element
            self.__next = next          #reference to next node
    #----------Stack Methods---------
    def __init__(self):
        """Create an empty stack. """
        self._head = None   #reference to the head node
        slef._size = 0      #number of stack elements
    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size
    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0
    def push(self, e):
        """Add element e to the top of the stack"""
        self._head = self._Node(e, self._head)  #create and link a new node
        self._size += 1
    def top(self):
        """Return (but not remove) the element at the top of the stack
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element  #top of stack is at head of list
    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO)
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answerd = self._head._element
        self._head = self._head._next   #bypass the former top node
        self._size -= 1
        return answer

