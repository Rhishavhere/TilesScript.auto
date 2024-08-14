from pyautogui import *
import pyautogui
import keyboard
import time
import random
import win32api,win32con

def click(x,y):
  win32api.SetCursorPos((x,y))
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
  time.sleep(0.02)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

click(930,560)

while keyboard.is_pressed('f')==False:
  if pyautogui.pixel(730,800)==(0,0,0):
    click(730,800)
  if pyautogui.pixel(860,800)==(0,0,0):
    click(860,800)
  if pyautogui.pixel(990,800)==(0,0,0):
    click(990,800)
  if pyautogui.pixel(1120,800)==(0,0,0):
    click(1120,800)

