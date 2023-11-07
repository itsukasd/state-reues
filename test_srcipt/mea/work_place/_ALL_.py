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
driver.get("http://mea/")
driver.find_element(By.ID, "identifiant_connexion").send_keys("admin")
driver.find_element(By.ID, "password_connexion").send_keys("admin")
driver.find_element(By.ID, "bouton_connexion").click()
time.sleep(0.5)

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
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test1")
driver.find_element(By.ID, "prenom").send_keys("test1")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_membre_fermer").click()
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
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 4
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click() #10
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#11
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#12
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#13
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#14
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#15
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 10
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#16
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 11
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#17
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 12
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#18
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 13
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#19
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click() #2
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#20
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#21
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 17
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#22
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 18
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#23
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#24
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#25
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#26
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 22
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#27
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#28
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 24
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#29
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 25
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click() #3
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 26
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#30
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 27
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#31
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 28
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#32
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 29
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#33
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 30
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#34
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 31
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#35
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 32
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#36
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 33
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#37
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 34
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#38
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 35
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#39
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click() #4
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 37
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#40
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 38
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click() #5
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 39
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click() #6
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 40
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click() #7
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 41
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click() #8
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
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

# This is node 42
driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click() #9
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.ID, "nom").send_keys("test")
driver.find_element(By.ID, "race").send_keys("test")
driver.find_element(By.ID, "date_naissance").send_keys("1")
driver.find_element(By.ID, "bouton_animal_fermer").click()
safe_close(driver)
driver.switch_to.window(handles[1])

# This is node 43
driver.find_element(By.CSS_SELECTOR, "input").click()
driver.find_element(By.CSS_SELECTOR, "input").send_keys("test1")
safe_close(driver)
safe_close(driver)
end=time.time()
print('time:%s s' % (end - start))
tlog(end - start)
