'''
@Author: skypeee
@LastEditors: skypeee
@Description: myStack
@Date: 2019-09-04 10:07:11
'''
class myStack():
    def __init__(self, lenth):
        self._value = []
        self._lenth = lenth

    def pop(self):
        if len(self._value) == 0:
            print("栈空")
            return
        result = self._value[-1]
        del(self._value[-1])
        return result

    def push(self, value):
        if len(self._value) >= self._lenth:
            print("栈满")
            return
        self._value.append(value)
        return self._value

if __name__ == "__main__":
    a = myStack(10)
    print(a.pop())
    print(a.push(1))
    print(a.push(2))
    print(a.push(3))
    print(a.push(4))
    print(a.pop())
    print(a.push(1))