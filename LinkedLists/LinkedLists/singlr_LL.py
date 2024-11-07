class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SingleLinkedList:
    def __init__(self):
        self.head=self.tail=None
    def Create_LL(self,data):
        n=Node(data)
        if self.head==None:
            self.head=self.tail=n
        else:
            self.tail.next=n
            self.tail=n
    def Insertion_first(self,data):
        n=Node(data)
        if self.head==None:
            self.head=self.tail=n
        else:
            n.next=self.head
            self.head=n
    def Insertion_position(self,data,pos):
        n=Node(data)
        if pos==1: 
            if self.head==None:  
                self.head=self.tail=n
            else:
                n.next=self.head
                self.head=n
            return n
        c=0
        temp=self.head
        while temp!=None:
            c+=1
            if c==pos-1:
                n.next=temp.next
                temp.next=n
            temp=temp.next
        if pos>c:
            print("invalid position")
            return
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
        
    def Show(self):
        if self.head==None:
            print("List is Empty")
            return
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
s=SingleLinkedList()
while True:
    print()
    print("1.Creation \n 2.Insertion first\n 3.Insertion position \n 4.Inseration based on Value \n 5.Show \n ")
    ch=int(input("Choice"))
    if ch==1:
        data=int(input("element"))
        s.Create_LL(data)
    elif ch==2:
        d=int(input())
        s.Insertion_first(d)
    elif ch==3:
        d=int(input())
        pos=int(input())
        s.Insertion_position(d,pos)
    elif ch==5:
        s.Show()
    elif ch==4:
        d=int(input())
        val=int(input())
        s.Insert_Based_Value(d,val)
    else:
        print("Invalid Choice")


        


