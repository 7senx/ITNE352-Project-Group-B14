import socket
import json
SERVER_IP = "127.0.0.1"
SERVER_PORT = 6900
CATEGORIES = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
COUNTRIES = ["au", "nz", "ca", "ae", "sa", "gb", "us", "eg", "ma"]
LANGUAGES = ["ar", "en"]

def start_client():
    #init client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #connect to server
    client_socket.connect((SERVER_IP, SERVER_PORT))
    print(f"Connected to server {SERVER_IP}:{SERVER_PORT}")
    #ask for client name
    client_name = input("Enter your name: ")
    send(client_name, client_socket)
    #main menu
    while True:
        print("Select option: \n")
        print("1- Search Headlines")
        print("2- List of Sources")
        print("3- Quit\n")
        
        option = (input("Enter your option: "))
        if not option.isdigit():
            print("Invalid option. Please try again.")
            continue
        option = int(option)
        if option == 1:
            getHeadline(client_socket)
        elif option == 2:
            getSource(client_socket)
        elif option == 3:
            print("Quitting program...")
            client_socket.close()
            break
        else:
            print("Invalid option. Please try again.")
    

def getHeadline(client_socket):
    #headline search menu
    print("Select option: ")
    print("1- Search for Keywords")
    print("2- Search by Category")
    print("3- Search by Country")
    print("4- List all New Headlines")
    print("5- Back to Main Menu")
    sub_option = int(input("Enter your option: "))
    #seach by keyword
    if sub_option == 1:
        criteria = input("Enter keyword: ")
        msg = f"1.{sub_option}:{criteria}"
        send(msg, client_socket)
        receive_headlines(client_socket)
    #seach by category
    elif sub_option == 2:
        print(CATEGORIES)
        criteria = input(f"\nEnter category: ")
        if criteria not in CATEGORIES:
            print("Invalid category")
            return
        msg = f"1.{sub_option}:{criteria}"
        send(msg, client_socket)
        receive_headlines(client_socket)
    #seach by country
    elif sub_option == 3:
        criteria = input(f"Enter country: {COUNTRIES}")
        if criteria not in COUNTRIES:
            print("Invalid country")
            return
        msg = f"1.{sub_option}:{criteria}"
        send(msg, client_socket)
        receive_headlines(client_socket)
    #list all new headlines
    elif sub_option == 4:
        msg = f"1.{sub_option}:null"
        send(msg, client_socket)
        receive_headlines(client_socket)
    elif sub_option == 5:
        return
    else:
        print("Invalid option")
        return
    
def getSource(client_socket):
    print("Select option: ")
    print("1- Search by category")
    print("2- Search by country")
    print("3- Search by language")
    print("4- List all")
    print("5- Back to Main Menu")
    sub_option = int(input("Enter your option: "))

    #seach by category
    if sub_option == 1:
        criteria = input(f"Enter category: {CATEGORIES}")
        if criteria not in CATEGORIES:
            print("Invalid category")
            return
        msg = f"2.{sub_option}:{criteria}"
        send(msg, client_socket)
        receive_sources(client_socket)

    #seach by country
    elif sub_option == 2:
        criteria = input(f"Enter country: {COUNTRIES}")
        if criteria not in COUNTRIES:
            print("Invalid country")
            return
        msg = f"2.{sub_option}:{criteria}"
        send(msg, client_socket)
        receive_sources(client_socket)

    #seach by language
    elif sub_option == 3:
        criteria = input(f"Enter language:{LANGUAGES} ")
        if criteria not in LANGUAGES:
            print("Invalid language")
            return
        msg = f"2.{sub_option}:{criteria}"
        send(msg, client_socket)
        receive_sources(client_socket)

    #list all
    elif sub_option == 4:
        msg = f"2.{sub_option}:null"
        send(msg, client_socket)
        receive_sources(client_socket)

    #back to main menu
    if sub_option == 5:
        return
    else:
        print("Invalid option")
        return


def receive_headlines( client_socket):
    print("Receiving Headlines")
    #receiving headlines data
    headlines_data = client_socket.recv(100000).decode()
    headlines_list = json.loads(headlines_data)
    #printing headlines list
    print("Results :")
    for index, item in enumerate(headlines_list['articles']):
        print(f"{index + 1}. {item['title']} - {item['description']}")
    #take input from user to select the article he wants to read
    selected = int(input("Enter the article number: "))
    selected_headline = headlines_list['articles'][selected-1]
    #printing selected article details
    print(f"Article {selected} Details:")
    print(f"Source: {selected_headline['source']['name']}")
    print(f"Author: {selected_headline['author']}")
    print(f"Title: {selected_headline['title']}")
    print(f"URL: {selected_headline['url']}")
    print(f"Description: {selected_headline['description']}")
    print(f"Published At: {selected_headline['publishedAt']}")

def receive_sources( client_socket):
    print("Receiving Sources")
    #receiving sources data
    sources_data = client_socket.recv(100000).decode()
    sources_list = json.loads(sources_data)
    #printing sources list
    print("Results for:")
    for index, item in enumerate(sources_list['sources']):
        print(f"{index + 1}. {item['name']}")
    #take input from user to select the source he wants to read
    selected = int(input("Enter the source number: "))
    selected_source = sources_list['sources'][selected-1]
    #printing selected source details
    print(f" Source {selected} Details:")
    print(f"Source: {selected_source['name']}")
    print(f"Country: {selected_source['country']}")
    print(f"Description: {selected_source['description']}")
    print(f"URL: {selected_source['url']}")
    print(f"Category: {selected_source['category']}")
    print(f"Language: {selected_source['language']}")

# a function to send messages to the server
def send(msg, client_socket):
    client_socket.send(msg.encode())

if __name__ == "__main__":
    start_client()