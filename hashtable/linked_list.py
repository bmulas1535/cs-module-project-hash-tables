import numpy as np

class ListNode:
    """Node that contains a value"""
    def __init__(self, value, last_node=None, next_node=None):

        self.value = value
        self.last_node = last_node
        self.next_node = next_node
        return None

    def get_value(self):
        return self.value

    def get_prev(self):
        return self.last_node

    def get_next(self):
        return self.next_node

    def set_prev(self, data):
        self.last_node = data
        return None

    def set_next(self, data):
        self.next_node = data
        return None


class LinkedList:
    """Class for linked list data structure"""
    def __init__(self, head=None, tail=None):
        # Initiate with empy head and tail
        self.head = head
        self.tail = tail
        return None

    def add_to_tail(self, data):
        """It puts the new on at the end."""
        # Put data at the end of the linked list
        node = ListNode(data)
        try:
            # Link tail to next node
            self.tail.set_next(node)
            # Set previous
            node.set_prev(self.tail)
            # Move tail pointer up to new node
            self.tail = node
        except:
            # The LL is empty, assign both head and tail
            self.tail = node
            self.head = node
        return None

    def add_to_head(self, data):
        """Put in a new node at the head and transition head pointer."""
        new_node = ListNode(data)
        try:
            # Assign current head as next in list
            new_node.set_next(self.head)
            # Register the new node as the previous for the current head
            self.head.set_prev(new_node)
            # Reassign head to the new node
            self.head = new_node
        except:
            # The LL is empty, assign both head and tail
            self.head = new_node
            self.tail = new_node
        return None

    def remove_tail(self):
        """Cut and return the last node in the list."""
        # Assuming that there is a tail...
        try:
            value = self.tail.get_value()

            if self.tail.get_prev() is None:
                # This is the only value
                self.head = None
                self.tail = None
            else:
                # Move the tail pointer back to previous
                self.tail = self.tail.get_prev()
            # Send out the node value
            return value

        except:
            # There is nothing in the list
            # Do nothing.
            return None


    def remove_head(self):
        """Take the top value out."""
        # Work on the assumption that there is a head value
        try:
            # Assign the value for the current head node
            value = self.head.get_value()

            if not self.head.get_next():
                # Head is the only value (and therefore also the tail)
                # Remove the head and tail pointers
                self.head = None
                self.tail = None
            else:
                # Reassign head to the next node in the list
                self.head = self.head.get_next()
            # Send out the node value
            return value

        except:
            # There is nothing in the list
            # Do nothing.
            return None

    def get_max(self):
        """Iterate through entire LinkedList and return the largest
        numeric value.
        """
        try:
            # Establish a locator for a iterator
            current = self.head
            # Hold the largest encountered value (negative infinity)
            max_value = -1 * np.inf

            while current:
                value = current.get_value()
                if value > max_value:
                    max_value = value
                current = current.get_next()

            return max_value

        except:
            print('The list is empty.')

    def contains(self, user_value):
        """Check if a value is contained within the linked list."""
        try:
            # Establish a locator for the iterator
            current = self.head
            # Default will be false. This will update if the
            # user_value is encountered in the list.
            is_contained = False
            while current:
                value = current.get_value()
                if value == user_value:
                    is_contained = True
                current = current.get_next()

            return is_contained

        except:
            print('The list is empty.')