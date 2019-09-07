'''
@Author: skypeee
@LastEditors: skypeee
@Description: myqueue
@Date: 2019-09-04 10:13:19
'''
class myQueue():
    def __init__(self):
        self._value = []

    def entry(self,value):
        self._value.append(value)
        return self._value
    
    def exit(self):
        result = self._value[0]
        del(self._value[0])
        return result

if __name__ == "__main__":
    a = myQueue()
    print(a.entry(1))
    print(a.entry(2))
    print(a.entry(3))
    print(a.exit())
    print(a.exit())
    print(a.exit())

