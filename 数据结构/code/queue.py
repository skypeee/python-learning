'''
@Author: skypeee
@LastEditors: skypeee
@Description: myqueue
@Date: 2019-09-04 10:13:19
'''
class myQueue():
    def __init__(self, lenth):
        self._value = []
        self._lenth = lenth

    def entry(self,value):
        if len(self._value) >= self._lenth:
            print("队已满")
            return
        self._value.append(value)
        return self._value
    
    def exit(self):
        if len(self._value) == 0:
            print("队空")
            return
        result = self._value[0]
        del(self._value[0])
        return result

if __name__ == "__main__":
    a = myQueue(3)
    print(a.exit())

    print(a.entry(1))
    print(a.entry(2))
    print(a.entry(3))
    print(a.exit())
    print(a.exit())

