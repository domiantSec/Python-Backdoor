#Command lsit
#Pwd, ls, upload, download, view files,cat,sudo nano
import os
import socket
from datetime import datetime
pt = "[+]"
s = socket.socket()
port = 8082

host = input(str(pt+"Enter Host ipaddr: "))
s.connect((host, port))
print( pt+"Connected to server"+pt )

while 1:
    command = s.recv(1024)
    command = command.decode()
    print("Command recieved!")
    print("")
    if command =="pwd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print("Command has been executed")
    elif command =="view_dir":
        print("View_dir")
        path = s.recv(1024)
        p = path.decode()
        files = os.listdir(p)
        files = str(files)
        s.send(files.encode())
        print("Command has been executed")
    elif command =="dnload":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        file_open = open(file_path, "rb")
        data = file_open.read()
        data = str(data)
        d = data.encode()
        s.send(d)
    elif command == "remove_file":
        file_path = s.recv(5000)
        f = file_path.decode()
        deleted_file = os.remove(f)
        msg = "file has been removed"
        msg = str(msg)
        msg = msg.encode()
        s.send(msg)
    elif command == "view_time":
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_time = str(current_time)
        current_time = current_time.encode()
        s.send(current_time)
    elif command == "send_file":
        file_name = s.recv(6000)
        new_file = open(file_name, "wb")
        data = s.recv(5000)
        #data  = data.decode()
        new_file.write(data)
        new_file.close()

    else:
        print(pt+ "Command not recognised")