import paramiko
import getpass
import os

output_file = "paramiko_data.txt"
commands = ['uname -a', 'ls -ltr', 'lscpu', 'cd netsimautom && ncs-netsim list']

cwd = os.getcwd()
path = cwd + "/" + output_file
print(path)
if os.path.exists(path):
    os.remove(path)

# device_ip_address = input("Please Enter device IP:  ")
# usr = input("Enter device username: ")
# pwd = getpass.getpass("Enter device password: ")

device_ip_address = "10.122.32.129"
usr = "zsnso02"
pwd = "rtpR0bot"

ssh = paramiko.SSHClient()

# Adding new host key to the local
# HostKeys object(in case of missing)
# AutoAddPolicy for missing host key to be set before connection setup.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# ssh.load_system_host_keys()
# ssh.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))

try:
    ssh.connect(device_ip_address, port=22, username=usr, password=pwd, timeout=5)
# disabled_algorithms={'keys': ['rsa-sha2-256', 'rsa-sha2-512']}
 
# Execute command on SSH terminal
# using exec_command
    for command in commands:
        stdin, stdout, stderr = ssh.exec_command(command)
        command_result = stdout.read()
        with open(output_file, "a") as data:
            data.write(command_result.decode())
            data.write("\n"+"***************************************************"+"\n")

        stdin.close()

except Exception as e:
    print(e.__class__)
    print(e)