import re
import os

def get_extract_file_name(filename):
    basefilename=os.path.basename(filename)
    test_name_pattern = re.compile(r'\w+(?=.py)')
    testname=test_name_pattern.search(basefilename).group()
    extract_file_name="_extract_"+testname+".zy"
    extract_file_absolute=os.path.join(os.path.dirname(filename),extract_file_name)
    return extract_file_absolute

def extract_file_2_list(filename):
    extract_file_absolute=get_extract_file_name(filename)
    f=open(extract_file_absolute, "r")
    lines=f.readlines()
    return lines

if __name__ == '__main__':
    # ret=get_extract_file_name(r"test_srcipt\default\test_1236.py")
    # print(ret)
    extract_file_2_list("./test_1236.py")