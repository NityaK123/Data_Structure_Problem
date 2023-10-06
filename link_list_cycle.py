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
    
    def Update(self,pos):
        if self.Head==None:
            return 
        else:
            temp=self.Head 
            while(temp.next!=None):
                temp=temp.next 
            tem=self.Head
            if pos==1:
                tem=self.Head 
                temp.next=tem 
            else:
                while(pos!=1):
                    tem=tem.next 
                    pos=pos-1
                temp.next=tem 
    def Cycle(self):
        if self.Head==None:
            return False 
        else:
            temp=self.Head
            tem=self.Head
            while(temp!=None and temp.next!=None):
                tem=tem.next
                temp=temp.next.next 
                if tem==temp:
                    break 
            if tem==temp:
                return True 
            else:
                return False
                
                
                
res=Link()
for i in range(0,5):
    n=int(input())
    res.insertNode(n)
pos=int(input())
res.Print()
res.Update(pos)    
val=res.Cycle()  
print(val)      