class Queue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def Enqueue(self,data):
        self.stack1.append(data)
    def Dequeue(self):
        if len(self.stack1)==0 and len(self.stack2)==0:
            print("queue is empty")
            return
        if len(self.stack2)==0:
            while (len(self.stack1)!=0):
                temp=self.stack1.pop()
                self.stack2.append(temp)
        return self.stack2.pop()
if __name__=="__main__":
    que=Queue()
    que.Enqueue(1)
    que.Enqueue(2)
    que.Enqueue(3)
    print(que.Dequeue())
    print(que.Dequeue())
    print(que.Dequeue())
    print(que.Dequeue())