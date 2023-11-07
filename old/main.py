import pytest
import time
import json
import os
import re
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import psutil
import win32gui
import win32api
import win32con
import win32process
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

class TrieNode:
    def __init__(self):
        self.children = []
        self.context = []
        self.index = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.root.context.append("# THIS IS VIRTUAL ROOT\n")
        self.cnt = 0
        self.root.index=self.cnt
        self.cnt=self.cnt+1
        # root node is empty, possesses index 0

    def insert_extracted_list(self, extract_list):
        extract_list=self.checklist(extract_list)
        root = self.root
        if len(root.children) == 0:
            c0=TrieNode()
            c0.context=extract_list
            c0.index=self.cnt
            self.cnt=self.cnt+1
            root.children.append(c0)
            return True
        else:
            for c in root.children:
                # ok=1 success ok=0 should try to add next 0k=-1 error
                ok=self.insert(c,extract_list)
                if ok==1:
                    return True
                elif ok==0:
                    continue
                else:
                    assert 0
            # create a new children
            newNode=TrieNode()
            newNode.context=extract_list
            newNode.index=self.cnt
            self.cnt=self.cnt+1
            root.children.append(newNode)
            return True

    def insert(self,node,ls):
        this_node_len=len(node.context)
        assert this_node_len != 0
        if self.compare_line(node.context[0],ls[0]) is False:
            # should try to add next
            return 0
        # totally same=0  partial same=1  left < right=2  left > right=3
        (rst,first_unsame_index)=self.compare_lists(node.context,ls)
        if rst==0:
            return 1
        elif rst==1:
            # pre part
            lnode=TrieNode()
            lnode.index=self.cnt
            self.cnt=self.cnt+1
            lnode.context=node.context[first_unsame_index:]
            lnode.children=node.children
            # new part
            rnode=TrieNode()
            rnode.index=self.cnt
            self.cnt=self.cnt+1
            rnode.context=ls[first_unsame_index:]
            # same part
            node.context=node.context[:first_unsame_index]
            node.children=[]
            node.children.append(lnode)
            node.children.append(rnode)
            return 1
        elif rst==2:
            #need to compare children
            if len(node.children) == 0:
                newNode=TrieNode()
                newNode.index=self.cnt
                self.cnt=self.cnt+1
                newNode.context=ls[this_node_len:]
                node.children.append(newNode)
                return 1
            else:
                for c in node.children:
                    ok=self.insert(c,ls[this_node_len:])
                    if ok==1:
                        return 1
                    elif ok==0:
                        continue
                    else:
                        assert 0
                newNode=TrieNode()
                newNode.index=self.cnt
                self.cnt=self.cnt+1
                newNode.context=ls[this_node_len:]
                node.children.append(newNode)
                return 1
        elif rst==3:
            #temporally I consider it reducdent
            return 1
        else:
            assert 0

    def compare_line(self,line1,line2):
        assert line1.strip() != ""
        assert line2.strip() != ""
        if line1==line2:
            return True
        return False

    def compare_lists(self,ls1,ls2):
        if self.compare_line(ls1[0],ls2[0]) is False:
            assert 0
        # unexpected: first line shouldn't same
        len1=len(ls1)
        len2=len(ls2)
        mlen=min(len1,len2)
        for i in range(mlen):
            if self.compare_line(ls1[i],ls2[i]) is False:
                return (1,i)
        if len1==len2:
            return (0,-1)
        elif len1<len2:
            return (2,-1)
        else:
            return (3,-1)

    def checklist(self,extract_list):
        # the extract list is almost same compared with
        # the initial test file. We want to do some 
        # modification with it
        extract_list=extract_list
        # things could do:
        # 1 indivisible code block
        # 2 always wrong sentence
        return extract_list

def create_work_path(input_testcase_dir):
    abspath = os.path.abspath(input_testcase_dir)
    work_path = os.path.join(abspath,'work_place')
    if os.path.exists(work_path):
        shutil.rmtree(work_path)
    os.mkdir(work_path)
    extract_path=os.path.join(work_path,'_extract_')
    os.mkdir(extract_path)
    single_path=os.path.join(work_path,'_single_')
    os.mkdir(single_path)
    return work_path

def examLine(line):
    assert line is not None
    if line.strip()=="":
        return "#SKIP"
    # now the line is no empty

    empty_char_pattern=re.compile(r'\s')
    ch=empty_char_pattern.match(line)
    if ch is None:
        return "#FINISH"
    # if no space in the front of line, consider the func over

    defined_fini_pattern=re.compile(r'.*##\$##.*')
    defined_fini=defined_fini_pattern.match(line)
    if defined_fini is not None:
        return "#FINISH"
    # user-define finish

    line= line.strip()
    comment_char_pattern=re.compile(r'#')
    comment_char=comment_char_pattern.match(line)
    if comment_char is not None:
        return "#SKIP"
    # command line is not expected

    assert line !=""
    line=line.replace('self.driver','driver')
    return line

def get_test_name(filepath):
    basefilename=os.path.basename(filepath)
    test_name_pattern = re.compile(r'\S+(?=.py$)')
    re_testname=test_name_pattern.match(basefilename)
    assert re_testname is not None
    testname=re_testname.group()
    return testname

def extractpy(filepath):
    testname=get_test_name(filepath)
    print('\n\033[0;35m<',testname,'>\033[0m\n')
    f=open(filepath, "r")
    # match the start of the extracted function | expect < def testname ( ) : >
    func_name_pattern=re.compile(r'def +'+testname+' *\(.*\) *: *')
    lines=f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        if func_name_pattern.match(lines[i]):
            print("[%s]\tfunc start found:\t\033[0;34m%s\033[0m\t" % (testname,lines[i]))
            assert i < len(lines)
            nlines=lines[i+1:]
            break
        if i==len(lines):
            print("[%s] unable to find the location to extract code" % filepath)
            assert 0
    # now we exam the code line by line
    extractList=[]
    for i in range(len(nlines)):
        ret=examLine(nlines[i])
        if ret != "#FINISH" and ret != "#SKIP":
            extractList.append(ret)
            #add to extractList
            print("[%s]\textract (line:%s)\t\033[0;34m%s\033[0m" % (testname,str(i),ret))
        if ret == "#FINISH" or i==len(nlines):
            print("[%s] extract finished" % testname)
            break
    return extractList

def generate_extract_file(in_path,out_path):
    testname=get_test_name(in_path)
    extract_file_name="_extract_"+testname+".zy"
    extract_file_absolute=os.path.join(out_path,extract_file_name)
    ls=extractpy(in_path)
    f=open(extract_file_absolute, "w")
    for line in ls:
        f.write(line+"\n")
    f.close()

def get_extract_file_paths(out_path):
    file_paths=[]
    for root,dirs,files in os.walk(out_path):
        for file in files:
            if file.endswith('.zy'):
                file_path=os.path.join(root,file)
                file_paths.append(file_path)
    return file_paths

def extract_file_2_list(file_path):
    f=open(file_path, "r")
    lines=f.readlines()
    return lines

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

def out_init_env(out_file):
    InitCodeFile="./Initcode.txt"
    Initls=extract_file_2_list(InitCodeFile)
    for line in Initls:
        out_file.write(line)

def out_duplicate_sentence(out_file,key):
    out_file.write("\n# [duplicate]\n")
    out_file.write("index=%s\n" % key)
    dupCodeFile="./dupcode.txt"
    dupls=extract_file_2_list(dupCodeFile)    
    for line in dupls:
        out_file.write(line)
    out_file.write("\n# [duplicate over]\n")         

def out_generate(trie,out_file):
    out_file.write("\n# This is auto-generated execution code\n\n")
    root=trie.root
    assert len(root.children) != 0
    recurse_generate(root,out_file)

def recurse_generate(father,out_file):
    assert len(father.context) != 0
    out_file.write("\n# This is node %s\n" % father.index)
    for line in father.context:
        out_file.write("driver.implicitly_wait(10)\n")
        out_file.write(line)
    ccnt=len(father.children)
    if ccnt != 0:
        for i in range(ccnt):
            if father.index and i < ccnt - 1 :
                # root and last needn't duplicate
                out_duplicate_sentence(out_file,father.index)
                recurse_generate(father.children[i],out_file)
                out_file.write("safe_close(driver)\n")
                out_file.write("driver.implicitly_wait(10)\n")
                out_file.write("driver.switch_to.window(handles[%s])\n" % father.index)
            else:
                # out_file.write("time.sleep(0.5)\n")
                recurse_generate(father.children[ccnt-1],out_file)
                # out_file.write("time.sleep(1)\n")
                out_file.write("safe_close(driver)\n")

def generate_single_test_file(in_file_path,out_path):
    out_file=open(out_path,'w')
    lines = extract_file_2_list(in_file_path)
    out_init_env(out_file)
    out_file.write('start=time.time()\n')
    for line in lines:
        out_file.write('driver.implicitly_wait(10)\n')
        out_file.write(line)
    out_file.write('end=time.time()\n')
    out_file.write("safe_close(driver)\n")
    out_file.write("print('time:%s s' % (end - start))")

if __name__=="__main__":

    #workplace
    testcase_in_dir=r'D:\preixTree\test_srcipt\sqgs_new'
    work_path = create_work_path(testcase_in_dir)
    extract_path=os.path.join(work_path,'_extract_')
    single_path=os.path.join(work_path,'_single_')
    print("workplace established")

    #extract
    for root,dirs,files in os.walk(testcase_in_dir):
        for file in files:
            if file.endswith('.py'):
                file_path=os.path.join(root,file)
                generate_extract_file(file_path,extract_path)
    print("All the files have extracted")

    #single file test
    extract_file_paths = get_extract_file_paths(extract_path)
    for file_path in extract_file_paths:
        file_name=os.path.basename(file_path)
        n_file_name='_singleTest_'+file_name+'.py'
        out_path=os.path.join(single_path,n_file_name)
        generate_single_test_file(file_path,out_path)
        # exec(open(out_path).read())

    #construct
    trie = Trie()
    extract_file_paths = get_extract_file_paths(extract_path)
    for file_path in extract_file_paths:
        lines = extract_file_2_list(file_path)
        trie.insert_extracted_list(lines)
    print("All the files have inserted into the tree")

    #generate
    out_file_path = os.path.join(work_path,'_ALL_.py')
    out_file=open(out_file_path, "w")
    out_init_env(out_file)
    out_file.write('start=time.time()\n')
    out_generate(trie,out_file)
    out_file.write('end=time.time()\n')
    out_file.write("print('time:%s s' % (end - start))")
    out_file.close()
    print("The new test file have generated")

    #execute
    exec(open(out_file_path).read())

    
    
