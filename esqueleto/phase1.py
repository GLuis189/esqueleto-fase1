from slist import SList
from slist import SNode
import sys

class SList2(SList):

    def sumLastN(self, n):
        '''complejidad O(n)'''
        #n=0
        if n==0:
            return 0
        #n<0
        elif n<0:
            return None

        #0<n<len(self)
        else:
            if n>len(self):
                n=len(self)
            current=self._head
            total=0
            for _ in range(len(self)-n):
                    current=current.next 
            while current:   
                total+=current.elem
                current=current.next
            return total
    
    #method for inserting a new node in the middle
    def insertMiddle(self, elem):
        if len(self)==0:
            self.addFirst(elem)
        else:
            node = SNode(elem)
            current=self._head
            if len(self)%2==0:
                for _ in range(len(self)//2-1):
                    current=current.next
            else:
                for _ in range((len(self)//2)):
                    current=current.next
            node.next=current.next
            current.next=node
                

    def insertList(self,inputList,start,end):
        #start <0, >len(self)
        if start<0 or start >len(self) or end<start or end>=len(self):
            return 
        
        elif start==0:
            current=self._head
            for _ in range(end):
                current=current.next
            aux_end=current.next
            self._head=inputList._head
            current=self._head
            while current.next:
                current=current.next
            current.next=aux_end
        
        else:
            # if start = 0 cambiar l.kead despues de conservar end
            current=self._head
            for _ in range(end):
                current=current.next
            aux_end=current.next
            current=self._head
            if not start==0:
                for _ in range(start-1):
                    current=current.next
            current.next=inputList._head 
            while current.next:
                current=current.next
            current.next=aux_end



    def reverseK(self,k):
        pass


    def maximumPair(self):
        pass
 