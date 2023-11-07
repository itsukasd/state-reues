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
driver.get("http://sqgs/login.php")
driver.set_window_size(1550, 830)
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, ".card-body").click()
driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys("admin123")
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

# This is node 8
driver.find_element(By.LINK_TEXT, "Assessments").click()

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

# This is node 2
driver.find_element(By.ID, "create_new").click()
driver.find_element(By.ID, "select2-class_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"English 7 - A")]').click()
driver.find_element(By.ID, "select2-component_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"Written")]').click()
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "hps").click()
driver.find_element(By.ID, "hps").send_keys("11")
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
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

# This is node 3
driver.find_element(By.ID, "create_new").click() #2
driver.find_element(By.ID, "select2-class_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"English 7 - A")]').click()
driver.find_element(By.ID, "select2-component_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"Written")]').click()
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "hps").click()
driver.find_element(By.ID, "hps").send_keys("11")
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
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

# This is node 4
driver.find_element(By.ID, "create_new").click() #3
driver.find_element(By.ID, "select2-class_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"English 7 - A")]').click()
driver.find_element(By.ID, "select2-component_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"Written")]').click()
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "hps").click()
driver.find_element(By.ID, "hps").send_keys("11")
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
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

# This is node 5
driver.find_element(By.ID, "create_new").click() #4
driver.find_element(By.ID, "select2-class_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"English 7 - A")]').click()
driver.find_element(By.ID, "select2-component_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"Written")]').click()
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "hps").click()
driver.find_element(By.ID, "hps").send_keys("11")
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
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

# This is node 6
driver.find_element(By.ID, "create_new").click() #5
driver.find_element(By.ID, "select2-class_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"English 7 - A")]').click()
driver.find_element(By.ID, "select2-component_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"Written")]').click()
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "hps").click()
driver.find_element(By.ID, "hps").send_keys("11")
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
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

# This is node 7
driver.find_element(By.ID, "create_new").click() #6
driver.find_element(By.ID, "select2-class_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"English 7 - A")]').click()
driver.find_element(By.ID, "select2-component_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"Written")]').click()
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "hps").click()
driver.find_element(By.ID, "hps").send_keys("11")
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
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

# This is node 43
driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(7) #btnGroupDrop1").click()
driver.find_element(By.LINK_TEXT, "Delete").click()
driver.find_element(By.ID, "confirm").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
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

# This is node 48
driver.find_element(By.ID, "btnGroupDrop1").click()
driver.find_element(By.LINK_TEXT, "Edit").click()
element = driver.find_element(By.CSS_SELECTOR, ".even:nth-child(2) #btnGroupDrop1")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.CSS_SELECTOR, ".even:nth-child(2) #btnGroupDrop1").click()
driver.find_element(By.LINK_TEXT, "Edit").click()
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.ID, "submit")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[8])

# This is node 55
driver.find_element(By.CSS_SELECTOR, "input").click()
driver.find_element(By.CSS_SELECTOR, "input").send_keys("test")
driver.find_element(By.CSS_SELECTOR, "input").send_keys(Keys.ENTER)
driver.find_element(By.ID, "dropdownMenuButton1").click()
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

# This is node 9
driver.find_element(By.LINK_TEXT, "Class").click()

# [duplicate]
index=9
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
driver.find_element(By.ID, "create_new").click()
driver.find_element(By.ID, "select2-subject_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"Math")]').click()
driver.find_element(By.ID, "grade").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "section").click()
driver.find_element(By.ID, "section").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.ID, "submit")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[9])

# [duplicate]
index=9
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
driver.find_element(By.ID, "create_new").click() #2
driver.find_element(By.ID, "select2-subject_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"Math")]').click()
driver.find_element(By.ID, "grade").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "section").click()
driver.find_element(By.ID, "section").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.ID, "submit")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[9])

# [duplicate]
index=9
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
driver.find_element(By.ID, "create_new").click() #3
driver.find_element(By.ID, "select2-subject_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"Math")]').click()
driver.find_element(By.ID, "grade").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "section").click()
driver.find_element(By.ID, "section").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.ID, "submit")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[9])

# [duplicate]
index=9
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
driver.find_element(By.ID, "create_new").click() #4
driver.find_element(By.ID, "select2-subject_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"Math")]').click()
driver.find_element(By.ID, "grade").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "section").click()
driver.find_element(By.ID, "section").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.ID, "submit")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[9])

# [duplicate]
index=9
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
driver.find_element(By.ID, "create_new").click() #5
driver.find_element(By.ID, "select2-subject_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"Math")]').click()
driver.find_element(By.ID, "grade").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "section").click()
driver.find_element(By.ID, "section").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.ID, "submit")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[9])

# [duplicate]
index=9
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
driver.find_element(By.ID, "create_new").click() #6
driver.find_element(By.ID, "select2-subject_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"Math")]').click()
driver.find_element(By.ID, "grade").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "section").click()
driver.find_element(By.ID, "section").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.ID, "submit")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[9])

# [duplicate]
index=9
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

# This is node 44
driver.find_element(By.CSS_SELECTOR, ".even:nth-child(8) #btnGroupDrop1").click()
driver.find_element(By.LINK_TEXT, "Delete").click()
driver.find_element(By.ID, "confirm").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[9])

# This is node 56
driver.find_element(By.CSS_SELECTOR, "input").click()
driver.find_element(By.CSS_SELECTOR, "input").send_keys("mm")
driver.find_element(By.CSS_SELECTOR, "input").send_keys(Keys.ENTER)
driver.find_element(By.ID, "dropdownMenuButton1").click()
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

# This is node 16
driver.find_element(By.LINK_TEXT, "Maintenance").click()

# [duplicate]
index=16
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
driver.find_element(By.ID, "new_component").click()
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.ID, "submit")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[16])

# [duplicate]
index=16
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
driver.find_element(By.ID, "new_component").click() #2
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.ID, "submit")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[16])

# [duplicate]
index=16
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
driver.find_element(By.ID, "new_component").click() #3
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.ID, "submit")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[16])

# [duplicate]
index=16
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
driver.find_element(By.ID, "new_component").click() #4
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.ID, "submit")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[16])

# [duplicate]
index=16
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
driver.find_element(By.ID, "new_component").click() #5
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.ID, "submit")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[16])

# [duplicate]
index=16
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
driver.find_element(By.ID, "new_component").click() #6
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.ID, "submit")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[16])

# [duplicate]
index=16
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

# This is node 30
driver.find_element(By.CSS_SELECTOR, "#new_subject > .svg-inline--fa").click()
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[16])

# [duplicate]
index=16
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

# This is node 31
driver.find_element(By.CSS_SELECTOR, "#new_subject > .svg-inline--fa").click()#2
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[16])

# [duplicate]
index=16
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

# This is node 32
driver.find_element(By.CSS_SELECTOR, "#new_subject > .svg-inline--fa").click()#3
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[16])

# [duplicate]
index=16
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

# This is node 33
driver.find_element(By.CSS_SELECTOR, "#new_subject > .svg-inline--fa").click()#4
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[16])

# [duplicate]
index=16
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

# This is node 34
driver.find_element(By.CSS_SELECTOR, "#new_subject > .svg-inline--fa").click()#5
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[16])

# [duplicate]
index=16
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

# This is node 35
driver.find_element(By.CSS_SELECTOR, "#new_subject > .svg-inline--fa").click()#6
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[16])

# [duplicate]
index=16
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

# This is node 45
driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(3) .delete_component").click()
driver.find_element(By.ID, "confirm").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[16])

# [duplicate]
index=16
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

# This is node 47
driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(4) .delete_subject path").click()
driver.find_element(By.ID, "confirm").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[16])

# [duplicate]
index=16
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

# This is node 49
driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(5) .edit_component").click()
driver.find_element(By.ID, "submit").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(4) .edit_component > .svg-inline--fa").click()
element = driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(4) .edit_component > .svg-inline--fa")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.ID, "submit")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[16])

# This is node 51
driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(1) .edit_subject path").click()
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.ID, "submit")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(2) .edit_subject > .svg-inline--fa").click()
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.ID, "submit")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
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

# This is node 23
driver.find_element(By.LINK_TEXT, "Students").click()

# [duplicate]
index=23
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
driver.find_element(By.ID, "create_new").click()
driver.find_element(By.ID, "select2-class_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"English 7 - A")]').click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[23])

# [duplicate]
index=23
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
driver.find_element(By.ID, "create_new").click()#2
driver.find_element(By.ID, "select2-class_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"English 7 - A")]').click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[23])

# [duplicate]
index=23
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
driver.find_element(By.ID, "create_new").click()#3
driver.find_element(By.ID, "select2-class_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"English 7 - A")]').click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[23])

# [duplicate]
index=23
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

# This is node 27
driver.find_element(By.ID, "create_new").click()#4
driver.find_element(By.ID, "select2-class_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"English 7 - A")]').click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[23])

# [duplicate]
index=23
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
driver.find_element(By.ID, "create_new").click()#5
driver.find_element(By.ID, "select2-class_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"English 7 - A")]').click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[23])

# [duplicate]
index=23
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
driver.find_element(By.ID, "create_new").click()#6
driver.find_element(By.ID, "select2-class_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"English 7 - A")]').click()
driver.find_element(By.ID, "name").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[23])

# [duplicate]
index=23
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

# This is node 46
driver.find_element(By.CSS_SELECTOR, ".even:nth-child(8) #btnGroupDrop1").click()
driver.find_element(By.LINK_TEXT, "Delete").click()
driver.find_element(By.ID, "confirm").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[23])

# [duplicate]
index=23
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

# This is node 50
driver.find_element(By.ID, "btnGroupDrop1").click()
driver.find_element(By.LINK_TEXT, "Edit").click()
element = driver.find_element(By.CSS_SELECTOR, ".even:nth-child(2) #btnGroupDrop1")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.CSS_SELECTOR, ".even:nth-child(2) #btnGroupDrop1").click()
driver.find_element(By.LINK_TEXT, "Edit").click()
element = driver.find_element(By.CSS_SELECTOR, ".even:nth-child(4) #btnGroupDrop1")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(3) #btnGroupDrop1").click()
driver.find_element(By.LINK_TEXT, "Edit").click()
element = driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(5) #btnGroupDrop1")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[23])

# This is node 57
driver.find_element(By.CSS_SELECTOR, "input").click()
driver.find_element(By.CSS_SELECTOR, "input").send_keys("test")
driver.find_element(By.CSS_SELECTOR, "input").send_keys(Keys.ENTER)
driver.find_element(By.ID, "dropdownMenuButton1").click()
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

# This is node 36
driver.find_element(By.LINK_TEXT, "Users").click()

# [duplicate]
index=36
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

# This is node 37
driver.find_element(By.ID, "create_new").click()
element = driver.find_element(By.ID, "create_new")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.ID, "fullname").click()
driver.find_element(By.ID, "fullname").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[36])

# [duplicate]
index=36
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

# This is node 38
driver.find_element(By.ID, "create_new").click()#2
element = driver.find_element(By.ID, "create_new")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.ID, "fullname").click()
driver.find_element(By.ID, "fullname").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[36])

# [duplicate]
index=36
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

# This is node 39
driver.find_element(By.ID, "create_new").click()#3
element = driver.find_element(By.ID, "create_new")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.ID, "fullname").click()
driver.find_element(By.ID, "fullname").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[36])

# [duplicate]
index=36
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

# This is node 40
driver.find_element(By.ID, "create_new").click()#4
element = driver.find_element(By.ID, "create_new")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.ID, "fullname").click()
driver.find_element(By.ID, "fullname").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[36])

# [duplicate]
index=36
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

# This is node 41
driver.find_element(By.ID, "create_new").click()#5
element = driver.find_element(By.ID, "create_new")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.ID, "fullname").click()
driver.find_element(By.ID, "fullname").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[36])

# [duplicate]
index=36
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

# This is node 42
driver.find_element(By.ID, "create_new").click()#6
element = driver.find_element(By.ID, "create_new")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.ID, "fullname").click()
driver.find_element(By.ID, "fullname").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys(random.sample('abcdefg123',10))
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[36])

# This is node 52
driver.find_element(By.ID, "btnGroupDrop1").click()
driver.find_element(By.LINK_TEXT, "Edit").click()
element = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) #btnGroupDrop1")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.ID, "submit")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) #btnGroupDrop1").click()
driver.find_element(By.LINK_TEXT, "Edit").click()
element = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) #btnGroupDrop1")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.ID, "submit").click()
element = driver.find_element(By.ID, "submit")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, "#uni_modal .btn-secondary").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
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

# This is node 53
driver.find_element(By.LINK_TEXT, "Marks").click()
driver.find_element(By.ID, "select2-class_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"Science 7 - C")]').click()
driver.find_element(By.ID, "select2-assessment_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"First - P1")]').click()
driver.find_element(By.ID, "filter").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
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

# This is node 54
driver.find_element(By.LINK_TEXT, "Report").click()
driver.find_element(By.ID, "select2-class_id-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"Science 7 - C")]').click()
driver.find_element(By.ID, "select2-quarter-container").click()
driver.find_element(By.XPATH, '//*/span/ul/li[contains(text(),"Second")]').click()
driver.find_element(By.ID, "filter").click()
driver.find_element(By.ID, "transmuted_table").click()
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
driver.switch_to.window(handles[1])

# This is node 58
driver.find_element(By.ID, "dropdownMenuButton1").click()
safe_close(driver)
safe_close(driver)
end=time.time()
print('time:%s s' % (end - start))
tlog(end - start)
