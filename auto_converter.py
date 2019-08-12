import re
import sys
import os

print("execute script from : " +sys.argv[0])
print("running target file : " +sys.argv[1] + "\n")

path = ""
if sys.argv[1] == "":
    path = input ("Enter the target flie path : ")
else:
    path = sys.argv[1]

if path == "":
    print("path null error.")
    sys.exit()

factor = 1.0
factor_input = input("Enter the factor to rescale [e.g> 0.75, 0.9, 1.0 ...] [default factor : 1.0]\n --> ")
if factor_input.strip() != "":
    factor = float(factor_input)
#print(str(factor))
#sys.exit()
new_file = []

file_read = open(path, "r")
for line in file_read:
    new_line=""
    if "dp" in line and "sdp" not in line:
        inside_string= re.findall(r'\"(.+?)\"',line)
        if len(inside_string) != 1:
            continue
        dp_value= float(re.sub("\D", "", line))
        new_value = round(dp_value*factor)
        new_line= line.replace(inside_string[0], "@dimen/_" + str(new_value) + "sdp")
        print(line + "changed into : \n" + new_line, 1)

    elif "sp" in line and "ssp" not in line:
        inside_string= re.findall(r'\"(.+?)\"',line)
        if len(inside_string) != 1:
            continue
        sp_value= float(re.sub("\D", "", line))
        new_value = round(sp_value*factor)
        new_line= line.replace(inside_string[0], "@dimen/_" + str(new_value) + "ssp")
        print(line + "changed into : \n" + new_line, 1)
    
    else:
        new_line = line

    new_file.append(new_line)


filename_with_ext= os.path.basename(path)               # /path/to/some/file.txt -> /path/to/some
#print("filename_with_ext : \n"+filename_with_ext + '\n')
dirname = os.path.dirname(os.path.abspath(path))        # /path/to/some/file.txt -> /path/to/some/file
new_filename = ""
if len(filename_with_ext) >= 2:
    filename= os.path.splitext(filename_with_ext)[0]     # /path/to/some/file.txt -> file
    fileext= os.path.splitext(filename_with_ext)[1]      # /path/to/some/file.txt -> txt
    new_filename = filename + "_" + str(int(factor*100)) + "." + fileext
else:
    new_filename= path + "_new.xml"

print("result file here \n--> "+ new_filename)
file_write = open(new_filename, "w+")


for i in new_file:
    file_write.write(i)

file_read.close()
file_write.close()