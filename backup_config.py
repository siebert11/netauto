from netmiko import ConnectHandler
from datetime import datetime
import os 
from glob import glob
from difflib import unified_diff

files  = sorted(glob('backup_*.txt'))
# handles the IndexError occurring at the beginning where no backup_files created 
if files:
    previous_file = files.pop()
else:
    previous_file = None


now = datetime.now()

file_path = f"backup_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"

connection_info = {
    'host':'127.0.0.1',
    'port':2222,
    'username':os.environ['NET_USER'],
    'password':os.environ['NET_PASSWORD'],
    'device_type':'linux',
    }

# ConnectHandler(host='192.168.1.1', username='admin', password='password', device_type='cisco_ios')
with ConnectHandler(**connection_info) as connection: # ** means dictionary unpacking, instead of the upove
    output = connection.send_command("cat /etc/hostname")
    with open(file_path, 'w') as file:
        file.write(output)

if previous_file is None:
    print("No previous backup found, saving this one as the baseline.")
else:
    with open(previous_file) as f:
        content = f.read()
    l_p_file = content.splitlines()
    l_output = output.splitlines()
    diff = list(unified_diff(l_p_file, l_output, fromfile= previous_file, tofile= file_path, lineterm=""))
    if diff:
        for line in diff:
            print(line)
    else:
        print("No changes since last backup.")