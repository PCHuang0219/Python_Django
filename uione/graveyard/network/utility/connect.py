import paramiko
import sys
import subprocess
def connectRemoteCMD(command=''):
    vm = paramiko.SSHClient()
    vm.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    vm.connect('192.168.0.105', username='alvin', password='openstack')

    vmtransport = vm.get_transport()
    dest_addr = ('192.168.100.10', 22) #edited#
    local_addr = ('192.168.0.105', 22) #edited#
    vmchannel = vmtransport.open_channel("direct-tcpip", dest_addr, local_addr)

    jhost = paramiko.SSHClient()
    jhost.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #jhost.load_host_keys('/home/osmanl/.ssh/known_hosts') #disabled#
    jhost.connect('192.168.100.10', username='root', password='openstack', sock=vmchannel)
    #

    stdin, stdout, stderr = jhost.exec_command("source ~/adminrc && " + command) #edited#
    out_log_bash = stdout.readlines()
    err_log_bash = stderr.readlines()

    if(len(err_log_bash) > 0):
        return err_log_bash
    # print(out_log)
    # print(err_log)
    return out_log_bash
