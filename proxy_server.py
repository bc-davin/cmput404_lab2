import socket
import multiprocessing

# Echo server settings
echo_host = '127.0.0.1'  # Your echo server's IP address
echo_port = 8889  # Port for the echo server

def handle_client(client_socket):
    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        client_socket.send(data)
    
    client_socket.close()

def start_echo_server():
    echo_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    echo_server.bind((echo_host, echo_port))
    
    # Listen for incoming connections
    echo_server.listen(5)
    
    print(f"Echo server is listening on {echo_host}:{echo_port}")
    
    while True:
        # Accept incoming client connections and fork a child process
        client_socket, client_addr = echo_server.accept()
        print(f"Accepted connection from {client_addr}")
        
        client_process = multiprocessing.Process(target=handle_client, args=(client_socket,))
        client_process.start()

if __name__ == "__main__":
    start_echo_server()