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
                

    def insertList(self,inputList:SList,start,end):
        if start<0 or start >len(self) or end<start or end>=len(self): # excepciones
            return 
        
        else:

            current=self._head
            end_iters=1
            start_iters=0

            for i in range(end): # navego hasta end
                current=current.next
                end_iters=i
            aux_end=current.next # guardo lo que va tras end para que no pierda el puntero y se borre
            
            if start==0: 
                # unicamente remplaza self.head por la head de la nueva lista, tambien establece
                # el puntero para la nevegacion de despues en la cabeza de la nueva lista
                self._head = inputList._head  
                current=self._head

            else:     
                # busca start y lo reemplaza por el head de la nueva lista, tambien establece 
                # el puntero para la navegacion de despues en cabeza de la nueva lista
                current=self._head # reinicio la navegacion
                for i in range(start-1): # navego hasta start
                    current=current.next
                    start_iters=i
                current.next=inputList._head # cambio el siguiente elemento por el head de la nueva lista

            while current.next: # navego hasta el final de la nueva lista
                current=current.next
            current.next=aux_end
            self._size= self._size+inputList._size-(end_iters-start_iters+2)

    def reverseK(self,k):
        pass


    def maximumPair(self):
        pass


