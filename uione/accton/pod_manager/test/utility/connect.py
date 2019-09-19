import base64
import paramiko
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("192.168.30.10",port=22 , username="jlo", password="jlo")
ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command("ls /home/jlo")
for line in ssh_stdout:
    print('... ' + line.strip('\n'))
client.close()