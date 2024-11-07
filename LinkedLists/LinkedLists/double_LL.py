class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoubelLinkedList:
    def __init__(self):
        self.head=self.tail=None

    #insertion at last    
    def Insertion_last(self,data):
        n=Node(data)
        if self.head==None:
            self.head=self.tail=n
        else:
            n.prev=self.tail
            self.tail.next=n
            self.tail=n

    #Insertion at first
    def Insertion_first(self,data):
        n=Node(data)
        if self.head==None:
            self.head=self.tail=n
        else:
            n.next=self.head
            self.head.prev=n
            self.head=n

    #insertion based on position        
    def Insertion_position(self,data,pos):
        n=Node(data)
        if pos==1: 
            if self.head==None:  
                self.head=self.tail=n
            else:
                n.next=self.head
                self.head.prev=n
                self.head=n
            return self.head
        c=0
        temp=self.head
        while temp!=None and c<pos-1:
            c+=1
            if c==pos-1:
                n.next=temp.next
                n.prev=temp
                temp.next.prev=n
                temp.next=n
            temp=temp.next
        if temp==None:
            print("invalid position")
            return
    

    #Insertion based on value
    def Insert_Based_Value(self,data,val):
        n=Node(data)
        if self.head.data==val:
            n.next=self.head
            self.head=n
            return self.head
        temp=self.head
        while temp.next.next!=None:
            if temp.next.data==val:
                n.next=temp.next
                temp.next=n
                return self.head
            temp=temp.next
        print("values is not in the list")
        return
    
    
    #delete last node
    def Delete_Last(self):
        if self.head==None:
            print("list is empty")
            return
        if self.head.next is None:
            # If there is only one node, remove it
            self.head = None
            self.tail = None
            return
        temp=self.head
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None
        self.tail=temp
        return self.head

    #Delete first node
    def Delete_First_Node(self):
        if self.head==None:
            print("list is empty")
            return
        self.head=self.head.next
        return self.head
    
    #deletion based on postion
    def Delete_Based_Position(self,pos):       # edge Cases:postion>0,pos==1,[this code delets from 2nd node only]
        if self.head==None:                        
            print("list is empty")
            return
        temp=self.head
        c=0
        while temp !=None:
            c+=1
            if c==pos-1:
                temp.next=temp.next.next
                return self.head
            temp=temp.next
        print("Position out of range")
        return self.head
    

    #print elements
    def Show(self):
        if self.head==None:
            print("List is Empty")
            return
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next


s=DoubelLinkedList()
while True:
    print()
    print("1.Creation \n 2.Insertion first\n 3.Insertion position \n 4.Inseration based on Value \n 5.Delete last Node \n 6.Delete first Node \n 7. Delete Based On position \n 8.Show \n ")
    ch=int(input("Choice"))
    if ch==1:
        data=int(input("element"))
        s.Insertion_last(data)
    elif ch==2:
        d=int(input())
        s.Insertion_first(d)
    elif ch==3:
        d=int(input())
        pos=int(input())
        s.Insertion_position(d,pos)
    elif ch==8:
        s.Show()
    elif ch==4:
        d=int(input())
        val=int(input())
        s.Insert_Based_Value(d,val)
    elif ch==6:
        s.Delete_First_Node()
    elif ch==5:
        s.Delete_Last()
    elif ch==7:
        pos=int(input())
        s.Delete_Based_Position(pos)
    else:
        print("Invalid Choice")


        


