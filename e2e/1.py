import psutil
import win32gui
import win32api
import win32con
import win32process

def Duplicate(self,PreHandle):
    Browser = self.BrowserWindowHandle
    self.driver.switch_to.window(PreHandle)
    win32api.PostMessage(Browser, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
    NewHandle = self.GetNewHandle(Browser)
    return NewHandle