import os 
import codecs

path = "/home/jlo/git_web/web/web_accton/uione/accton/pod_manager/"
file_list = []
start_change = "</body>"
include_line="	{% include 'preset_js.html' %}\n"

change = "js/common.js"
change_line='vendors/additional/js/common.js'
for root , dirs , files in os.walk(path):
  for archives in files :
    if os.path.splitext(archives)[1] == ".html":
      file_list.append(os.path.join(root,archives))

for archives in file_list :
  f = codecs.open(archives,encoding='utf-8')
  line_list = []
  for line in f :
    if line.find(start_change) >= 0:
      line_list.append(include_line)
    if line.find(change_line) >= 0:
      change_line = change_line.replace('X',"'")
      line_list.append(change_line)
      line_list.append(line)
      print(archives)
    else:
      line_list.append(line)
  with open (archives,'w') as file :
    for line in line_list :
      file.write(line)