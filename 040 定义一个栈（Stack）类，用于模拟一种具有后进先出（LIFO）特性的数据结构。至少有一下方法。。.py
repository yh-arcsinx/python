class C:
    count = 0
    def __init__(self,start=[]):
        C.count += 1
        self.stack=[]
        for x in start:
            self.push(x)
    def isEmpty():
        if C.count == 0:
            return True
        return False
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        return self.stack.pop()
    def top(self):
        return self.stack[-1]
    def bottom(self):
        return self.stack[1]
    
