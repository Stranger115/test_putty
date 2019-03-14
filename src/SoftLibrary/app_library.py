import os
import pyautogui
from time import sleep
from pywinauto.application import Application
from .setting import PAUSE

CURDIR = os.path.abspath(os.path.dirname(__file__))
pyautogui.PAUSE = PAUSE


class AppOperaLibrary:
    def __init__(self):
        self.__app = None
    
    def open_app(self, last_dir, app_name):
        # open app
        path = os.path.join(os.path.abspath('.'), last_dir, app_name)
        app_start = Application().start(path)
        # 绑定进程,class_name和title是可选的，可以灵活使用，如果找到多个货没有找到该程序，程序会报错
        self.__app = Application().connect(class_name='PuTTYConfigBox')

    # 每执行一个函数后暂停几秒钟
    def __raise_error(self):
        if not self.__app:
            raise RuntimeError('未创建应用 请先调用 OPEN APP ')
    
    def connect_setting(self, ip, name):
        self.__raise_error()
        win = self.__app["PuTTY Configuration"]
        # 创建SHH连接
        win.Edit.type_keys(ip)
        win.Edit3.type_keys(name)
        return win

    def save_connect(self, win, close_state):
        win[close_state].click()
        win['Save'].click()
        sleep(2)

    def delete_connect(self, win, name):
        win['ListBox'].select(name)
        win['Delete'].click()

    def open_connect(self, win):
        win['Open'].click()
        win.wait_not('visible')
        # second_win = self.__app['PuTTY Security Alert']
        # second_win['是（Y）'].click()

    def connect_type(self, win, type):
        win[type].click()
        sleep(2)
    
    def connect(self, operation: dict):
        self.__raise_error()
        """登录且验证命令行键入"""
        #  每次键入的时间间隔
        secs_between_keys = 0.1
        for key in operation:
            pyautogui.typewrite(operation[key], interval=secs_between_keys)
            sleep(1)
    
    def close_session(self):
        self.__raise_error()
        win_close = self.__app['PuTTY']
        try:
            win_close.close()
        except Exception as e:
            win_confirm = self.__app['PuTTY Exit Confirmation']
            win_confirm['确定'].click()

    def close_setting(self, win):
        win.close()

