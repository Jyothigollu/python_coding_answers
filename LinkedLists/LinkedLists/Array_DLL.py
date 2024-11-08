class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoubelLinkedList:
    def __init__(self):
        self.head=self.tail=None
    def Insertion_last(self,data):
        n=Node(data)
        if self.head==None:
            self.head=self.tail=n
        else:
            n.prev=self.tail
            self.tail.next=n
            self.tail=n
        
    def show(self):
        if self.head==None:
            print("List is Empty")
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
    

    def Reverse_DLL(self):
        if self.head==None or self.head.next==None:
            return self.head
        temp = self.head
        while temp != None:
            t = temp.prev 
            temp.prev = temp.next 
            temp.next = t
            temp = temp.prev  

        
        self.head = t.prev  
        return self.head



s=DoubelLinkedList()
a=[1,2,3,4]
for i in range(len(a)):
    s.Insertion_last(a[i])
s.show()
s.Reverse_DLL()
s.show()