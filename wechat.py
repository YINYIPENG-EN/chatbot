import time
import pyperclip
import pyautogui
from tools.utils import Speech_Recognition, save_wav
time.sleep(10)  # 等待10s.
save_wav()  # 录制语音并保存
text = ''  # 初始化
text_ = Speech_Recognition()  # 是否开启语音助手
print(text)
while True:
    if text_ == '开启语音助手':  # 开启
        time.sleep(2)  # 等待2s输入一次
        save_wav()  # 语音录制
        try:
            text = Speech_Recognition()  # 语音识别
            if text == '关闭语音助手':
                break
            pyperclip.copy(text)  # 文本框内想输入的内容
            pyautogui.hotkey('ctrl', 'v')  # 粘贴内容
            pyautogui.mouseUp()  # 模拟鼠标将左键抬起
            pyautogui.moveTo(1531, 933)  # 鼠标光标移动至发送按钮(这里是坐标)
            pyautogui.mouseDown()  # 鼠标左键按下，发送内容
            pyautogui.mouseUp()  # 鼠标左键抬起
            # 对于chatgpt需要在点击一下对话框
            pyautogui.moveTo(639, 929)
            pyautogui.mouseDown()  # 鼠标左键按下，发送内容
            pyautogui.mouseUp()  # 鼠标左键抬起
            text = ''
        except:
            print("未识别到语音")
            continue

    elif text_ == '关闭语音助手':
        break



