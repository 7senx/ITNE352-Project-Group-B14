import socket
import json 
import threading
from newsapi import NewsApiClient 

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5443
API_KEY = '844863c15fad42cba626fb66d2c24ef2'
api = NewsApiClient(api_key=API_KEY)

def handle_clients(socket,address):
    print(f"Host {address} connected")
    c=client_socket.recv(1024).decode()
    print(f"Client '{c}' connected")
    while True:
        try:
            choice = client_socket.recv(1024).decode()
            if choice.startswith('1.'):
                search_news(choice, client_socket, c)
        except Exception as e:
            print(f"Error handling client {c}: {e}")
            break
        print(f"Client '{c}' disconnected")
        client_socket.close()

def search_news(choice, client_socket, c):
    _, sub_choice = choice.split('.')
    if sub_choice == '1':
        keyword = input("Enter keyword: ")
        data = newsapi.get_top_headlines(q=keyword)
        filename = f"{c}_search_keywords.json"
    elif sub_choice == '2':
        category = input("Enter category (business, entertainment, general, health, science, sports, technology): ")
        data = newsapi.get_top_headlines(category=category)
        filename = f"{c}_search_category_{category}.json"
    elif sub_choice == '3':
        country = input("Enter country (au, nz, ca, ae, sa, gb, us, eg, ma): ")
        data = newsapi.get_top_headlines(country=country)
        filename = f"{c}_search_country_{country}.json"
    elif sub_choice == '4':
        data = newsapi.get_top_headlines()
        filename = f"{c}_list_all_headlines.json"
        with open(filename, 'w') as f:
         json.dump(data, f)

    client_socket.send(json.dumps(data).encode())
    def start_server():
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ss.bind((S_HOST, S_PORT))
        ss.listen(MAX_CONNECTIONS)
        print(f"Server listening on {S_HOST}:{S_PORT}")
        while True:
            client_socket, client_address = ss.accept()
            client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_handler.start()
    if __name__ == "__main__":
        start_server()