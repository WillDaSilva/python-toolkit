from collections import deque

class BinaryTree:
    def __init__(self, data=None, l=None, r=None):
        self.data = data
        self.l = None
        self.r = None

    def __iter__(self):
        return self.inOrder()

    def __str__(self):
        return '__str__ not yet implemented'

    def height(self):
        q = deque()
        q.append(self)
        h = 0
        while q:
            h += 1
            nodeCount = len(q)
            while nodeCount > 0:
                node = q.popleft()
                if node.l is not None:
                    q.append(node.l)
                if node.r is not None:
                    q.append(node.r)
                nodeCount -= 1
        return h

    def breadthFirst(self):
        q = deque()
        q.append(self)
        while q:
            node = q.popleft()
            yield node
            if node.l is not None:
                q.append(node.l)
            if node.r is not None:
                q.append(node.r)

    def preOrder(self):
        stack = []
        stack.append(self)
        while stack:
            node = stack.pop()
            yield node
            if node.r is not None:
                stack.append(node.r)
            if node.l is not None:
                stack.append(node.l)

    def inOrder(self):
        node = self
        stack = []
        while stack or node is not None:
            if node is not None:
                stack.append(node)
                node = node.l
            else:
                node = stack.pop()
                yield node
                node = node.r

    def postOrder(self):
        node = self
        stack = []
        lastNode = None
        while stack or node is not None:
            if node is not None:
                stack.append(node)
                node = node.l
            else:
                if stack[-1].r is not None and lastNode != stack[-1].r:
                    node = stack[-1].r
                else:
                    yield stack[-1]
                    lastNode = stack.pop()
