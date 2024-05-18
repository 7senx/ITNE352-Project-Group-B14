import socket
import json 
import threading
from newsapi import NewsApiClient 

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5443
API_KEY = '844863c15fad42cba626fb66d2c24ef2'
api = NewsApiClient(api_key=API_KEY)

def handle_clients(cs,address):
    print(f"Host {address} connected")

    client_name = cs.recv(1024).decode()
    print(f"Client '{client_name}' connected")

    while True:
        try:
            option = cs.recv(1024).decode()

            if option.startswith('1'):
                search_news(option, cs, client_name)

        except Exception as e:
            print(f"Error handling client {client_name}: {e}")
            break

    print(f"Client '{client_name}' disconnected")
    cs.close()

def search_news(option, cs, client_name):

    _, sub_option = option.split('.')
    if sub_option == '1':
        keyword = input("Enter keyword: ")
        data = newsapi.get_top_headlines(q=keyword)
        filename = f"{c}_search_keywords.json"

    elif sub_option == '2':
        category = input("Enter category (business, entertainment, general, health, science, sports, technology): ")
        data = newsapi.get_top_headlines(category=category)
        filename = f"{c}_search_category_{category}.json"

    elif sub_option == '3':
        country = input("Enter country (au, nz, ca, ae, sa, gb, us, eg, ma): ")
        data = newsapi.get_top_headlines(country=country)
        filename = f"{c}_search_country_{country}.json"

    elif sub_option == '4':
        data = newsapi.get_top_headlines()
        filename = f"{c}_list_all_headlines.json"
        with open(filename, 'w') as f:
            json.dump(data, f)

    cs.send(json.dumps(data).encode())

    def start_server():
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ss.bind((S_HOST, S_PORT))
        ss.listen(3)
        print(f"Server listening on {S_HOST}:{S_PORT}")
        while True:
            cs, client_address = ss.accept()
            client_handler = threading.Thread(target=handle_client, args=(cs, client_address))
            client_handler.start()
            
    if __name__ == "__main__":
        start_server()