class Node:
    def __init__(self,val):
        self.value = val
        self.next = None




class Queue:
    def __init__(self,headval):
        self.head = Node(headval)
        self.tail = self.head


    def append(self,value):
        s = Node(value)
        if(self.head != None):
            if(self.head.next == None):
                self.head.next = s
                self.tail = s
            else:
                self.tail.next = s
                self.tail = s
        else:
            self.head = s

    def pop(self):
        self.head = self.head.next
        
    def print(self):
        s = self.head
        if(self.head ==None):
            return "Queue is empty!"
        while(s.next != None):
            print(s.value)
            s = s.next
        print(s.value)

    
    


        
        
