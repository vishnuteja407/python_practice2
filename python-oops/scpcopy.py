import paramiko
import glob
import os

remote_host = "10.122.32.129"
username = "zsnso02"
password = "rtpR0bot"

file_path = "/Users/vibodapa/Desktop/CEWA-DEFECT/logs"
remote_location = "/home/zsnso02/netsimautom/"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(remote_host, username=username, password=password)
scp = ssh.open_sftp()

for file in glob.glob(os.path.join(file_path, "*")):
    print(file)
    file_name = file.split("/")[-1]
    print(file_name)
    scp.put(file, remote_location+file_name)

# Close the SCP client
scp.close()

# Close the SSH client
ssh.close()
