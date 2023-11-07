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
driver.get("http://1addressbook/")
driver.set_window_size(1175, 629)
driver.find_element(By.NAME, "user").send_keys("admin")
driver.find_element(By.NAME, "pass").send_keys("123")
driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
driver.find_element(By.NAME, "searchform").click()

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

# This is node 2
driver.find_element(By.LINK_TEXT, "next birthdays").click()
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

# This is node 3
driver.find_element(By.LINK_TEXT, "add new").click()
driver.find_element(By.NAME, "address").send_keys("hadspiashdp")
driver.find_element(By.CSS_SELECTOR, "form:nth-child(2) > input:nth-child(1)").click()
driver.find_element(By.NAME, "middlename").click()
driver.find_element(By.NAME, "middlename").send_keys("a")
driver.find_element(By.NAME, "lastname").click()
driver.find_element(By.NAME, "lastname").send_keys("s")
driver.find_element(By.NAME, "nickname").click()
driver.find_element(By.NAME, "nickname").send_keys("d")
driver.find_element(By.NAME, "title").click()
driver.find_element(By.NAME, "title").send_keys("aa")
driver.find_element(By.NAME, "company").click()
driver.find_element(By.NAME, "company").send_keys("aaaa")
driver.find_element(By.NAME, "home").click()
driver.find_element(By.NAME, "home").send_keys("a")
driver.find_element(By.NAME, "mobile").click()
driver.find_element(By.NAME, "mobile").send_keys("a")

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

# This is node 4
driver.find_element(By.NAME, "work").click() #1
driver.find_element(By.NAME, "work").send_keys("aaa")
driver.find_element(By.NAME, "theform").click()
driver.find_element(By.NAME, "fax").click()
driver.find_element(By.NAME, "fax").send_keys("aa")
driver.find_element(By.NAME, "address").click()
driver.find_element(By.NAME, "address").send_keys("aa")
driver.find_element(By.NAME, "email2").click()
driver.find_element(By.NAME, "email2").send_keys("aa")
driver.find_element(By.NAME, "email3").click()
driver.find_element(By.NAME, "email3").send_keys("a")
driver.find_element(By.NAME, "homepage").click()
driver.find_element(By.NAME, "homepage").send_keys("a")
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
driver.find_element(By.NAME, "notes").click()
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bday").click()
dropdown = driver.find_element(By.NAME, "bday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bmonth").click()
dropdown = driver.find_element(By.NAME, "bmonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(10)").click()
driver.find_element(By.NAME, "byear").click()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "aday").click()
dropdown = driver.find_element(By.NAME, "aday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(66) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "amonth").click()
dropdown = driver.find_element(By.NAME, "amonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(67) > option:nth-child(10)").click()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "new_group").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(71) > option:nth-child(1)").click()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "address2").click()
driver.find_element(By.NAME, "address2").send_keys("a")
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "notes").send_keys("aa")
driver.find_element(By.NAME, "phone2").click()
driver.find_element(By.NAME, "phone2").send_keys("a")
driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
driver.find_element(By.NAME, "searchstring").send_keys("aa")
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

# This is node 5
driver.find_element(By.NAME, "work").click() #10
driver.find_element(By.NAME, "work").send_keys("aaa")
driver.find_element(By.NAME, "theform").click()
driver.find_element(By.NAME, "fax").click()
driver.find_element(By.NAME, "fax").send_keys("aa")
driver.find_element(By.NAME, "address").click()
driver.find_element(By.NAME, "address").send_keys("aa")
driver.find_element(By.NAME, "email2").click()
driver.find_element(By.NAME, "email2").send_keys("aa")
driver.find_element(By.NAME, "email3").click()
driver.find_element(By.NAME, "email3").send_keys("a")
driver.find_element(By.NAME, "homepage").click()
driver.find_element(By.NAME, "homepage").send_keys("a")
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
driver.find_element(By.NAME, "notes").click()
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bday").click()
dropdown = driver.find_element(By.NAME, "bday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bmonth").click()
dropdown = driver.find_element(By.NAME, "bmonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(10)").click()
driver.find_element(By.NAME, "byear").click()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "aday").click()
dropdown = driver.find_element(By.NAME, "aday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(66) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "amonth").click()
dropdown = driver.find_element(By.NAME, "amonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(67) > option:nth-child(10)").click()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "new_group").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(71) > option:nth-child(1)").click()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "address2").click()
driver.find_element(By.NAME, "address2").send_keys("a")
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "notes").send_keys("aa")
driver.find_element(By.NAME, "phone2").click()
driver.find_element(By.NAME, "phone2").send_keys("a")
driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
driver.find_element(By.NAME, "searchstring").send_keys("aa")
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

# This is node 6
driver.find_element(By.NAME, "work").click() #2
driver.find_element(By.NAME, "work").send_keys("aaa")
driver.find_element(By.NAME, "theform").click()
driver.find_element(By.NAME, "fax").click()
driver.find_element(By.NAME, "fax").send_keys("aa")
driver.find_element(By.NAME, "address").click()
driver.find_element(By.NAME, "address").send_keys("aa")
driver.find_element(By.NAME, "email2").click()
driver.find_element(By.NAME, "email2").send_keys("aa")
driver.find_element(By.NAME, "email3").click()
driver.find_element(By.NAME, "email3").send_keys("a")
driver.find_element(By.NAME, "homepage").click()
driver.find_element(By.NAME, "homepage").send_keys("a")
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
driver.find_element(By.NAME, "notes").click()
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bday").click()
dropdown = driver.find_element(By.NAME, "bday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bmonth").click()
dropdown = driver.find_element(By.NAME, "bmonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(10)").click()
driver.find_element(By.NAME, "byear").click()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "aday").click()
dropdown = driver.find_element(By.NAME, "aday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(66) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "amonth").click()
dropdown = driver.find_element(By.NAME, "amonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(67) > option:nth-child(10)").click()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "new_group").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(71) > option:nth-child(1)").click()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "address2").click()
driver.find_element(By.NAME, "address2").send_keys("a")
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "notes").send_keys("aa")
driver.find_element(By.NAME, "phone2").click()
driver.find_element(By.NAME, "phone2").send_keys("a")
driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
driver.find_element(By.NAME, "searchstring").send_keys("aa")
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

# This is node 7
driver.find_element(By.NAME, "work").click() #3
driver.find_element(By.NAME, "work").send_keys("aaa")
driver.find_element(By.NAME, "theform").click()
driver.find_element(By.NAME, "fax").click()
driver.find_element(By.NAME, "fax").send_keys("aa")
driver.find_element(By.NAME, "address").click()
driver.find_element(By.NAME, "address").send_keys("aa")
driver.find_element(By.NAME, "email2").click()
driver.find_element(By.NAME, "email2").send_keys("aa")
driver.find_element(By.NAME, "email3").click()
driver.find_element(By.NAME, "email3").send_keys("a")
driver.find_element(By.NAME, "homepage").click()
driver.find_element(By.NAME, "homepage").send_keys("a")
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
driver.find_element(By.NAME, "notes").click()
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bday").click()
dropdown = driver.find_element(By.NAME, "bday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bmonth").click()
dropdown = driver.find_element(By.NAME, "bmonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(10)").click()
driver.find_element(By.NAME, "byear").click()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "aday").click()
dropdown = driver.find_element(By.NAME, "aday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(66) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "amonth").click()
dropdown = driver.find_element(By.NAME, "amonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(67) > option:nth-child(10)").click()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "new_group").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(71) > option:nth-child(1)").click()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "address2").click()
driver.find_element(By.NAME, "address2").send_keys("a")
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "notes").send_keys("aa")
driver.find_element(By.NAME, "phone2").click()
driver.find_element(By.NAME, "phone2").send_keys("a")
driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
driver.find_element(By.NAME, "searchstring").send_keys("aa")
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

# This is node 8
driver.find_element(By.NAME, "work").click() #4
driver.find_element(By.NAME, "work").send_keys("aaa")
driver.find_element(By.NAME, "theform").click()
driver.find_element(By.NAME, "fax").click()
driver.find_element(By.NAME, "fax").send_keys("aa")
driver.find_element(By.NAME, "address").click()
driver.find_element(By.NAME, "address").send_keys("aa")
driver.find_element(By.NAME, "email2").click()
driver.find_element(By.NAME, "email2").send_keys("aa")
driver.find_element(By.NAME, "email3").click()
driver.find_element(By.NAME, "email3").send_keys("a")
driver.find_element(By.NAME, "homepage").click()
driver.find_element(By.NAME, "homepage").send_keys("a")
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
driver.find_element(By.NAME, "notes").click()
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bday").click()
dropdown = driver.find_element(By.NAME, "bday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bmonth").click()
dropdown = driver.find_element(By.NAME, "bmonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(10)").click()
driver.find_element(By.NAME, "byear").click()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "aday").click()
dropdown = driver.find_element(By.NAME, "aday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(66) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "amonth").click()
dropdown = driver.find_element(By.NAME, "amonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(67) > option:nth-child(10)").click()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "new_group").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(71) > option:nth-child(1)").click()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "address2").click()
driver.find_element(By.NAME, "address2").send_keys("a")
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "notes").send_keys("aa")
driver.find_element(By.NAME, "phone2").click()
driver.find_element(By.NAME, "phone2").send_keys("a")
driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
driver.find_element(By.NAME, "searchstring").send_keys("aa")
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

# This is node 9
driver.find_element(By.NAME, "work").click() #5
driver.find_element(By.NAME, "work").send_keys("aaa")
driver.find_element(By.NAME, "theform").click()
driver.find_element(By.NAME, "fax").click()
driver.find_element(By.NAME, "fax").send_keys("aa")
driver.find_element(By.NAME, "address").click()
driver.find_element(By.NAME, "address").send_keys("aa")
driver.find_element(By.NAME, "email2").click()
driver.find_element(By.NAME, "email2").send_keys("aa")
driver.find_element(By.NAME, "email3").click()
driver.find_element(By.NAME, "email3").send_keys("a")
driver.find_element(By.NAME, "homepage").click()
driver.find_element(By.NAME, "homepage").send_keys("a")
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
driver.find_element(By.NAME, "notes").click()
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bday").click()
dropdown = driver.find_element(By.NAME, "bday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bmonth").click()
dropdown = driver.find_element(By.NAME, "bmonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(10)").click()
driver.find_element(By.NAME, "byear").click()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "aday").click()
dropdown = driver.find_element(By.NAME, "aday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(66) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "amonth").click()
dropdown = driver.find_element(By.NAME, "amonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(67) > option:nth-child(10)").click()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "new_group").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(71) > option:nth-child(1)").click()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "address2").click()
driver.find_element(By.NAME, "address2").send_keys("a")
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "notes").send_keys("aa")
driver.find_element(By.NAME, "phone2").click()
driver.find_element(By.NAME, "phone2").send_keys("a")
driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
driver.find_element(By.NAME, "searchstring").send_keys("aa")
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

# This is node 10
driver.find_element(By.NAME, "work").click() #6
driver.find_element(By.NAME, "work").send_keys("aaa")
driver.find_element(By.NAME, "theform").click()
driver.find_element(By.NAME, "fax").click()
driver.find_element(By.NAME, "fax").send_keys("aa")
driver.find_element(By.NAME, "address").click()
driver.find_element(By.NAME, "address").send_keys("aa")
driver.find_element(By.NAME, "email2").click()
driver.find_element(By.NAME, "email2").send_keys("aa")
driver.find_element(By.NAME, "email3").click()
driver.find_element(By.NAME, "email3").send_keys("a")
driver.find_element(By.NAME, "homepage").click()
driver.find_element(By.NAME, "homepage").send_keys("a")
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
driver.find_element(By.NAME, "notes").click()
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bday").click()
dropdown = driver.find_element(By.NAME, "bday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bmonth").click()
dropdown = driver.find_element(By.NAME, "bmonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(10)").click()
driver.find_element(By.NAME, "byear").click()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "aday").click()
dropdown = driver.find_element(By.NAME, "aday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(66) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "amonth").click()
dropdown = driver.find_element(By.NAME, "amonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(67) > option:nth-child(10)").click()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "new_group").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(71) > option:nth-child(1)").click()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "address2").click()
driver.find_element(By.NAME, "address2").send_keys("a")
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "notes").send_keys("aa")
driver.find_element(By.NAME, "phone2").click()
driver.find_element(By.NAME, "phone2").send_keys("a")
driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
driver.find_element(By.NAME, "searchstring").send_keys("aa")
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

# This is node 11
driver.find_element(By.NAME, "work").click() #7
driver.find_element(By.NAME, "work").send_keys("aaa")
driver.find_element(By.NAME, "theform").click()
driver.find_element(By.NAME, "fax").click()
driver.find_element(By.NAME, "fax").send_keys("aa")
driver.find_element(By.NAME, "address").click()
driver.find_element(By.NAME, "address").send_keys("aa")
driver.find_element(By.NAME, "email2").click()
driver.find_element(By.NAME, "email2").send_keys("aa")
driver.find_element(By.NAME, "email3").click()
driver.find_element(By.NAME, "email3").send_keys("a")
driver.find_element(By.NAME, "homepage").click()
driver.find_element(By.NAME, "homepage").send_keys("a")
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
driver.find_element(By.NAME, "notes").click()
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bday").click()
dropdown = driver.find_element(By.NAME, "bday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bmonth").click()
dropdown = driver.find_element(By.NAME, "bmonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(10)").click()
driver.find_element(By.NAME, "byear").click()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "aday").click()
dropdown = driver.find_element(By.NAME, "aday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(66) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "amonth").click()
dropdown = driver.find_element(By.NAME, "amonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(67) > option:nth-child(10)").click()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "new_group").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(71) > option:nth-child(1)").click()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "address2").click()
driver.find_element(By.NAME, "address2").send_keys("a")
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "notes").send_keys("aa")
driver.find_element(By.NAME, "phone2").click()
driver.find_element(By.NAME, "phone2").send_keys("a")
driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
driver.find_element(By.NAME, "searchstring").send_keys("aa")
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

# This is node 12
driver.find_element(By.NAME, "work").click() #8
driver.find_element(By.NAME, "work").send_keys("aaa")
driver.find_element(By.NAME, "theform").click()
driver.find_element(By.NAME, "fax").click()
driver.find_element(By.NAME, "fax").send_keys("aa")
driver.find_element(By.NAME, "address").click()
driver.find_element(By.NAME, "address").send_keys("aa")
driver.find_element(By.NAME, "email2").click()
driver.find_element(By.NAME, "email2").send_keys("aa")
driver.find_element(By.NAME, "email3").click()
driver.find_element(By.NAME, "email3").send_keys("a")
driver.find_element(By.NAME, "homepage").click()
driver.find_element(By.NAME, "homepage").send_keys("a")
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
driver.find_element(By.NAME, "notes").click()
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bday").click()
dropdown = driver.find_element(By.NAME, "bday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bmonth").click()
dropdown = driver.find_element(By.NAME, "bmonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(10)").click()
driver.find_element(By.NAME, "byear").click()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "aday").click()
dropdown = driver.find_element(By.NAME, "aday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(66) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "amonth").click()
dropdown = driver.find_element(By.NAME, "amonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(67) > option:nth-child(10)").click()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "new_group").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(71) > option:nth-child(1)").click()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "address2").click()
driver.find_element(By.NAME, "address2").send_keys("a")
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "notes").send_keys("aa")
driver.find_element(By.NAME, "phone2").click()
driver.find_element(By.NAME, "phone2").send_keys("a")
driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
driver.find_element(By.NAME, "searchstring").send_keys("aa")
safe_close(driver)
driver.switch_to.window(handles[3])

# This is node 13
driver.find_element(By.NAME, "work").click() #9
driver.find_element(By.NAME, "work").send_keys("aaa")
driver.find_element(By.NAME, "theform").click()
driver.find_element(By.NAME, "fax").click()
driver.find_element(By.NAME, "fax").send_keys("aa")
driver.find_element(By.NAME, "address").click()
driver.find_element(By.NAME, "address").send_keys("aa")
driver.find_element(By.NAME, "email2").click()
driver.find_element(By.NAME, "email2").send_keys("aa")
driver.find_element(By.NAME, "email3").click()
driver.find_element(By.NAME, "email3").send_keys("a")
driver.find_element(By.NAME, "homepage").click()
driver.find_element(By.NAME, "homepage").send_keys("a")
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
driver.find_element(By.NAME, "notes").click()
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bday").click()
dropdown = driver.find_element(By.NAME, "bday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "bmonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "bmonth").click()
dropdown = driver.find_element(By.NAME, "bmonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(10)").click()
driver.find_element(By.NAME, "byear").click()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "aday")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "aday").click()
dropdown = driver.find_element(By.NAME, "aday")
dropdown.find_element(By.XPATH, "//option[. = '7']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(66) > option:nth-child(9)").click()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "amonth")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "amonth").click()
dropdown = driver.find_element(By.NAME, "amonth")
dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(67) > option:nth-child(10)").click()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "new_group")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "new_group").click()
driver.find_element(By.CSS_SELECTOR, "select:nth-child(71) > option:nth-child(1)").click()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.NAME, "notes")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "address2").click()
driver.find_element(By.NAME, "address2").send_keys("a")
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "notes").send_keys("aa")
driver.find_element(By.NAME, "phone2").click()
driver.find_element(By.NAME, "phone2").send_keys("a")
driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
driver.find_element(By.NAME, "searchstring").send_keys("aa")
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
driver.find_element(By.ID, "4").click()
driver.find_element(By.CSS_SELECTOR, ".left:nth-child(8) > input").click()
assert driver.switch_to.alert.text == "Delete 1 addresses?"
driver.switch_to.alert.accept()
safe_close(driver)
driver.switch_to.window(handles[1])

# This is node 15
driver.find_element(By.CSS_SELECTOR, "td.center:nth-child(8) > a:nth-child(1) > img:nth-child(1)").click()
driver.find_element(By.NAME, "middlename").click()
driver.find_element(By.NAME, "firstname").click()
driver.find_element(By.NAME, "firstname").send_keys("b")
driver.find_element(By.NAME, "middlename").click()
driver.find_element(By.NAME, "middlename").send_keys("b")
driver.find_element(By.NAME, "lastname").click()
driver.find_element(By.NAME, "lastname").send_keys("b")
driver.find_element(By.NAME, "nickname").click()
driver.find_element(By.NAME, "nickname").send_keys("b")
driver.find_element(By.NAME, "company").click()
driver.find_element(By.NAME, "company").send_keys("b")
driver.find_element(By.NAME, "title").click()
driver.find_element(By.NAME, "title").send_keys("b")
driver.find_element(By.NAME, "address").click()
driver.find_element(By.NAME, "address").send_keys("b")
driver.find_element(By.NAME, "home").click()
driver.find_element(By.NAME, "home").send_keys("b")
driver.find_element(By.NAME, "mobile").click()
driver.find_element(By.NAME, "mobile").send_keys("b")
driver.find_element(By.NAME, "work").click() #
driver.find_element(By.NAME, "work").send_keys("b")
driver.find_element(By.NAME, "fax").click()
driver.find_element(By.NAME, "fax").send_keys("b")
driver.find_element(By.NAME, "email").click()
driver.find_element(By.NAME, "email").send_keys("b")
driver.find_element(By.NAME, "email2").click()
driver.find_element(By.NAME, "email2").send_keys("b")
driver.find_element(By.NAME, "email3").click()
driver.find_element(By.NAME, "email3").send_keys("b")
driver.find_element(By.NAME, "homepage").click()
driver.find_element(By.NAME, "homepage").send_keys("b")
driver.find_element(By.NAME, "address2").click()
driver.find_element(By.NAME, "address2").send_keys("b")
driver.find_element(By.NAME, "phone2").click()
driver.find_element(By.NAME, "phone2").send_keys("b")
driver.find_element(By.NAME, "notes").click()
driver.find_element(By.NAME, "notes").send_keys("b")
driver.find_element(By.CSS_SELECTOR, "input:nth-child(86)").click()
driver.find_element(By.NAME, "searchstring").send_keys("b")
safe_close(driver)
safe_close(driver)
end=time.time()
print('time:%s s' % (end - start))
tlog(end - start)
