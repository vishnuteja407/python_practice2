import csv
import paramiko
import sys

remote_host = "10.22.22.22"
username = "username"
password = "password"

# file_path = "/Users/vibodapa/Desktop/CEWA-DEFECT/logs"
# remote_location = "/home/zsnso02/netsimautom/"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(remote_host, username=username, password=password, timeout=4)
    command = 'cd netsimautom/ && ncs-netsim list | grep USGAATLSO02VDM0002'
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdin)
    output = stdout.read().decode('utf-8')
    print(output)
except Exception as e:
    print("Error:", e)
    ssh.close()
    sys.exit(1)  # Exit the script with an error code

# Rest of the code for reading output and writing to CSV

# Close the SSH connection in a finally block
finally:
    ssh.close()

output_lines = output.split(' ')  # Split output into lines

# Assuming the output is in a format suitable for CSV (comma-separated values)
with open('output.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    for line in output_lines:
        csv_writer.writerow(line.split(','))  # Modify this according to your output format
