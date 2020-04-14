class Queue:
    def __init__(self):
        self.stack=[]
    def Enqueue(self,data):
        self.stack.append(data)
    def Dequeue(self):
        if len(self.stack)==0:
            print("queue is empty")
            return
        temp=self.stack.pop()
        if len(self.stack)==0:
            return temp
        temp1=self.Dequeue()
        self.stack.append(temp)
        return temp1
if __name__=="__main__":
    que=Queue()
    que.Enqueue(1)
    que.Enqueue(2)
    que.Enqueue(3)
    print(que.Dequeue())
    print(que.Dequeue())
    print(que.Dequeue())
    print(que.Dequeue())




