import os
import re
def check_files(path):
    file_name = []
    file_name_set = set()
    for root, dirs, files in os.walk(path):
        for name in files:
            if os.path.splitext(name)[1] == '.jl':
                if len(re.findall(r"\d", str(name))) != 0:
                    print(name)
                    num = int(''.join(re.findall(r"\d", str(name))))
                    file_name.append(num)

    file_name_set = set(file_name)

    start = int(24863216/15)
    count = start
    bad_pages = []
    dict = {}
    while count > 0:
        count -= 1
        if count not in file_name_set:
            bad_pages.append(count)
    dict['bad_pages'] = bad_pages
    file = open("bad_pages.json", 'w')
    file.write(str(dict))

if __name__ == "__main__":
    path = os.getcwd()
    check_files(path)