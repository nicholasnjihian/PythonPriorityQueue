class Node:
    def __init__(self, data, next=None, previous=None, priority):
        self.data = data
        self.next = next
        self.priority = priority
        
    def __repr__(self):
        return f"{self.data}; -> {self.next} ; Priority == {self.priority}"
        
class PriorityQueue:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def is_empty(self):
        if self.length == 0:
            return True
        else:
            return False
    
    def clear(self):
        self.length = 0
        self.head = None
        
       
    
    def insertInQueue(self, content, priority):
       #No node available(even head node none):
       #New Node becomes self.head

        node = Node(content, priority)
        
        if self.head is None:
            self.head = node 
        else:
            #Head node present but no other node present
            
           
            #If there is no node other than head, i.e., head.next is None
            #Compare priority of our new node and the head node
            #Scenario 1:  -> If new node has higher priority, self.head becomes our new node 
            #and the original self.head is pushed to second position in the Queue.
            #Scenario 2:  -> If new node has lower priority, it becomes second in Queue
 
            adjacent_to_head = self.head.next
            if adjacent_to_head is None:
                #Scenario 1
                if self.head.priority > node.priority: #Hence node has higher priority
                    duplicate = self.head
                    self.head  = node
                    self.head.next = duplicate
                #Scenario 2
                else:
                    self.head.next = node
            else:
                # Head node present and in addition one or more other nodes are present:
                # Note: Every time we add a new node to the Queue, the Queue is ordered from 
                # highest priority to lowest.
                
                #Therefore,
                #Scenario 1:->  Our new Node has higher priority, it automatically becomes self.head.
                #Scenario 2: -> 
                #Our new node has lower priority. We need to loop through the Queue to find the appropriate 
                #position for the node given its priority.
                #e.g. if we have a Queue = [1,2,5,7,9] and new node 6, the Queue needs to become [1,2,5,6,7,9].
                
                #Scenario 1:
                if self.head.priority > node.priority: # if node has higher priority
                    duplicate = self.head
                    self.head = node
                    self.head.next = duplicate
                #Scenario 2:
                elif self.head.priority < node.priority: # if node priority is lower than self.head priority
                    last=self.head
                    counter = 1 #We can store the position at which we find a lower priority(higher number) 
                    #e.g 7 in the above example with Queue [1,2,5,7,9], so as to push all the other 
                    #lower priority numbers further back the Queue
                    
                    while last.next:
                        if counter == length:
                            last.next = node
                            break
                        if last.priority > node.priority: #Test if new node has higher priority
                            node.next=last
                            break
                        counter+=1
                        last=last.next  
                        
                    if counter != length:
                        idx_at_which_to_append = counter - 1
                        last=self.head
                        counter = 1
                        while last.next:
                            if counter == idx_at_which_to_append:
                                last.next = node
                else: #self.head.priority is equal to node.priority
                    val = self.head
                    counter = 1
                    while val.next:
                        if val.priority != node.priority:
                            node.next = val
                            break
                        counter += 1
                        val = val.next
                    val = self.head
                    idx_at_which_to_append = counter - 1
                    counter = 1
                    while val.next:
                        if counter == idx_at_which_to_append:
                            val.next = node
                            break
                        counter += 1
                        val = val.next      
        self.length = self.length + 1
        
    
    def removeFromQueue(self):
        content = self.head.data
        self.head = self.head.next
        self.length = self.length - 1
        return content

