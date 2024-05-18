import socket
import os

server_ip = "127.0.0.1"
server_port = 6677

def start_client():
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect((server_ip,server_port))
    print(f"Connected to server address: {server_ip} port {server_port}\n")

    client_name = input("Enter name: ")

    while True:
        print("Select option: \n")
        print("1- Search Headlines\n")
        print("2- List of Sources\n")
        print("3- Quit\n")
        
        option = input("Enter option: ")
        
        if option == '1':
            search_headlines(option, cs)
        elif option == '2':
            search_sources(option, cs)
        elif option == '3':
            send_option("3", cs)
            print("Client Offline")
            break
        else:
            print("Invalid option")
    cs.close    

    
    