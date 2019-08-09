class Node:
    
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right= None


class Tree:
    
    def __init__(self,root):
        self.root = Node(root)
        
    def append(self,value):
        s = Node(value)
        current = self.root
        while(current != None):
            print(current.value)
            if(value > current.value):
                if(current.right != None):
                    current = current.right
                    print(current.value)

                else:
                    current.right = s
                    break

            else:
                if(current.left != None):
                    current = current.left
                    print(current.value)

                else:
                    current.left = s
                    break

    def traverse(self):
        parent = self.root
        print(parent.value)
        if(parent.left != None):
            depth = 1
            self.subtree(parent.left,depth)
        if(parent.right != None):
            depth = 1
            self.subtree(parent.right,depth)


    def subtree(self,current,depth):
        
        if(current != None):
            tabs = ""
            for x in range(0,depth):
                tabs = tabs +"\t"
            print(tabs+str(current.value))
        else:
            print("None")
            
        if(current.left == None):
            if(current.right == None):
                return 0
            else:
                self.subtree(current.right,depth+1)

        else:
            self.subtree(current.left,depth+1)

        
