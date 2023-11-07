import re
import os

def extract_core_code(file):

def check_testcase(dir_name):
    base_dir = os.path.dirname(__file__)
    directory = os.path.join(base_dir, dir_name)
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.py'):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'r') as f:
                    # do something with the file
        for sub_dir in dirnames:
            list_py_files(os.path.join(dirpath, sub_dir))

def extract_in_dir(dir_name):

    # return -1 for no testcase
    chdret=check_testcase(dir_name)
    if chdret==-1:
        print("Error: Directory '%s' have no identified testcase.\n",dir_name)
    else:
        print("Prepare extract code from %s ......",dir_name)

if __name__ == '__main__':
    extract_in_dir("./test_srcipt")
    check_e
    fd = open("runoob.txt", "r")