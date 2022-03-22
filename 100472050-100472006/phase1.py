from slist import SList
from slist import SNode
import sys
# Raúl Aguilar Arroyo, 100472050
# Luis Gómez-Manzanilla Nieto, 100472006

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
            if n>len(self): # Si se supera el size de la lista se suman todos los elementos de la lista
                n=len(self)
            current=self._head # varaible de movimiento
            total=0
            for _ in range(len(self)-n): # posicionamiento en la lista dejando los n últimos elementos 
                    current=current.next 
            while current: # suman los n elementos hasta el final de la lista
                total+=current.elem 
                current=current.next
            return total
    
    #method for inserting a new node in the middle
    def insertMiddle(self, elem):
        # caso lista vacía
        if len(self)==0:
            self.addFirst(elem) 
        else:
            node = SNode(elem) # cear el nodo con el elemento a introducir
            current=self._head # variable de movimiento
            if len(self)%2==0: # caso par
                for _ in range(len(self)//2-1): # posicionamiento antes de la mitad
                    current=current.next
            else: # caso impar
                for _ in range((len(self)//2)): # posicionamiento antes de la mitad
                    current=current.next
            node.next=current.next # vinculamos el nodo a la lista 
            current.next=node # vinculamos la lista al nodo
        self._size+=1
                

    def insertList(self,inputList:SList,start,end):
        ''' en el peor de los casos tiene complejidad de T(n)=3n+5 es decir O(n)'''
        if start<0 or start >len(self) or end<start or end>=len(self): # excepciones
            return 

        else: # ejecucion normal
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
        '''tiene una complejidad de T(n)=2n+13 O(n)'''
        auxL=SList() # la lista dondese invierten los elementos
        current=self._head # seran los elementos que se invierten
        current2=self._head # es la posicion donde se asignan los elementos ya invertidos
        auxPointer=None # sera el puntero que recorre la lista auxiliar para reasignar los elementos ya reordenados
        if k<=1: # no modifica la lista 
            return
            
        while current: # ejecucion normal
            for _ in range(k): 
                if current: # excepcion para cuando estas en el ultimo nodo no se salga, -len(self) % k != 0-
                    auxL.addFirst(current.elem) # añade los elementos a la lista auxilar de forma que se van invirtiendo
                    current=current.next 
            
            auxPointer=auxL._head #reinicia el puntero de la lista de k elementos invertida
            for _ in range(k):
                if current2 and auxPointer: # excepcion para cuando estas en el ultimo nodo no se salga
                    current2.elem=auxPointer.elem   # reemplaza el elemento del nodo que apunta c2 por el elemento 
                                                    # que apunta el puntero de la lista invertida
                    current2=current2.next # avancamos en la lista principal
                    auxPointer=auxPointer.next # avancamos en la lista invertida
            
            auxL=SList() # reiniciamos la lista invertida


    def maximumPair(self):
        '''T(n)=2n+19 O(n)'''
        aux=SList2()
        current=self._head
        if self._size==0:
            return
        
        for _ in range(len(self)):  # creamos una lista invertida
            aux.addFirst(current.elem)
            current=current.next
        
        current_aux=aux._head # reinicio de los contadores
        current=self._head
        maxi=0
        alfa=0
        if len(self)%2!=0: # establece que si la lista es impar se debe hacer una iteracion mas
            alfa=1
        for i in range((len(self)//2+alfa)): # recorremos la mitad de la lista redondeado hacia abajo por lo que si es
                                             # impar debemos añadir una iteracion para el ultimo elemento       
            par1=current.elem
            par2=current_aux.elem
            if not i == len(self)//2: # si no estamos en la ultima iteracion sumamos pares
                value=par1+par2
            else:   # cuando lo anterior no se cumple significa que la lista es impar por lo que no hay que sumar el par ya que solo se cuenta una vez
                value=par1
            if value>maxi: # modificamos el valor maximo
                    maxi=value
            
            current=current.next # continua la iteracion
            current_aux=current_aux.next # continua la iteracion
        return maxi
