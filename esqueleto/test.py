print(3//2)










else:
            current=self._head
            for _ in range(end):
                current=current.next
            aux_end=current.next
            if not start==0:
                current=self._head
                for _ in range(start-1):
                    current=current.next
            current=inputList._head
            current=self._head
            while current.next:
                current=current.next
            
            current.next=aux_end







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