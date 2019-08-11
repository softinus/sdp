import re

path = input ("Enter the target flie path : ") 
factor = float(input("Enter the factor to rescale : (0.75, 0.9, 1.0 ...)"))
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

file_write = open(path + "_new.xml", "w+")
for i in new_file:
    file_write.write(i)

file_read.close()
file_write.close()