# for any questions go to this link https://www.youtube.com/watch?v=WymCpVUPWQ4
import win32gui
import win32ui
import win32con
import sys
import pygetwindow as gw


from win32api import GetSystemMetrics

print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))


# win32gui.GetWindowText(win32gui.GetForegroundWindow())

def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        print (hex(hwnd), win32gui.GetWindowText( hwnd ))



win32gui.EnumWindows( winEnumHandler, None )
