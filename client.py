#Aim:Write a python program to create simple socket for basic information exchange between server
#and client till clint/server type bye.
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
import socket

HOST = '127.0.0.1'  # Make sure this matches the server's IP
PORT = 12345        # Must be the same as in server.py

try:
    print("Attempting to connect to server...")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("Connected to the server.")

    while True:
        client_message = input("Client: ")
        client_socket.send(client_message.encode())

        if client_message.lower() == "bye":
            print("Closing connection.")
            break

        data = client_socket.recv(1024).decode()
        print(f"Server: {data}")

        if data.lower() == "bye":
            print("Server closed the connection.")
            break

    client_socket.close()

except Exception as e:
    print(f"Error: {e}")
