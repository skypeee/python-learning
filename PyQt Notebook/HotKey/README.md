# python 全局热键

## 需求

- 获取全局键盘事件

## 用到的包

1. evdev

## 文档

-  https://python-evdev.readthedocs.io/en/latest 

## 代码

```python
import evdev

device = evdev.InputDevice('/dev/input/event1')

print(device)

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
         print(evdev.categorize(event))
```



