import socket
import API_interface
import threading
import json
import time
import os
SERVER_IP = "127.0.0.1"
SERVER_PORT = 6900

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(3)
    print(f"Server is listening on {SERVER_IP}:{SERVER_PORT}")
    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=client_handling, args=(client_socket, client_address))
        client_handler.start()

def client_handling(client_socket,address):
    print(f"New connection from {address}")
    client_name = client_socket.recv(10000).decode()
    print(f"Client {client_name} connected")
    while True:
        try:
            msg = client_socket.recv(10000).decode()
            if not msg:
                break
            option, criteria = msg.split(":")
            main_option, sub_option = option.split(".")

            if main_option == "1":
                API_interface.get_headlines(criteria,sub_option,client_name)
                response(main_option, sub_option, client_name,client_socket)
            elif main_option == "2":
                API_interface.get_sources(criteria,sub_option,client_name)
                response(main_option, sub_option, client_name,client_socket)
                
        except Exception as e:
            print(f"Error handling client {client_name}: {e}")
            break
    client_socket.close()
    print(f" {address} disconnected")

def response(main_option, sub_option, client_name,client_socket):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_records")
    file_path = os.path.join(path, f'B14_{client_name}_{main_option}.{sub_option}.json')

    with open(file_path) as json_file:
        data = json.load(json_file)
        client_socket.send(json.dumps(data).encode())
        print(f"File B14_{client_name}_{main_option}.{sub_option}.json sent to {client_name}")

if __name__ == "__main__":
    start_server()