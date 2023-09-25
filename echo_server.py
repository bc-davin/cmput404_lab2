import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the SO_REUSEADDR option to allow reusing the same bind port
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to a specific address and port
server_address = ('localhost', 8001)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)
print(f"Listening on {server_address}")

while True:
    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    
    # Echo data back to the client
    try:
        # Echo data back to the client
        data = client_socket.recv(1024)
        if data:
            print(f"Received data: {data.decode()}")
            client_socket.sendall(data)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        client_socket.close()
