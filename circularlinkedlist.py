class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircularLinkedList(object):
    
    def __init__(self):
        self.head = None
        self.tail = self.head
        
    def add_node(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head

        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.tail.next = self.head

        
    def remove_node(self, index):
        prev = None
        node = self.head
        i = 0
        
        while i < index:
            prev = node
            node = node.next
            i += 1
            
        if prev == None:
            self.head = node.next
            self.tail.next = self.head
        else:
            prev.next = node.next
            if self.tail == node:
                self.tail = prev
                
    def get_list_length(self):
        """
            the list's length is define as the unique nodes linked together, even though its a circular list,
            it doesn't go on to continue counting the loop
            e.g. a circular list with letters a->b->c...y->z and z pointing back to a has a length of 26
        """
        if self.head == None:
            return 0
        else: 
            i = 1
            node = self.head
            while node != self.tail:
                node = node.next
                i += 1
            return i
            
    def get_node_position_by_data(self, data):
        node = self.head
        i = 0
        while i < self.get_list_length():
            if data == node.data:
                return i
            else:
                node = node.next
                i += 1
                
        ## if it comes here, means data doesn't match any node
        return -1
        
    def get_node_data_by_traversing_from(self, index_of_start_node, number_of_moves):
        """
            Takes the index of the node to start traversing from and move next the number of times specified with number_of_moves
        """
        start_node = self.head
        i = 0
        while i < self.get_list_length():
            if i == index_of_start_node:
                break
            else:
                start_node = start_node.next
                i += 1
                
        i = 0
        while i < number_of_moves:
            start_node = start_node.next
            i += 1
            
        return start_node.data
        
    def print_list(self):
        res = ""
        node = self.head
        while True:
            res += node.data
            res += "->"
            if node != self.tail:
                node = node.next
            else:
                ## to signify a circular link
                res += "[]"
                break
                
        print res