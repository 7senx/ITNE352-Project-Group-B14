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

    sub_option = input("Enter your option: ")

    if sub_option == '5':
        return
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

def search_source(option,cs):
    #print menu
    print("\nSelect option :")
    print("1- Search by Category")
    print("2- Search by Country")
    print("3- Search by Language")
    print("4- List all")
    print("5- Back to Main Menu")

    #get input and send/receive
    sub_option = input("Enter your option: ")
    if sub_option == '5':
        return
    send(sub_option,cs)
    response = receive(cs)

    #print results all results 
    print("All sources :")
    for idx, item in enumerate(response['sources']):
        print(f"{idx + 1}. {item['name']} - {item['description']}")

    #ask user for specific item
    selected_item = int(input("Enter source number: "))
    send(str(selected_item), cs)
    response = receive(cs)
    
    #print results for selected items
    print("Selected Source Details:")
    print(f"Source: {response['name']}")
    print(f"Country: {response['country']}")
    print(f"Description: {response['description']}")
    print(f"URL: {response['url']}")
    print(f"Category: {response['category']}")
    print(f"Language: {response['language']}")








    