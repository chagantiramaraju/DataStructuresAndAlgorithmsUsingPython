from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
    
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
    
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return -1
    
    def Isempty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


if __name__=='__main__':
    st = Stack()
    st.push(5)
    st.push(10)
    print(st.stack)
    st.pop()
    print(st.stack)
    print(st.peek())