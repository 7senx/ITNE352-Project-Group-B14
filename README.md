# Multithreaded News Client/Server Information System

## Project Description
The project aims to develop a Python-based client-server system for real-time news exchange. The server component handles multiple client connections and retrieves news updates from NewsAPI.org, while the client script provides a user-friendly interface for querying the server and displaying news content.

## Semester
Second 2024

## Group
- **Group Name:** B14
- **Course Code:** ITNE352
- **Section:** 2
- **Members:**
  - Mahmood Alaa (ID: 202107304)
  - Husain Nabeel (ID: 202108591)

## Table of Contents
1. [Requirements](#requirements)
2. [How to Run the System](#how-to-run-the-system)
3. [Scripts Description](#scripts-description)
4. [Additional Concepts](#additional-concepts)
5. [Acknowledgments](#acknowledgments)
6. [Conclusion](#conclusion)

## Requirements
- **Dependencies:** Python 3, newsapi-python, Tkinter(to use GUI client)
- **Installation:**
  - Install Python 3 from [python.org](https://www.python.org/)
  - Install required libraries:
  ```
    pip install newsapi-python
  ```
## How to Run the System
### 1. Server Setup
1. Open a terminal window.
2. Navigate to the directory containing the server script.
3. Run the server script:
```
   python server.py
```
### 2. Client Setup
1. Open a new terminal window.
2. Navigate to the directory containing the client script.
3. Run the client script:
```
   python client.py
```
### 2. Client GUI setup (to run client with GUI)
1. Open a new terminal window
2. Navigate to the directory containing the clientgui script
3. Run the client script:
```
  python clientgui.py
```

## Scripts Description
### Server Script
- **Main Functionalities:** Handles client connections, interacts with NewsAPI, and serves news data to clients.
- **Utilized Packages:** socket, threading, json, newsapi.NewsApiClient
- **Key Functions:**
  
  - start_server: creates a TCP/IP socket, binds it to a specified IP and port, and listens for up to three connections. For each incoming connection, it spawns a new thread to handle the client using the client_handling function.
  ```
  def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(3)
    print(f"Server is listening on {SERVER_IP}:{SERVER_PORT}")
    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=client_handling, args=(client_socket, client_address))
        client_handler.start()
  ```
  
  - client_handling: logs the connection, receives the client's name, and continuously processes messages from the client. Based on the message content, it either retrieves headlines or sources via the API_interface and sends the appropriate response. It handles exceptions and closes the connection when done.
  ```
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
  ```
  
  - response: sends a JSON response to the client. It constructs the file path based on client information, reads the JSON data, and sends it over the socket, logging the action.
  ```
  def response(main_option, sub_option, client_name,client_socket):
    file_path = os.path.join(API_interface.PATH, f'B14_{client_name}_{main_option}.{sub_option}.json')

    with open(file_path) as json_file:
        data = json.load(json_file)
        client_socket.send(json.dumps(data).encode())
        print(f"File B14_{client_name}_{main_option}.{sub_option}.json sent to {client_name}")
  ```
  

### Client Script
- **Main Functionalities:** Provides a UI for user interaction, communicates with the server, and displays news content.
- **Utilized Packages:** socket, json
- **Key Functions:**
  
    - getHeadline, getSource : for sending the user request to the server based on chosen option.
    - receive_headlines, recieve_sources: to recieve the json file from the server and display it to the client.
    - start_client
  ```
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
        option = int(input("Enter your option: "))
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
  ```
  

## Additional Concepts
- **Graphical User Interface for client side**: user friendly GUI to use the system easily. (clientgui.py)

## Acknowledgments
- [Khaled Abdulrahman](https://github.com/akhaled01) helped us with understanding the project.
- [Matt Lisivick](https://github.com/mattlisiv)  provided the newsapi-python library

## Conclusion
- The Multithreaded News Client/Server Information System showcases proficiency in network programming, API integration, and user interface design, contributing to a practical understanding of modern software development principles.
