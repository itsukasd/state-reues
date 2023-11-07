import re
import os

def examLine(line):
    if line is None:
        return "#SKIP"
    if line.strip()=="":
        return "#SKIP"
    # now there is no empty line
    comment_char_pattern=re.compile(r'#')
    comment_char=comment_char_pattern.match(line)
    if comment_char is not None:
        return "#SKIP"
    empty_char_pattern=re.compile(r'\s')
    ch=empty_char_pattern.match(line)
    if ch is None:
        return "#FINISH"
    # if no space in the front of line, consider the func over
    line= line.strip()
    comment_char_pattern=re.compile(r'#')
    comment_char=comment_char_pattern.match(line)
    if comment_char is not None:
        return "#SKIP"
    # when a new function find, we return #FINISH
    func_exam_pattern= re.compile(r' *def +.*:')
    if func_exam_pattern.match(line):
        return "#FINISH"
    if line=="":
        return "#SKIP"
    return line

def extractpy(filename):
    basefilename=os.path.basename(filename)
    test_name_pattern = re.compile(r'\w+(?=.py)')
    testname=test_name_pattern.search(basefilename).group()
    print('\n\033[0;35m<',testname,'>\033[0m\n')
    f=open(filename, "r")
    # match the start of the extracted function
    func_name_pattern=re.compile(r'def +'+testname+' *\( *\w+ *\) *: *')
    lines=f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        if func_name_pattern.match(lines[i]):
            print("[%s]\tfunc start found:\t\033[0;34m%s\033[0m\t" % (testname,lines[i]))
            nlines=lines[i+1:]
            break
        if i==len(lines):
            print("[%s] unable to find the location to extract code" % filename)
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

def generate_extract_file(filename):
    basefilename=os.path.basename(filename)
    test_name_pattern = re.compile(r'\w+(?=.py)')
    testname=test_name_pattern.search(basefilename).group()
    extract_file_name="_extract_"+testname+".zy"
    extract_file_absolute=os.path.join(os.path.dirname(filename),extract_file_name)
    ls=extractpy(filename)
    f=open(extract_file_absolute, "w")
    for line in ls:
        f.write(line+"\n")
    f.close()


if __name__ == '__main__':
    generate_extract_file("./test_1236.py")
    generate_extract_file("./test_1246.py")