def get_last50_lines(lines):
    line_list=[]
    for line in lines:
        line=line.replace('[0;31m','')
        line=line.replace('[0;32m','')
        line=line.replace('[0;33m','')
        line=line.replace('[0;34m','')
        line=line.replace('[0;35m','')
        line=line.replace('[0;36m','')
        line=line.replace('[0;37m','')
        line=line.replace('[0;38m','')
        line=line.replace(" recv b'",'')
        line=line.replace(r"\r\n",'\n')
        line=line.replace("'\n",'')
        line=line.replace("'",'')
        line=line.replace(r"\r",'')
        line=line.replace(r"\n",'')
        line_list.append(line)
    return line_list[-80:]
    
def decode_log(line_list):
    console_IP = "10.250.0.193"
    write_list = []
    for line in line_list:
        line = line.replace(" recv b'",'')
        line = line.replace(r"\r\n",'\n')
        line = line.replace("'\n",'')
        line = line.replace("'",'')
        line = line.replace(r"\r",'')
        line = line.replace(r"\n",'')
        write_list.append(line)
    return line_list