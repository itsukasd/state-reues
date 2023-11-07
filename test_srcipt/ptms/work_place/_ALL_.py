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
driver.get("http://ptms/admin/login.php")
driver.set_window_size(1550, 830)
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
element = driver.find_element(By.CSS_SELECTOR, ".btn")
driver.execute_script("arguments[0].click();", element)

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

# This is node 4
driver.find_element(By.LINK_TEXT, "Employee List").click()

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

# This is node 2
driver.find_element(By.CSS_SELECTOR, "#DataTables_Table_0_filter .form-control").send_keys("test")
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
safe_close(driver)
driver.switch_to.window(handles[4])

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

# This is node 3
driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(5) .btn").click() #3
driver.find_element(By.LINK_TEXT, "Delete").click()
element = driver.find_element(By.ID, "confirm")
driver.execute_script("arguments[0].click();", element)
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
safe_close(driver)
driver.switch_to.window(handles[4])

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

# This is node 28
driver.find_element(By.ID, "create_new").click()
time.sleep(0.5)
driver.find_element(By.ID, "code").send_keys('test'+str(random.randint(100,10000000000)))
driver.find_element(By.ID, "firstname").send_keys('test'+str(random.randint(100,10000000000)))
driver.find_element(By.ID, "lastname").send_keys('test'+str(random.randint(100,10000000000)))
driver.find_element(By.ID, "department").send_keys('test'+str(random.randint(100,10000000000)))
driver.find_element(By.ID, "position").send_keys('test'+str(random.randint(100,10000000000)))
driver.find_element(By.ID, "email").send_keys('test'+str(random.randint(100,10000000000))+'@test.com')
driver.find_element(By.ID, "generate-btn").click()
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
safe_close(driver)
driver.switch_to.window(handles[4])

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

# This is node 29
driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(5) .btn").click() #1
driver.find_element(By.LINK_TEXT, "View").click()
element = driver.find_element(By.CSS_SELECTOR, ".btn-dark")
driver.execute_script("arguments[0].click();", element)
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
safe_close(driver)
driver.switch_to.window(handles[4])

# This is node 30
driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(5) .btn").click() #2
driver.find_element(By.LINK_TEXT, "Edit").click()
element = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].click();", element)
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
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

# This is node 5
driver.find_element(By.CSS_SELECTOR, ".nav-reports_rendered_time > p").click()
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
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
driver.find_element(By.CSS_SELECTOR, ".nav-reports_by_employee > p").click()
driver.find_element(By.CSS_SELECTOR, ".btn-sm:nth-child(1)").click()
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
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

# This is node 7
driver.find_element(By.CSS_SELECTOR, ".nav-reports_date_wise > p").click()
driver.find_element(By.CSS_SELECTOR, ".fa-filter").click()
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
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

# This is node 8
driver.find_element(By.LINK_TEXT, "Work Type List").click()

# [duplicate]
index=8
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
driver.find_element(By.ID, "create_new").click()
time.sleep(1.5)
driver.find_element(By.ID, "name").send_keys('test'+str(random.randint(100,10000000000)))
driver.find_element(By.ID, "description").send_keys('test'+str(random.randint(100,10000000000)))
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
safe_close(driver)
driver.switch_to.window(handles[8])

# [duplicate]
index=8
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
driver.find_element(By.CSS_SELECTOR, "#DataTables_Table_0_filter .form-control").send_keys("test")
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
safe_close(driver)
driver.switch_to.window(handles[8])

# [duplicate]
index=8
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
driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) .btn").click()
driver.find_element(By.LINK_TEXT, "View").click()
element = driver.find_element(By.CSS_SELECTOR, ".btn-dark")
driver.execute_script("arguments[0].click();", element)
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
safe_close(driver)
driver.switch_to.window(handles[8])

# [duplicate]
index=8
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
driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(3) .btn").click()
driver.find_element(By.LINK_TEXT, "Edit").click()
element=driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].click();", element)
element=driver.find_element(By.CSS_SELECTOR, ".btn-group")
driver.execute_script("arguments[0].click();", element)
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
safe_close(driver)
driver.switch_to.window(handles[8])

# This is node 13
driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(7) .btn").click()
driver.find_element(By.LINK_TEXT, "Delete").click()
element = driver.find_element(By.ID, "confirm")
driver.execute_script("arguments[0].click();", element)
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
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

# This is node 14
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")  #1
driver.execute_script("arguments[0].click();", element)
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

# This is node 15
driver.find_element(By.LINK_TEXT, "User List").click()
time.sleep(1)

# [duplicate]
index=15
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

# This is node 16
driver.find_element(By.LINK_TEXT, "Create New").click()
time.sleep(0.5)
driver.find_element(By.ID, "firstname").send_keys('project'+str(random.randint(100,10000000000)))
driver.find_element(By.ID, "lastname").send_keys('project'+str(random.randint(100,10000000000)))
driver.find_element(By.ID, "username").send_keys('project'+str(random.randint(100,10000000000)))
driver.find_element(By.ID, "password").send_keys('project'+str(random.randint(100,10000000000)))
driver.find_element(By.CSS_SELECTOR, ".mr-2").click()
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
safe_close(driver)
driver.switch_to.window(handles[15])

# [duplicate]
index=15
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
element = driver.find_element(By.CSS_SELECTOR, ".odd .btn")
driver.execute_script("arguments[0].click();", element)
driver.find_element(By.LINK_TEXT, "Edit").click()
element = driver.find_element(By.CSS_SELECTOR, ".mr-2")
driver.execute_script("arguments[0].click();", element)
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
safe_close(driver)
driver.switch_to.window(handles[15])

# [duplicate]
index=15
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
driver.find_element(By.CSS_SELECTOR, "#DataTables_Table_0_filter .form-control").click()
driver.find_element(By.CSS_SELECTOR, "#DataTables_Table_0_filter .form-control").send_keys("test")
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
safe_close(driver)
driver.switch_to.window(handles[15])

# This is node 19
driver.find_element(By.CSS_SELECTOR, ".even .btn").click()
driver.find_element(By.LINK_TEXT, "Delete").click()
element = driver.find_element(By.ID, "confirm")
driver.execute_script("arguments[0].click();", element)
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
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

# This is node 20
driver.find_element(By.LINK_TEXT, "Settings").click()
driver.find_element(By.CSS_SELECTOR, ".btn-sm:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR, ".btn-rounded").click()
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

# This is node 21
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
driver.find_element(By.LINK_TEXT, "My Account").click()
driver.find_element(By.CSS_SELECTOR, ".btn-sm:nth-child(1)").click()
element = driver.find_element(By.CSS_SELECTOR, ".btn-sm:nth-child(1)")
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
safe_close(driver)
driver.switch_to.window(handles[1])

# This is node 22
driver.find_element(By.LINK_TEXT, "Project List").click()

# [duplicate]
index=22
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
driver.find_element(By.ID, "create_new").click()
element = driver.find_element(By.ID, "name")
driver.execute_script("arguments[0].click();", element)
driver.find_element(By.ID, "name").send_keys('project'+str(random.randint(100,10000000000)))
driver.find_element(By.ID, "description").send_keys('project'+str(random.randint(100,10000000000)))
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
safe_close(driver)
driver.switch_to.window(handles[22])

# [duplicate]
index=22
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
driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) .btn").click()
driver.find_element(By.LINK_TEXT, "View").click()
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
safe_close(driver)
driver.switch_to.window(handles[22])

# [duplicate]
index=22
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
driver.find_element(By.CSS_SELECTOR, "#DataTables_Table_0_filter .form-control").send_keys("project1")
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
safe_close(driver)
driver.switch_to.window(handles[22])

# [duplicate]
index=22
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

# This is node 26
driver.find_element(By.CSS_SELECTOR, ".even:nth-child(2) .btn").click()
driver.find_element(By.LINK_TEXT, "Edit").click()
element = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].click();", element)
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
safe_close(driver)
driver.switch_to.window(handles[22])

# This is node 27
driver.find_element(By.CSS_SELECTOR, ".even:nth-child(6) .btn").click()
driver.find_element(By.LINK_TEXT, "Delete").click()
element = driver.find_element(By.ID, "confirm")
driver.execute_script("arguments[0].click();", element)
element = driver.find_element(By.CSS_SELECTOR, ".ml-3")
driver.execute_script("arguments[0].click();", element)
safe_close(driver)
safe_close(driver)
safe_close(driver)
end=time.time()
print('time:%s s' % (end - start))
tlog(end - start)
