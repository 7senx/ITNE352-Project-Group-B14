import socket

server_ip = '127.0.0.1'
server_port = 5443
key = ' '
def handle_clients(socket,address):
    print(f"start {address}")
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



