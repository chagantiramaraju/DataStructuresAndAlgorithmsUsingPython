from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def push(self,data):
        self.queue.append(data)

    def pop(self):
        if len(self.queue) > 0:
            self.queue.popleft()

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
    
    def Isempty(self):
        return len(self.queue) == 0


if __name__=='__main__':
    que = Queue()
    que.push(10)
    que.push(20)
    que.push(30)
    print(que.queue)
    que.pop()
    print(que.peek())
    que.pop()
    print(que.queue)