'''
@Author: skypeee
@LastEditors: skypeee
@Description: myStack
@Date: 2019-09-04 10:07:11
'''
class myStack():
    def __init__(self):
        self._value = []

    def pop(self):
        result = self._value[-1]
        del(self._value[-1])
        return result

    def push(self, value):
        self._value.append(value)
        return self._value

if __name__ == "__main__":
    a = myStack()
    print(a.push(1))
    print(a.push(2))
    print(a.push(3))
    print(a.pop())
    print(a.push(4))
    print(a.pop())
    print(a.push(1))