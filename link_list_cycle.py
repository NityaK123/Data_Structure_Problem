class Node:
    def __init__(self,x):
        self.val=x 
        self.next=None 
        
class Link:
    def __init__(self):
        self.Head=None

    def insertNode(self,x):
        newNode=Node(x)
        if self.Head==None:
            self.Head=newNode 
        else:
            temp=self.Head
            while(temp.next!=None):
                temp=temp.next 
            temp.next=newNode
    
    def Print(self):
        if self.Head!=None:
            temp=self.Head 
            while(temp!=None):
                print(temp.val,end="->")
                temp=temp.next 
                
res=Link()
for i in range(0,5):
    n=int(input())
    res.insertNode(n)
res.Print()
    
            
                
            