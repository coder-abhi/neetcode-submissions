class LinkedList:
    
    def __init__(self):
        self.arr = []

    
    def get(self, index: int) -> int:
        if len(self.arr) > index:
            return self.arr[index]
        else:
            return -1
        

    def insertHead(self, val: int) -> None:
        result = [val]
        for i in self.arr:
            result.append(i)
        self.arr = result

        

    def insertTail(self, val: int) -> None:
        self.arr.append(val)
        

    def remove(self, index: int) -> bool:
        if len(self.arr) <= index:
            return False
        result = []
        for i in range(len(self.arr)):
            if i != index:
                result.append(self.arr[i])

        self.arr = result
        return True
        

    def getValues(self) -> List[int]:
        return self.arr
        
