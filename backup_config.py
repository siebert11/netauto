from netmiko import ConnectHandler
from datetime import datetime
import os 

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