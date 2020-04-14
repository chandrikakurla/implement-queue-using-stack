class Queue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def Enqueue(self,data):
        while(len(self.stack1)!=0):
            temp=self.stack1.pop()
            self.stack2.append(temp)
        self.stack1.append(data)
        while(len(self.stack2)!=0):
            temp=self.stack2.pop()
            self.stack1.append(temp)
    def Dequeue(self):
        if len(self.stack1)==0:
            print("queue is empty")
            return
        return self.stack1.pop()

if __name__=="__main__":
    que=Queue()
    print(que.Dequeue())

    que.Enqueue(1)
    que.Enqueue(2)
    que.Enqueue(3)
    print(que.Dequeue())
    print(que.Dequeue())
    print(que.Dequeue())
