import socket
import json

server_ip = "127.0.0.1"
server_port = 6677

def receive(cs):
    response = cs.recv(4096).decode("utf-8")
    return json.loads(response)

def send(item,cs):
    cs.send(item.encode("utf-8"))

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

def search_headline(option,cs):

    print("Select option: ")
    print("1- Search for Keywords")
    print("2- Search by Category")
    print("3- Search by Country")
    print("4- List all New Headlines")
    print("5- Back to Main Menu")

    if option == '5':
        return
    elif option in ['1','2','3','4']:
        response = receive(cs)
        print("Results: ")

        for index, item in enumerate(response['articles']):
            print(f"{index + 1}. {item['title']} - {item['description']}")

        selected_item = int(input("Enter article number: "))
        
        send(str(selected_item), client_socket)
        response = receive(client_socket)
        print("Article Details:")
        print(f"Source: {response['source']['name']}")
        print(f"Author: {response['author']}")
        print(f"Title: {response['title']}")
        print(f"URL: {response['url']}")
        print(f"Description: {response['description']}")
        print(f"Published At: {response['publishedAt']}")
        print(f"Content: {response['content']}")










    