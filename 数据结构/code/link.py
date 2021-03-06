class Node():
    """
    节点类
    """
    def __init__(self, alink = None, value = None):
        self._value = value
        self._next = alink

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value
    
    def getNext(self):
        return self._next
    
    def setNext(self, alink):
        self._next = alink

print(Node() is None)

class mySingleLink():
    def __init__(self):
        self._head = Node()
        self._tail = None
        self._lenth = 0

    def isEmpty(self):
        if self._lenth == 0:
            return True
        else:
            return False

    def add(self, value):
        """
            头部添加元素
            如果链表为空，则新节点是头结点也是尾节点
            如果长度大于等于1，则新节点是头节点，新节点的下一个节点是当前头结点，尾节点不变
        """
        newNode = Node(value=value)
        if self._lenth == 0:
            self._tail = newNode
            self._head = newNode
        else:
            newNode.getNext(self._head)
            self._head = newNode
        self._lenth += 1

    def append(self, value):
        """
            尾部追加元素
            如果链表为空，则新节点是头结点也是尾节点
            如果长度大于等于1，则新节点是尾节点，新节点的下一个节点是之前的尾节点，头节点不变
        """
        newNode = Node(value=value)
        if self._lenth == 0:
            self._tail = newNode
            self._head = newNode
        else:
            self._tail.setNext(newNode)
            self._tail = newNode
        self._lenth += 1

    def insert(self, pos, value):
        """
            中间插入函数
            当输入位置为0，则调用add函数
            当输入位置大于长度，则调用append函数
            其他情况，遍历链表，找到位置的节点，将节点插入（位置节点的下一个节点指向新节点，
                                                        新节点的下一个节点指向位置节点的下一个节点）
        """
        if pos < 1:
            self.add(value)
        elif pos >= self._lenth:
            self.append(value)
        else:
            pre = self._head
            newNode = Node(value)
            tmp = 0
            while tmp < pos:
                pre = pre.getNext()
                tmp += 1
            newNode.setNext(pre.getNext())
            pre.setNext(newNode)
            self._lenth += 1
    
    def search(self, pos):
        """
        查找函数
        输入位置，返回该位置的节点
        """
        if pos < 1:
            return self._head
        elif pos >= self._lenth:
            return self._tail
        else:
            tmp = 0
            pre = self._head
            while tmp < pos:
                pre = pre.getNext()
                tmp += 1
            return pre
    
    def update(self ,pos ,value):
        """
        更新函数
        输入位置，将位置节点值替换
        """
        if pos < 1:
            self._head.setValue(value)
        elif pos >= self._lenth:
            self._tail.setValue(value)
        else:
            tmp = 0
            pre = self._head
            while tmp < pos:
                pre = pre.getNext()
                tmp += 1
            pre.setValue(value)

link1 = mySingleLink()
print(link1.isEmpty())
link1.add(123)
link1.insert(1,12345)
link1.append(9877)
print(link1.search(1))