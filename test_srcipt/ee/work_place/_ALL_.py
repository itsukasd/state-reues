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
driver.get("http://ee/admin/login.php")
driver.set_window_size(1550, 830)
driver.find_element(By.ID, "username").click()

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
driver.find_element(By.ID, "password").send_keys("admin123")
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, ".btn").click()

# [duplicate]
index=19
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
driver.find_element(By.LINK_TEXT, "Maintenance").click()

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

# This is node 4
driver.find_element(By.CSS_SELECTOR, "#new_department > .svg-inline--fa").click()
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys('Department'+str(random.randint(100,10000000000)))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
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

# This is node 5
driver.find_element(By.CSS_SELECTOR, "#new_course > .svg-inline--fa").click()
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys('Position'+str(random.randint(100,10000000000)))
driver.find_element(By.ID,"select2-department_id-container").click()
driver.find_element(By.XPATH, '//*[@id="select2-department_id-results"]/li[2]').click()
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
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

# This is node 9
driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(8) .delete_department path").click()
driver.find_element(By.ID, "confirm").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
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

# This is node 11
driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(5) .delete_course path").click()
driver.find_element(By.ID, "confirm").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
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

# This is node 14
driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(5) .edit_course path").click()
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID,"dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[2])

# This is node 15
driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(8) .edit_department > .svg-inline--fa").click()
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
safe_close(driver)
driver.switch_to.window(handles[19])

# [duplicate]
index=19
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
driver.find_element(By.LINK_TEXT, "Enrollees").click()
driver.find_element(By.ID, "create_new").click()
driver.find_element(By.ID, "reference_code").click()
driver.find_element(By.ID, "reference_code").send_keys('Emcode'+str(random.randint(100,10000000000)))
driver.find_element(By.ID, "firstname").click()
driver.find_element(By.ID, "firstname").send_keys('Fname'+str(random.randint(100,10000000000)))
driver.find_element(By.ID, "lastname").click()
driver.find_element(By.ID, "lastname").send_keys('Lname'+str(random.randint(100,10000000000)))
driver.find_element(By.ID, "email").click()
driver.find_element(By.ID, "email").send_keys(str(random.randint(100,10000000000))+'@test.com')
driver.find_element(By.ID, "contact").click()
driver.find_element(By.ID, "contact").send_keys('Contact'+str(random.randint(100,10000000000)))
driver.find_element(By.ID, "address").click()
driver.find_element(By.ID, "address").send_keys('Address'+str(random.randint(100,10000000000)))
sel=driver.find_element(By.ID, "course_id")
Select(sel).select_by_index(2)
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, ".mid-large .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[19])

# [duplicate]
index=19
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
driver.find_element(By.LINK_TEXT, "Users").click()

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

# This is node 12
driver.find_element(By.ID, "create_new").click()
driver.find_element(By.ID, "fullname").click()
driver.find_element(By.ID, "fullname").send_keys('fullname'+str(random.randint(100,10000000000)))
driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys('username'+str(random.randint(100,10000000000)))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
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

# This is node 13
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) #btnGroupDrop1").click()
driver.find_element(By.LINK_TEXT, "Delete").click()
driver.find_element(By.ID, "confirm").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[6])

# This is node 17
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) #btnGroupDrop1").click()#1
driver.find_element(By.LINK_TEXT, "Edit").click()
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID,"dropdownMenuButton1").click()
safe_close(driver)
safe_close(driver)
driver.switch_to.window(handles[19])

# [duplicate]
index=19
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
driver.find_element(By.LINK_TEXT, "Report").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[19])

# [duplicate]
index=19
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
driver.find_element(By.ID, "dropdownMenuButton1").click()#2
driver.find_element(By.LINK_TEXT, "Manage Account").click()
driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys("admin123")
driver.find_element(By.ID, "old_password").click()
driver.find_element(By.ID, "old_password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, ".my-1").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[19])

# [duplicate]
index=19
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
driver.find_element(By.ID, "dropdownMenuButton1").click()#3
driver.find_element(By.LINK_TEXT, "Enrollees").click()
driver.find_element(By.ID, "btnGroupDrop1").click()
driver.find_element(By.LINK_TEXT, "Delete").click()
driver.find_element(By.ID, "confirm").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[19])

# [duplicate]
index=19
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
driver.find_element(By.ID, "dropdownMenuButton1").click()#5
driver.find_element(By.LINK_TEXT, "Enrollees").click()
driver.find_element(By.ID,  "btnGroupDrop1").click()
driver.find_element(By.LINK_TEXT, "Edit").click()
driver.find_element(By.ID, "status").click()
dropdown = driver.find_element(By.ID, "status")
dropdown.find_element(By.XPATH, "//option[. = 'Inactive']").click()
driver.find_element(By.CSS_SELECTOR, "#status > option:nth-child(2)").click()
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, ".mid-large .btn-secondary").click()
driver.find_element(By.ID,"dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[19])

# [duplicate]
index=19
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
driver.find_element(By.LINK_TEXT, "Online Entrance Exam System").click()
driver.find_element(By.LINK_TEXT, "Home").click()
driver.find_element(By.LINK_TEXT, "Enrollees").click()
driver.find_element(By.LINK_TEXT, "Report").click()
driver.find_element(By.LINK_TEXT, "Exam Set").click()
driver.find_element(By.LINK_TEXT, "Users").click()
driver.find_element(By.LINK_TEXT, "Maintenance").click()
driver.find_element(By.ID,  "dropdownMenuButton1").click()#1
driver.find_element(By.LINK_TEXT, "Manage Account").click()
driver.find_element(By.ID,"dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[19])

# [duplicate]
index=19
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
driver.find_element(By.ID, "dropdownMenuButton1").click()#7
driver.find_element(By.LINK_TEXT, "Enrollees").click()
driver.find_element(By.CSS_SELECTOR, "input").click()
driver.find_element(By.CSS_SELECTOR, "input").send_keys("test")
driver.find_element(By.CSS_SELECTOR, "input").send_keys(Keys.ENTER)
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[19])

# [duplicate]
index=19
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
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[19])

# This is node 23
driver.find_element(By.ID, "dropdownMenuButton1").click()#8
driver.find_element(By.LINK_TEXT, "Enrollees").click()
driver.find_element(By.ID, "btnGroupDrop1").click()
driver.find_element(By.LINK_TEXT, "View").click()
driver.find_element(By.CSS_SELECTOR, ".me-3").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
safe_close(driver)
driver.switch_to.window(handles[1])

# This is node 20
driver.find_element(By.ID, "password").send_keys("test123")
driver.find_element(By.ID, "username").send_keys("test")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
safe_close(driver)
safe_close(driver)
end=time.time()
print('time:%s s' % (end - start))
tlog(end - start)
