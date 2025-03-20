import DoublyLinkedList._DoublyLinkedBase
class LinkedDeque(_DoublyLinkedBase):   #note the use of inheritance
    """Double-ended queue implementation based on a dobuly linked list"""
    def first(self):
        """Return (but not remove) the element at the front of the dequeue"""
        if self.is_empty(): raise Empty("Dequeue is empty")
        return self._header._next._element  #real item just after header
    def last(self):
        """Return (but not remove) the elementat the back of the deque"""
        if self.is_empty():
            raise Empty("Dequeue is empty")
        return self._trailer._prev._element #real tiem just before trailer
    def insert_first(self, e):
        """Add an element to the front of the dequeue"""
        self._insert_between(e, self._header, self._header._next) #after header
    def insert_last(self, e):
        """Add an element to the back of the dequeue"""
        self._insert_between(e, self._trailer._prev, self._trailer) #before trailer
    def delete_fisrt(self):
        """Remove and return the element from the front of the dequeue
        Raise Empty exception if the dequeue is empty

        """
        if self.is_empty():
            raise Empty("Dequeue is empty""")
        return self._delete_node(self._header._next)    #use inherited method
    def delete_last(self):
        """Remove and return the element from the back of the dequeue
        Raise Empty exception if the dequeue is empty
        """
        if self.is_empty():
            raise Empty("Dequeue is empty")
        return self._delete_node(self._trailer._prev)   #use inherited method

        
