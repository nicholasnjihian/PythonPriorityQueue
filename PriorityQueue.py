class Node:
    def __init__(self, data, next=None, previous=None, priority):
        self.data = data
        self.next = next
        self.previous = previous
        self.priority = priority
        
    def __repr__(self):
        return self.data
        
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
        
       
    
    def insertInQueue(self, content, priority):
        #Create a Node with content and priority values
        node = Node(content, priority)
        
        #If there is no node, not even head, we initialize our head with the node we created above
        if self.head is None:
            self.head = node
            
        #If there is at least one node
        else:
            #If there is no node other than head, i.e., head.next is None
            if self.head.next is None:
                #If the head node has a lower priority e.g. 5 than the created node's priority e.g 1,
                #we need to move the head to node.next
                if self.head.next.priority > node.priority:
                    self.head.next = self.head
                    self.head  = node
                else:
                    
                    #If the new created node's priority is lower than the self.head's priority
                    #push the new node to the end of the PriorityQueue
                    self.head.next = node
                    self.head.next.previous = self.head
                    
            #If there are other nodes or there is another node, other than self.head
            #we need to compare the priorities again
            #If the newly created node's priority is higher(for instance a value such as 1),
            #we need to push every other node with a lower priority to the back of the queue, 
            #further back to give space to the new node.
            #If the created node's priority is lower it will be moved further back up to where no other node 
            #before it has a lower priority. So if we have a new node with priority 3 and a Queue with priorities
            #[1,2,6,8], the Queue will become [1,2,3,6,8].
            else:
                last = self.head
                
                #Loop for so long as the priority of the created node is higher(a lower value is higher)
                # and push nodes with lower priority further bact the Queue
                while last.priority > node.priority:
                    
                    #loop to the end of the Queue
                    #We then create a new node at the Queue's end 
                    #and then copy the last existing node to this new node
                    while last.next:
                        last=last.next
                    last.next = last
                    
                    #Now loop back to the head shifting the nodes to the back
                    #[self.head > Node1 > Node2 > Node3 > Node3] becomes
                    #[new self.head > former self.head > Node1 > Node2 > Node3]
                    first = last
                    while first.previous:
                        first=first.previous
                        
                        
                    
                    
                
        self.length = self.length + 1
        
    
    def removeFromQueue(self):
        
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next_node
            


