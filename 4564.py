# -*- coding:UTF-8 -*-
import pyautogui
import time

# 指定点击位置的坐标
x, y = 750, 850

# 指定连续点击的次数
n = 100000

# 循环点击n次
for _ in range(n):
    pyautogui.click(x, y)  # 在指定坐标处点击
    time.sleep(0.01)  # 可选，添加延迟以模拟真实点击间隔