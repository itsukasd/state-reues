from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import psutil
import win32gui
import win32api
import win32con
import win32process
import os
import time
import random

def get_window_by_pid(pid):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds[0] if hwnds else None

def get_browser_window_handle_by_driver_pid(driver_pid):
    # Only one of processes in browser process group have window handle
    # in normal cases. And all of process(in process group) related to 
    # the browser are the children of the driver process. So the function
    # will return as we confirm a process have window handle, which we 
    # will manipulate later
    process_driver = psutil.Process(driver_pid)
    children_processes=process_driver.children(recursive=True)
    children_pids=[]
    for process in children_processes:
        children_pids.append(process.pid) 
        for pid in children_pids:
            hwnd=get_window_by_pid(pid)
            if hwnd is not None:
                return hwnd

def safe_close(driver):
    try:
        driver.close()
    except:
        driver=driver

def tlog(time):
    f=open('D:\preixTree\log.txt','a')
    out='@@@'+str(time)+'$$$\n'
    f.write(out)
    f.close()


options = Options()
options.binary_location = r'C:\Program Files\Firefox Developer Edition\firefox.exe'
path = os.path.abspath(r'D:\preixTree\my-firefox-plugin.xpi')
driver = webdriver.Firefox(options=options)
driver.install_addon(path,temporary=True)
driver.get("about:blank")
driver_pid=driver.service.process.pid
#print("driver pid:",driver_pid)
hwnd=get_browser_window_handle_by_driver_pid(driver_pid)
#print("hwnd:",hwnd)
handles={}
roothd=driver.current_window_handle
handles[0]=roothd
start=time.time()

# This is auto-generated execution code

driver.implicitly_wait(10)

# This is node 0
# THIS IS VIRTUAL ROOT

# This is node 1
driver.get("http://savsoftquiz/")
driver.set_window_size(976, 703)
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, ".btn").click()

# [duplicate]
index=1
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 5
driver.find_element(By.LINK_TEXT, "Setting").click()

# [duplicate]
index=5
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 2
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) b").click()

# [duplicate]
index=2
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 11
driver.find_element(By.LINK_TEXT, "Add new").click()
driver.find_element(By.LINK_TEXT, "Back").click()
driver.find_element(By.CSS_SELECTOR, ".fa-caret-down").click()
safe_close(driver)
driver.switch_to.window(handles[2])

# [duplicate]
index=2
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 12
driver.find_element(By.LINK_TEXT, "Edit").click()
driver.find_element(By.LINK_TEXT, "Back").click()
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle > .fa-user").click()
safe_close(driver)
driver.switch_to.window(handles[2])

# This is node 20
driver.find_element(By.LINK_TEXT, "Next").click()
driver.find_element(By.LINK_TEXT, "Back").click()
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle").click()
safe_close(driver)
safe_close(driver)
driver.switch_to.window(handles[5])

# [duplicate]
index=5
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 3
driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1) > b").click()

# [duplicate]
index=3
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 13
driver.find_element(By.LINK_TEXT, "Add new").click()
driver.find_element(By.NAME, "groupname").click()
driver.find_element(By.NAME, "groupname").send_keys("1")
driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
driver.find_element(By.LINK_TEXT, "Back").click()
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle > .fa-user").click()
safe_close(driver)
driver.switch_to.window(handles[3])

# [duplicate]
index=3
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 14
driver.find_element(By.LINK_TEXT, "Edit").click()
driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
driver.find_element(By.LINK_TEXT, "Back").click()
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle").click()
safe_close(driver)
driver.switch_to.window(handles[3])

# This is node 21
driver.find_element(By.LINK_TEXT, "Next").click()
driver.find_element(By.LINK_TEXT, "Back").click()
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle").click()
safe_close(driver)
safe_close(driver)
driver.switch_to.window(handles[5])

# This is node 4
driver.find_element(By.LINK_TEXT, "Difficulty Level").click()

# [duplicate]
index=4
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 15
driver.find_element(By.LINK_TEXT, "Add new").click()
driver.find_element(By.LINK_TEXT, "Back").click()
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle > .fa-user").click()
safe_close(driver)
driver.switch_to.window(handles[4])

# This is node 16
driver.find_element(By.LINK_TEXT, "Edit").click()
driver.find_element(By.LINK_TEXT, "Back").click()
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) .btn-info").click()
driver.find_element(By.LINK_TEXT, "Back").click()
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) .btn-info").click()
driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
driver.find_element(By.LINK_TEXT, "Back").click()
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle").click()
safe_close(driver)
safe_close(driver)
safe_close(driver)
driver.switch_to.window(handles[1])

# [duplicate]
index=1
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 6
driver.find_element(By.CSS_SELECTOR, ".panel-primary .panel-footer").click()

# [duplicate]
index=6
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 7
driver.find_element(By.LINK_TEXT, "Dashboard").click()
driver.find_element(By.CSS_SELECTOR, ".panel-green .panel-footer .fa").click()

# [duplicate]
index=7
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 9
driver.find_element(By.LINK_TEXT, "Add new").click()
element = driver.find_element(By.CSS_SELECTOR, "html")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.CSS_SELECTOR, "html")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "html")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.switch_to.frame(0)
driver.find_element(By.CSS_SELECTOR, "html").click()
driver.switch_to.default_content()
element = driver.find_element(By.CSS_SELECTOR, "html")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.CSS_SELECTOR, "html")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "html")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.switch_to.frame(0)
element = driver.find_element(By.ID, "tinymce")
driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>test<br data-mce-bogus=\"1\"></p>'}", element)
driver.switch_to.default_content()
driver.find_element(By.ID, "radiobtn").click()
driver.switch_to.frame(1)
driver.find_element(By.CSS_SELECTOR, "html").click()
element = driver.find_element(By.ID, "tinymce")
driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>test<br data-mce-bogus=\"1\"></p>'}", element)
driver.switch_to.default_content()
driver.find_element(By.CSS_SELECTOR, ".btn").click()
driver.find_element(By.LINK_TEXT, "Question Bank").click()
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle > .fa-user").click()
safe_close(driver)
driver.switch_to.window(handles[7])

# [duplicate]
index=7
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 10
driver.find_element(By.LINK_TEXT, "Dashboard").click()
element = driver.find_element(By.CSS_SELECTOR,"i.fa.fa-arrow-circle-right")
driver.execute_script("arguments[0].click();", element)

# [duplicate]
index=10
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 23
driver.find_element(By.LINK_TEXT, "Dashboard").click()
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle > .fa-user").click()
safe_close(driver)
driver.switch_to.window(handles[10])

# [duplicate]
index=10
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 24
driver.find_element(By.LINK_TEXT, "Next").click()
driver.find_element(By.LINK_TEXT, "Back").click()
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle").click()
safe_close(driver)
driver.switch_to.window(handles[10])

# This is node 27
driver.find_element(By.LINK_TEXT, "Search").click()
driver.find_element(By.NAME, "search").click()
driver.find_element(By.NAME, "search").send_keys("1")
driver.find_element(By.CSS_SELECTOR, ".btn-default:nth-child(3)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-caret-down").click()
safe_close(driver)
safe_close(driver)
driver.switch_to.window(handles[7])

# [duplicate]
index=7
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 17
driver.find_element(By.LINK_TEXT, "Edit").click()
element = driver.find_element(By.CSS_SELECTOR, "html")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.CSS_SELECTOR, "html")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "html")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.CSS_SELECTOR, ".btn").click()
driver.find_element(By.LINK_TEXT, "Question Bank").click()
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle").click()
safe_close(driver)
driver.switch_to.window(handles[7])

# [duplicate]
index=7
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 22
driver.find_element(By.LINK_TEXT, "Next").click()
driver.find_element(By.LINK_TEXT, "Back").click()
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle > .fa-user").click()
safe_close(driver)
driver.switch_to.window(handles[7])

# This is node 26
driver.find_element(By.LINK_TEXT, "Search").click()
driver.find_element(By.NAME, "search").click()
driver.find_element(By.NAME, "search").send_keys("5")
driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle").click()
safe_close(driver)
safe_close(driver)
driver.switch_to.window(handles[6])

# [duplicate]
index=6
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 8
driver.find_element(By.LINK_TEXT, "Add new").click()
driver.find_element(By.NAME, "username").click()
driver.find_element(By.NAME, "username").send_keys("test")
driver.find_element(By.NAME, "first_name").send_keys("test")
driver.find_element(By.NAME, "last_name").send_keys("test")
driver.find_element(By.NAME, "user_email").send_keys("test")
driver.find_element(By.NAME, "user_password").send_keys("test")
driver.find_element(By.NAME, "confirm_password").send_keys("test")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
driver.find_element(By.LINK_TEXT, "Users").click()
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle").click()
safe_close(driver)
driver.switch_to.window(handles[6])

# [duplicate]
index=6
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 18
driver.find_element(By.LINK_TEXT, "Edit").click()
driver.find_element(By.CSS_SELECTOR, ".btn").click()
driver.find_element(By.LINK_TEXT, "Users").click()
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) .btn-info").click()
driver.find_element(By.CSS_SELECTOR, ".btn").click()
driver.find_element(By.LINK_TEXT, "Users").click()
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle").click()
safe_close(driver)
driver.switch_to.window(handles[6])

# [duplicate]
index=6
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 25
driver.find_element(By.LINK_TEXT, "Next").click()
driver.find_element(By.LINK_TEXT, "Back").click()
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle").click()
safe_close(driver)
driver.switch_to.window(handles[6])

# This is node 28
driver.find_element(By.LINK_TEXT, "Search").click()
driver.find_element(By.NAME, "search").click()
driver.find_element(By.NAME, "search").send_keys("1")
driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
driver.find_element(By.CSS_SELECTOR, ".fa-caret-down").click()
safe_close(driver)
safe_close(driver)
driver.switch_to.window(handles[1])

# [duplicate]
index=1
pre_hd=driver.current_window_handle
# always use duplicate page, previous handle need to reserve
win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
# time.sleep(1)
handles[index]=None
while(handles[index] is None):
    for window_handle in driver.window_handles:
    #if exist window handle not in dict, it's new duplicate window
        if window_handle not in handles.values() and window_handle != pre_hd:
            handles[index]=window_handle
driver.switch_to.window(pre_hd)
#ensure change success
while(driver.current_window_handle == pre_hd):
    break
# [duplicate over]

# This is node 19
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle > .fa-user").click()
driver.find_element(By.LINK_TEXT, "My Account").click()
driver.find_element(By.CSS_SELECTOR, ".btn").click()
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle > .fa-user").click()
safe_close(driver)
driver.switch_to.window(handles[1])

# This is node 29
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle").click()
safe_close(driver)
safe_close(driver)
end=time.time()
print('time:%s s' % (end - start))
tlog(end - start)
